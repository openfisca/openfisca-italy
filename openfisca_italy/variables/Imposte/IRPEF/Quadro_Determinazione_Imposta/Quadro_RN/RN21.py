# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# Questo file è relativo al calcolo delle detrazioni per investimenti in startup ma nel quadro RN e non RP (che invece è dettagliato nel file RP83_altre_detrazioni.py)


class RN21_detrazioni_per_investimenti_startup(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Detrazione per investimenti in startup indicata nel rigo RP80 col. 6 e riportata nel Rigo RN21 col.1"
    def formula(person,period,parameters):
        RP80_totale_detrazioni_per_investimenti_startup = person('RP80_totale_detrazioni_per_investimenti_startup',period) # rigo RP80 col 6
        return RP80_totale_detrazioni_per_investimenti_startup


class RN21_detrazioni_per_investimenti_startup_utilizzata(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Detrazioni effettivamente utilizzata per investimenti in startup (Rigo RN21 col. 2 quadro RN) dell'anno corrente"
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
                        capienza >= person('RN21_detrazioni_per_investimenti_startup',period),
                        capienza < person('RN21_detrazioni_per_investimenti_startup',period)],
                        [0,
                        person('RN21_detrazioni_per_investimenti_startup',period),
                        where(capienza<=person('RN21_detrazioni_per_investimenti_startup',period),capienza,person('RN21_detrazioni_per_investimenti_startup',period))])
