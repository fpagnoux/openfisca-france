from copy import deepcopy

from openfisca_core.taxbenefitsystems import TaxBenefitSystem
from openfisca_core.variables import Variable
from openfisca_core.columns import FloatCol
from openfisca_core.tools import assert_near, assert_equal

from openfisca_france.scenarios import Scenario
from openfisca_france.entities import entities, Individus, Familles, FoyersFiscaux, Menages, PARENT, ENFANT, CONJOINT, PERSONNE_DE_REFERENCE

class af(Variable):
    column = FloatCol
    entity_class = Familles
    label = u"Allocations familiales"

class salaire(Variable):
    column = FloatCol
    entity_class = Individus
    label = u"Salaire"

class DummyTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        TaxBenefitSystem.__init__(self, entities)
        self.Scenario = Scenario
        self.add_variables(af, salaire)

tbs = DummyTaxBenefitSystem()

TEST_CASE = {
    'individus': [{'id': 'ind0'}, {'id': 'ind1'}, {'id': 'ind2'}, {'id': 'ind3'},{'id': 'ind4'}, {'id': 'ind5'}],
    'familles': [
        {'enfants': ['ind2', 'ind3'], 'parents': ['ind0', 'ind1']},
        {'enfants': ['ind5'], 'parents': ['ind4']}
        ],
    'foyers_fiscaux': [
        {'declarants': ['ind0', 'ind1'], 'personnes_a_charge': ['ind2', 'ind3']},
        {'personnes_a_charge': ['ind5'], 'declarants': ['ind4']}
        ],
    'menages': [
        {'conjoint': 'ind1', 'enfants': ['ind2', 'ind3'], 'personne_de_reference': 'ind0'},
        {'conjoint': None, 'enfants': ['ind5'], 'personne_de_reference': 'ind4'},
        ],
    }

def new_simulation(test_case):
    return tbs.new_scenario().init_from_test_case(
        period = 2013,
        test_case = test_case
    ).new_simulation()

def test_entities_id_and_role_columns():

    simulation = new_simulation(TEST_CASE)

    id_famille_column_name = tbs.get_entity_index_column_name(Familles)
    role_in_famille_column_name = tbs.get_entity_role_column_name(Familles)
    postion_in_famille_column_name = tbs.get_entity_position_column_name(Familles)

    assert_near(simulation.calculate(id_famille_column_name), [0,0,0,0,1,1])
    assert_equal(
        simulation.calculate(role_in_famille_column_name),
        [PARENT, PARENT, ENFANT, ENFANT, PARENT, ENFANT]
        )
    assert_near(simulation.calculate(postion_in_famille_column_name), [0,1,2,3,0,1])

    role_in_menage_column_name = tbs.get_entity_role_column_name(Menages)

    assert_equal(
        simulation.calculate(role_in_menage_column_name),
        [PERSONNE_DE_REFERENCE, CONJOINT, ENFANT, ENFANT, PERSONNE_DE_REFERENCE, ENFANT]
        )

def test_project_on_persons():
    test_case = deepcopy(TEST_CASE)
    test_case['familles'][0]['af'] = 20000

    simulation = new_simulation(test_case)

    af = simulation.calculate('af')
    af_projete = simulation.project_on_persons(af, entity = Familles)

    assert_near(af_projete, [20000, 20000, 20000, 20000, 0, 0])

def test_project_on_first_person():
    test_case = deepcopy(TEST_CASE)
    test_case['familles'][0]['af'] = 20000
    test_case['familles'][1]['af'] = 5000

    simulation = new_simulation(test_case)

    af = simulation.calculate('af')
    af_projete = simulation.project_on_first_person(af, entity = Familles)

    assert_near(af_projete, [20000, 0, 0, 0, 5000, 0])

def test_sum_in_entity():
    test_case = deepcopy(TEST_CASE)
    test_case['individus'][0]['salaire'] = 1000
    test_case['individus'][1]['salaire'] = 1500
    test_case['individus'][4]['salaire'] = 3000
    test_case['individus'][5]['salaire'] = 500

    simulation = new_simulation(test_case)

    salaire = simulation.calculate('salaire')
    salaire_total_par_famille = simulation.sum_in_entity(salaire, entity = Familles)

    assert_near(salaire_total_par_famille, [2500, 3500])

def test_transpose_to_entity():
    test_case = deepcopy(TEST_CASE)
    test_case['familles'][0]['af'] = 20000
    test_case['familles'][1]['af'] = 10000
    test_case['foyers_fiscaux'] = [
        TEST_CASE['foyers_fiscaux'][0],
        {'declarants': ['ind4']},
        {'declarants': ['ind5']}
        ]

    simulation = new_simulation(test_case)

    af = simulation.calculate('af')
    af_foyer_fiscal = simulation.transpose_to_entity(af, target_entity = FoyersFiscaux, origin_entity = Familles)

    assert_near(af_foyer_fiscal, [20000, 10000, 0])
