# -*- coding: utf-8 -*-

import collections
import itertools

from openfisca_core.entities import Entity

Individus = Entity(
    key = "individus",
    label = u'Individus',
    is_person = True
    )

Familles = Entity(
    key = "familles",
    label = u'Famille',
    roles = {
        'enfants': {
            'label': u'Enfants'
            },
        'parents': {
            'label': u'Parents',
            'max': 2
            }
        }
    )

FoyersFiscaux = Entity(
    key = "foyers_fiscaux",
    label = u'Déclaration d’impôts',
    roles = {
        'personnes_a_charge': {
            'label': u'Personnes à charge'
            },
        'declarants': {
            'label': u'Déclarants',
            'max': 2
            }
        }
    )

Menages = Entity(
    key = "menages",
    label = u'Logement principal',
    roles = {
        'personne_de_reference': {
            'label': u'Personne de référence',
            'max': 1
        },
        'conjoint': {
            'label': u'Conjoint',
            'max': 1
            },
        'enfants': {
            'label': u'Enfants',
            'max': 2
            },
        'autres': {
            'label': u'Autres'
            }
        }
    )

entities = [Individus, Familles, FoyersFiscaux, Menages]
