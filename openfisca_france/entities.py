# -*- coding: utf-8 -*-

import collections
import itertools

from openfisca_core.entities import Entity


class Familles(Entity):
    key = "famille"
    plural = "familles"
    label = u'Famille'
    roles = [
        {
            'key': 'parents',
            'label': u'Parents',
            'max': 2
            },
        {
            'key': 'enfants',
            'label': u'Enfants'
            }
        ]

class Individus(Entity):
    key = "individu"
    plural = "individus"
    label = u'Individu'
    is_person = True


class FoyersFiscaux(Entity):
    key = "foyers_fiscaux",
    label = u'Déclaration d’impôts',
    roles = [
        {
            'key': 'declarant',
            'label': u'Déclarants',
            'max': 1,
            'role_in_scenario': 'declarants'
            },
        {
            'key': 'conjoint',
            'label': u'Déclarants',
            'max': 1,
            'role_in_scenario': 'declarants'
            },
        {
            'key': 'personnes_a_charge',
            'label': u'Personnes à charge'
            },
        ]


class Menages(Entity):
    key = "menages",
    label = u'Logement principal',
    roles = [
        {
            'key': 'personne_de_reference',
            'label': u'Personne de référence',
            'max': 1
            },
        {
            'key': 'conjoint',
            'label': u'Conjoint',
            'max': 1
            },
        {
            'key': 'enfants',
            'label': u'Enfants',
            'max': 2
            },
        {
            'key': 'autres',
            'label': u'Autres'
            }
        ]

entities = [Individus, Familles, FoyersFiscaux, Menages]
