from copy import deepcopy

from openfisca_core.taxbenefitsystems import TaxBenefitSystem
from openfisca_core.variables import Variable
from openfisca_core.columns import FloatCol, IntCol, BoolCol
from openfisca_core.tools import assert_near, assert_equal

from openfisca_france.scenarios import Scenario
from openfisca_france.entities import entities, Individus, Familles, FoyersFiscaux, Menages
from openfisca_france.model.base import *  # noqa analysis:ignore



# When the TBS is repaired, we can use it instead of the fake one
class af(Variable):
    column = FloatCol
    entity = Familles

class salaire(Variable):
    column = FloatCol
    entity = Individus

class age(Variable):
    column = IntCol
    entity = Individus

class autonomie_financiere(Variable):
    column = BoolCol
    entity = Individus

class DummyTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        TaxBenefitSystem.__init__(self, entities)
        self.Scenario = Scenario
        self.add_variables(af, salaire, age, autonomie_financiere)

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


    assert_near(simulation.get_entity_id(Familles), [0,0,0,0,1,1])
    assert_equal(
        simulation.get_role_in_entity(Familles),
        [PARENT, PARENT, ENFANT, ENFANT, PARENT, ENFANT]
        )
    assert_near(simulation.get_position_in_entity(Familles), [0,1,2,3,0,1])

    assert_equal(
        simulation.get_role_in_entity(FoyersFiscaux),
        [DECLARANT, CONJOINT, PERSONNE_A_CHARGE, PERSONNE_A_CHARGE, DECLARANT, PERSONNE_A_CHARGE])

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

    salaire_conjoint_par_menage = simulation.sum_in_entity(salaire, entity = Menages, role = CONJOINT)

    assert_near(salaire_conjoint_par_menage, [1500, 0])

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

TEST_CASE_AGES = deepcopy(TEST_CASE)
AGES = [40, 37, 7, 9, 54, 20]
for (individu, age) in zip(TEST_CASE_AGES['individus'], AGES):
        individu['age'] = age

def test_nb_enfants():
    test_case = deepcopy(TEST_CASE_AGES)
    simulation = new_simulation(test_case)

    from openfisca_france.model.prestations.prestations_familiales.base_ressource import nb_enf

    assert_near(nb_enf(simulation, 2013, 3, 18), [2, 0])
    assert_near(nb_enf(simulation, 2013, 19, 50), [0, 1]) # Adults don't count

    test_case['individus'][5]['autonomie_financiere'] = True
    simulation_2 = new_simulation(test_case)

    assert_near(nb_enf(simulation_2, 2013, 19, 50), [0, 0])

def test_any_in_entity():
    test_case = deepcopy(TEST_CASE_AGES)
    simulation = new_simulation(test_case)

    age = simulation.calculate('age')
    condition_age = (age <= 18)
    has_famille_member_with_age_inf_18 = simulation.any_in_entity(condition_age, entity = Familles)
    assert_near(has_famille_member_with_age_inf_18, [True,False])

    condition_age_2 = (age > 18)
    has_famille_enfant_with_age_sup_18 = simulation.any_in_entity(condition_age_2, entity = Familles, role = ENFANT)
    assert_near(has_famille_enfant_with_age_sup_18, [False, True])

def test_max_in_entity():
    test_case = deepcopy(TEST_CASE_AGES)
    simulation = new_simulation(test_case)

    age = simulation.calculate('age')

    age_max = simulation.max_in_entity(age, entity = Familles)
    assert_near(age_max, [40, 54])

    age_max_enfants = simulation.max_in_entity(age, entity = Familles, role = ENFANT)
    assert_near(age_max_enfants, [9, 20])

def test_min_in_entity():
    test_case = deepcopy(TEST_CASE_AGES)
    simulation = new_simulation(test_case)

    age = simulation.calculate('age')

    age_min = simulation.min_in_entity(age, entity = Familles)
    assert_near(age_min, [7, 20])

    age_min_parents = simulation.min_in_entity(age, entity = Familles, role = PARENT)
    assert_near(age_min_parents, [37, 54])

def test_all_in_entity():
    test_case = deepcopy(TEST_CASE_AGES)
    simulation = new_simulation(test_case)

    age = simulation.calculate('age')

    condition_age = (age >= 18)
    all_persons_age_sup_18 = simulation.all_in_entity(condition_age, entity = Familles)
    assert_near(all_persons_age_sup_18, [False, True])

    all_parents_age_sup_18 = simulation.all_in_entity(condition_age, entity = Familles, role = PARENT)
    assert_near(all_parents_age_sup_18, [True, True])

def test_value_from_person():
    test_case = deepcopy(TEST_CASE_AGES)
    simulation = new_simulation(test_case)

    age = simulation.calculate('age')

    age_conjoint = simulation.value_from_person(age, entity = FoyersFiscaux, role = CONJOINT, default = -1)

    assert_near(age_conjoint, [37, -1])
