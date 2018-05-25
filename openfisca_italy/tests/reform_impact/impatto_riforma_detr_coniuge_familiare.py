# importo reform
from openfisca_italy.reforms.IRPEF.Quadro_Determinazione_Imposta.Quadro_RN.RN6.riforma_detrazioni_per_figli_a_carico import *
from openfisca_italy import ItalyTaxBenefitSystem # import tax benefit system
from openfisca_italy.scenarios import Scenario # import scenario

def init_profile(scenario):
    scenario.init_single_entity(
        period = '2017',
        parent1 = dict(
            age = 50,
            reddito_per_detrazioni= 10000,
            la_persona_non_ha_un_coniuge_a_carico = False,
            mesi_coniuge_a_carico = 12
        )
    )
    return scenario


# main
tax_benefit_system = ItalyTaxBenefitSystem() #prendi il sistema di tasse e benefici
simple_scenario = tax_benefit_system.new_scenario() # nuovo scenario normale
print "\nTipo scenario: ", simple_scenario
print "\nEseguo inizializzazine dello scenario"
simple_scenario = init_profile(simple_scenario) # inizializzo lo scenario con la situazione per calcolare la detrazione per la persona
print "\nEseguo simulazione dello scenario"
simulation = simple_scenario.new_simulation() # nuova simulazione per lo scenario normale
# Print values
print('Detrazioni per coniuge a carico con sistema senza riforma:')
print(simulation.calculate('detrazioni_per_conigue_a_carico','2017'))
