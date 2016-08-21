# -*- coding: utf-8 -*-

import collections
import itertools

from openfisca_core.entities import Entity


Individus = Entity(
    key = "individus",
    label = u'Individus',
    is_person = True
    )

ENFANT = "enfants" # Commun avec l'entité Ménages
PARENT = "parents"

Familles = Entity(
    key = "familles",
    label = u'Famille',
    roles = {
        ENFANT: {
            'label': u'Enfants'
            },
        PARENT: {
            'label': u'Parents',
            'max': 2
            }
        }
    )

DECLARANT = 'declarants'
PERSONNE_A_CHARGE = 'personnes_a_charge'

FoyersFiscaux = Entity(
    key = "foyers_fiscaux",
    label = u'Déclaration d’impôts',
    roles = {
        PERSONNE_A_CHARGE: {
            'label': u'Personnes à charge'
            },
        DECLARANT: {
            'label': u'Déclarants',
            'max': 2
            }
        }
    )

PERSONNE_DE_REFERENCE = 'personne_de_reference'
CONJOINT = 'conjoint'
AUTRE = 'autres'

Menages = Entity(
    key = "menages",
    label = u'Logement principal',
    roles = {
        PERSONNE_DE_REFERENCE: {
            'label': u'Personne de référence',
            'max': 1
        },
        CONJOINT: {
            'label': u'Conjoint',
            'max': 1
            },
        ENFANT: {
            'label': u'Enfants',
            'max': 2
            },
        AUTRE: {
            'label': u'Autres'
            }
        }
    )

entities = [Individus, Familles, FoyersFiscaux, Menages]
