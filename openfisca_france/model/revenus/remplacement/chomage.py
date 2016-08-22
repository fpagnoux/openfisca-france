# -*- coding: utf-8 -*-

from openfisca_france.model.base import *  # noqa analysis:ignore


class chomeur_longue_duree(Variable):
    cerfa_field = {
        DECLARANT: [ u"1AI", u"1BI"],
        PERSONNE_A_CHARGE: [u"1CI", u"1DI", u"1EI"],
        }
    column = BoolCol
    entity_class = Individus
    label = u"Demandeur d'emploi inscrit depuis plus d'un an"

  # Pour toutes les variables de ce type, les pac3 ne sont plus proposés après 2007


class chomage_brut(Variable):
    column = FloatCol()
    entity_class = Individus
    label = u"Chômage brut"


class indemnites_chomage_partiel(Variable):
    column = FloatCol
    entity_class = Individus
    label = u"Indemnités de chômage partiel"


