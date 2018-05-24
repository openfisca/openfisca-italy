# coding=utf-8
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


class residui_detrazioni_start_up_2016_RN19(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni startup del 2016 da riportare all'anno successivo (Rigo RN47 col. 1 del modello REDDITI attuale o del 2018)"
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
                                'RN18_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2014'
                                ]
        totale_da_sottrarre = round_(sum(person(detrazione, period) for detrazione in RP83_altre_detrazioni_da_sottrarre),2)
        capienza = irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro - totale_da_sottrarre
        return select([capienza<=0,
                        capienza<=person('RN19_residuo_detrazione_startup_2015',period)],
                        [person('RN19_residuo_detrazione_startup_2015',period),
                        (person('RN19_residuo_detrazione_startup_2015',period)-person('RN19_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2015',period))])


class residui_detrazioni_start_up_2017_RN20(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni startup del 2017 da riportare all'anno successivo (Rigo RN47 col. 2 del modello REDDITI attuale o del 2018)"
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
                            capienza<=person('RN20_residuo_detrazione_startup_2016',period)],
                            [person('RN20_residuo_detrazione_startup_2016',period),
                            (person('RN20_residuo_detrazione_startup_2016',period)-person('RN20_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2016',period))])


class residui_detrazioni_start_up_2018_RN21(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni startup del 2018 da riportare all'anno successivo (Rigo RN47 col. 3 del modello REDDITI attuale o del 2018)"
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
                                    'RN19_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2015',
                                    'RN20_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2016'
                                    ]
            totale_da_sottrarre = round_(sum(person(detrazione, period) for detrazione in RP83_altre_detrazioni_da_sottrarre),2)
            capienza = irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro - totale_da_sottrarre
            return select([capienza<=0,
                            capienza<=person('RN21_detrazioni_per_investimenti_startup',period)],
                            [person('RN21_detrazioni_per_investimenti_startup',period),
                            (person('RN21_detrazioni_per_investimenti_startup',period)-person('RN21_detrazioni_per_investimenti_startup_utilizzata',period))])
