# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from __future__ import division

import datetime
import logging
from numpy import logical_not as not_, logical_or as or_, maximum as max_, minimum as min_


from openfisca_core.accessors import law
from openfisca_core.columns import FloatCol
from openfisca_core.formulas import dated_function, DatedFormulaColumn

from ..base import CAT, QUIFAM, QUIFOY, QUIMEN
from ..base import Individus, reference_formula


CHEF = QUIFAM['chef']
PREF = QUIMEN['pref']
VOUS = QUIFOY['vous']


log = logging.getLogger(__name__)


@reference_formula
class ratio_smic_salaire(DatedFormulaColumn):
    column = FloatCol
    entity_class = Individus
    label = u"Ratio smic/salaire pour le calcul de l'allègement Fillon"

    @dated_function(start = datetime.date(2012, 1, 1))
    def function_2012(self, period, nombre_heures_remunerees, salbrut, taille_entreprise, type_heures_remunerees,
                      type_sal, smic_horaire_brut = law.cotsoc.gen.smic_h_b):
        # salbrut_annuel 2012 nombre_heures_remunerees incluent hsup à partir de 2012
        smic_annuel = smic_horaire_brut * 1820  # durée légale du travail = 1820

        ratio_smic_salaire = (
            # temps_plein
            (type_heures_remunerees != 1) * smic_annuel / (salbrut + 1e-10) +
            # temps partiel
            (type_heures_remunerees == 1) * smic_annuel * nombre_heures_remunerees / 1820 / (salbrut + 1e-10)
            )
        return ratio_smic_salaire

    @dated_function(start = datetime.date(2011, 1, 1), stop = datetime.date(2011, 12, 31))
    def function_2011(self, period, nombre_heures_remunerees, salbrut, taille_entreprise, type_heures_remunerees,
                      type_sal, smic_horaire_brut = law.cotsoc.gen.smic_h_b):

        # salbrut_annuel 2011 même chose mais avec salbrut sans hsup
        smic_annuel = smic_horaire_brut * 1820  # durée légale du travail = 1820
        ratio_smic_salaire = (
            # temps_plein
            (type_heures_remunerees != 1) * smic_annuel / (salbrut + 1e-10) +
            # temps partiel
            (type_heures_remunerees == 1) * smic_annuel * nombre_heures_remunerees / 1820 / (salbrut + 1e-10)
            )
        return ratio_smic_salaire

    @dated_function(start = datetime.date(2005, 7, 1), stop = datetime.date(2010, 12, 31))
    def function_2007_2010(self, period, nombre_heures_remunerees, salbrut, taille_entreprise, type_heures_remunerees,
                           type_sal, smic_horaire_brut = law.cotsoc.gen.smic_h_b):

        smic_mensuel = smic_horaire_brut * 151.67
        ratio_smic_salaire = (
            # temps_plein
            (type_heures_remunerees != 1) * smic_mensuel / (salbrut + 1e-10) +
            (type_heures_remunerees == 1) * smic_horaire_brut * nombre_heures_remunerees / 1820 / (salbrut + 1e-10)
            )
        return ratio_smic_salaire

    def get_variable_period(self, output_period, variable_name):
        if variable_name in ["salbrut"]:
            return output_period.start.offset('first-of', 'year').period('year')
        else:
            return output_period.start.offset('first-of', 'month').period('month')

    def get_output_period(self, period):
        return period.start.offset('first-of', 'month').period('month')


@reference_formula
class allegement_fillon(DatedFormulaColumn):
    column = FloatCol
    entity_class = Individus
    label = u"Allègement de charges patronales sur les bas et moyens salaires (dit allègement Fillon)"

    @dated_function(datetime.date(2005, 7, 1))
    def function(self, period, ratio_smic_salaire, salbrut, taille_entreprise, type_sal,
                 smic_horaire_brut = law.cotsoc.gen.smic_h_b, cotsoc = law.cotsoc):

        majoration = (taille_entreprise <= 2)  # majoration éventuelle pour les petites entreprises
        taux_fillon = taux_exo_fillon(ratio_smic_salaire, majoration, cotsoc)
        allegement_fillon = (
            taux_fillon *
            salbrut *
            ((type_sal == CAT['prive_non_cadre']) | (type_sal == CAT['prive_cadre']))
            )
        return allegement_fillon

    def get_output_period(self, period):
        return period.start.offset('first-of', 'month').period('month')


@reference_formula
class alleg_cice(DatedFormulaColumn):
    column = FloatCol
    entity_class = Individus
    label = u"Crédit d'imôt pour la compétitivité et l'emploi"

    @dated_function(datetime.date(2013, 1, 1))
    def function_2013_(self, period, salbrut, sal_h_b, type_sal, taille_entreprise, cotsoc = law.cotsoc):

        taux_cice = taux_exo_cice(sal_h_b, cotsoc)
        alleg_cice = (
            taux_cice
            * salbrut
            * or_((type_sal == CAT['prive_non_cadre']), (type_sal == CAT['prive_cadre']))
            )
        return alleg_cice

    def get_output_period(self, period):
        return period.start.offset('first-of', 'month').period('month')


# Helper functions

def taux_exo_fillon(ratio_smic_salaire, majoration, P):
    '''
    Exonération Fillon
    http://www.securite-sociale.fr/comprendre/dossiers/exocotisations/exoenvigueur/fillon.htm
    '''
    # La divison par zéro engendre un warning
    # Le montant maximum de l’allègement dépend de l’effectif de l’entreprise.
    # Le montant est calculé chaque année civile, pour chaque salarié ;
    # il est égal au produit de la totalité de la rémunération annuelle telle
    # que visée à l’article L. 242-1 du code de la Sécurité sociale par un
    # coefficient.
    # Ce montant est majoré de 10 % pour les entreprises de travail temporaire
    # au titre des salariés temporaires pour lesquels elle est tenue à
    # l’obligation d’indemnisation compensatrice de congés payés.

    Pf = P.exo_bas_sal.fillon
    seuil = Pf.seuil
    tx_max = (Pf.tx_max * not_(majoration) + Pf.tx_max2 * majoration)
    if seuil <= 1:
        return 0
    return tx_max * min_(1, max_(seuil * ratio_smic_salaire - 1, 0) / (seuil - 1))


def taux_exo_cice(sal_h_b, P):
    smic_h_b = P.gen.smic_h_b
    Pc = P.exo_bas_sal.cice
    plafond = Pc.max * smic_h_b
    taux_cice = (sal_h_b <= plafond) * Pc.taux
    return taux_cice