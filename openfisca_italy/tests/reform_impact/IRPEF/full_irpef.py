# importo reform
from openfisca_italy.reforms.IRPEF.Quadro_Determinazione_Imposta.Quadro_RN.RN5.al_IRP_red_inf_15000 import *
from openfisca_italy import ItalyTaxBenefitSystem # import tax benefit system
from openfisca_italy.scenarios import Scenario # import scenario

def init_profile(scenario):
    scenario.init_single_entity(
        period = '2017',
        parent1 = dict(
            RN1_reddito_complessivo = 50000,
            RN2_deduzione_abitazione_principale = 1500,
            RN3_oneri_deducibili_totali = 2500,
            RN22_totale_detrazioni_imposta = 4000,
            RN25_totale_altre_detrazioni_crediti_imposta = 2000
        )
    )
    return scenario


# main
tax_benefit_system = ItalyTaxBenefitSystem() #prendi il sistema di tasse e benefici
# scenario normale
print "Calcolo irpef complesso"
print "\nCreazione ed inizializzazine dello scenario di tasse e benefici normale"
simple_scenario = tax_benefit_system.new_scenario() # nuovo scenario normale
print type(tax_benefit_system)
simple_scenario = init_profile(simple_scenario) # inizializzo lo scenario con la situazione per calcolare la detrazione per la persona
print "Simulazione dello scenario di tasse e benefici normale"
simulation = simple_scenario.new_simulation() # nuova simulazione per lo scenario normale
# Print values
print('Irpef lorda:')
print(simulation.calculate('RN5_irpef_lorda','2017'))
print('Irpef netta:')
print(simulation.calculate('RN26_irpef_netta','2017'))
