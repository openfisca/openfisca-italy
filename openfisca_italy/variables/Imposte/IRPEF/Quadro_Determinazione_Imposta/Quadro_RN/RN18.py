# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


class startup_RPF_2017_RN47_col2(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni e crediti d'imposta e deduzioni per startup del 2017 (Rigo RN47 col. 2 del modello REDDITI 2017)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class RN18_residuo_detrazione_startup_2014(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni startup per periodo d'imposta del 2014 (Rigo RN18 col. 1 quadro RN)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('startup_RPF_2017_RN47_col2',period) - person('RP80_eccedenza_detrazione_non_fruita_e_non_piu_spettante',period)


class RN18_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2014(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = u"Residui detrazioni startup per periodo d'imposta del 2014 (Rigo RN18 col. 2 quadro RN)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro = person('RN5_irpef_lorda',period) - (person('RN6_detrazioni_per_carichi_famigliari',period) + person('RN7_detrazione_per_lavoro',period) - person('detrazione_ulteriore_per_figli_a_carico',period))
        RP83_altre_detrazioni_da_sottrarre = ['RN12_detrazione_fruita_da_detrazioni_locazione_affitto',
                                'RN13_detrazioni_per_oneri_detraibili_19_annuali',
                                'RN13_detrazioni_per_oneri_detraibili_26_annuali',
                                'RN14_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue',
                                'RN15_detrazioni_per_spese_arredo_immobili_giovani_coppie_iva_acquisto_abitazione_annue',
                                'RN16_detrazioni_per_spese_per_interventi_finalizzati_al_risparmio_energetico_annue',
                                'RN17_totale_detrazione_oneri_Sez_VI_quadro_RP'
                                ]
        totale_da_sottrarre = round_(sum(person(detrazione, period) for detrazione in RP83_altre_detrazioni_da_sottrarre),2)
        capienza = irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro - totale_da_sottrarre
        return select([capienza<=0,
                        capienza >= person('RN18_residuo_detrazione_startup_2014',period),
                        capienza < person('RN18_residuo_detrazione_startup_2014',period)],
                        [0,
                        person('RN18_residuo_detrazione_startup_2014',period),
                        where(capienza<=person('RN18_residuo_detrazione_startup_2014',period),capienza,person('RN18_residuo_detrazione_startup_2014',period))])
