# importo reform
from openfisca_italy.reforms.IRPEF.Quadro_Determinazione_Imposta.Quadro_RN.RN6.rif_detr_figli_carico import *
from openfisca_italy import ItalyTaxBenefitSystem # import tax benefit system
from openfisca_italy.scenarios import Scenario # import scenario

def init_profile(scenario):
    scenario.init_single_entity(
        period = '2017',
        parent1 = dict(
            age_year = 50,
            reddito_per_detrazioni= 10000,
            la_persona_non_ha_un_coniuge_a_carico = False,
            mesi_coniuge_a_carico = 12
        )
    )
    return scenario


# main
tax_benefit_system = ItalyTaxBenefitSystem() #prendi il sistema di tasse e benefici
# scenario normale
print "Riforma per cambiare coefficente per aumentare le detrazioni percepite per coniuge a carico"
print "\nCreazione ed inizializzazine dello scenario di tasse e benefici normale"
simple_scenario = tax_benefit_system.new_scenario() # nuovo scenario normale
simple_scenario = init_profile(simple_scenario) # inizializzo lo scenario con la situazione per calcolare la detrazione per la persona
print "Simulazione dello scenario di tasse e benefici normale"
simulation = simple_scenario.new_simulation() # nuova simulazione per lo scenario normale
# Print values
print('Detrazioni per coniuge a carico con sistema senza riforma:')
print(simulation.calculate('detrazioni_per_conigue_a_carico','2017'))
# scenario con riforma
print "\nCreazione ed inizializzazine dello scenario di tasse e benefici con riforma"
riforma = riforma_detrazioni_per_conigue_a_carico_reddito_inferiore_15000(tax_benefit_system)
reform_scenario = riforma.new_scenario() # nuovo scenario normale
reform_scenario = init_profile(reform_scenario) # inizializzo lo scenario con la situazione per calcolare la detrazione per la persona
print "Simulazione dello scenario di tasse e benefici normale"
reform_simulation = reform_scenario.new_simulation() # nuova simulazione per lo scenario normale
# Print values
print('Detrazioni per coniuge a carico con sistema con riforma:')
print(reform_simulation.calculate('detrazioni_per_conigue_a_carico','2017'))
