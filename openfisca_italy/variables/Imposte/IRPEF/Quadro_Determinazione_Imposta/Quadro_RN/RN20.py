# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# Il rigo presente Rn20  utilizza le stesse variabili per il calcolo del residuo della detrazione per startup per il 2016 quindi le utilizzo

class RN20_residuo_detrazione_startup_2016(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni startup per periodo d'imposta del 2014 (Rigo RN19 col. 1 quadro RN)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('startup_RPF_2017_RN47_col3',period) - person('RP80_eccedenza_detrazione_non_fruita_e_non_piu_spettante',period)


class RN20_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2016(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = u"Residui detrazioni startup per periodo d'imposta del 2016 (Rigo RN20 col. 2 quadro RN) dell'anno corrente"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro = person('RN5_irpef_lorda',period) - (person('RN6_detrazioni_per_carichi_famigliari',period) + person('RN7_detrazione_per_lavoro',period) - person('detrazione_ulteriore_per_figli_a_carico',period))
        RP83_altre_detrazioni_da_sottrarre = ['RN12_detrazione_fruita_da_detrazioni_locazione_affitto',
                                'RN13_detrazioni_per_oneri_detraibili_19_annuali',
                                'RN13_detrazioni_per_oneri_detraibili_26_annuali',
                                'RN14_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue',
                                'RN15_detrazioni_per_spese_arredo_immobili_giovani_coppie_iva_acquisto_abitazione_annue',
                                'RN16_detrazioni_per_spese_per_interventi_finalizzati_al_risparmio_energetico_annue',
                                'RN17_totale_detrazione_oneri_Sez_VI_quadro_RP',
                                'RN18_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2014',
                                'RN19_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2015'
                                ]
        totale_da_sottrarre = round_(sum(person(detrazione, period) for detrazione in RP83_altre_detrazioni_da_sottrarre),2)
        capienza = irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro - totale_da_sottrarre
        return select([capienza<=0,
                        capienza >= person('RN20_residuo_detrazione_startup_2016',period),
                        capienza < person('RN20_residuo_detrazione_startup_2016',period)],
                        [0,
                        person('RN20_residuo_detrazione_startup_2016',period),
                        where(capienza<=person('RN20_residuo_detrazione_startup_2016',period),capienza,person('RN20_residuo_detrazione_startup_2016',period))])
