# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# Questo file è relativo al calcolo delle detrazioni per investimenti in startup ma nel quadro RN e non RP (che invece è dettagliato nel file altre_detrazioni.py)


class detrazioni_per_investimenti_startup(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Detrazione per investimenti in startup indicati nella sezione VI del Quadro RP e riportato nel Rigo RN21 col.1"
    def formula(person,period,parameters):
        totale_detrazioni_per_investimenti_startup = person('totale_detrazioni_per_investimenti_startup',period) # rigo RP80 col 6
        return totale_detrazioni_per_investimenti_startup



class detrazioni_per_investimenti_startup_utilizzata(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Detrazioni effettivamente utilizzata per investimenti in startup (Rigo RN21 col. 2 quadro RN) dell'anno corrente"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro = person('irpef_lorda',period) - (person('detrazioni_per_carichi_famigliari',period) + person('detrazione_per_lavoro',period) - person('detrazione_ulteriore_per_figli_a_carico',period))
        altre_detrazioni_da_sottrarre = ['detrazione_fruita_da_detrazioni_locazione_affitto',
                                'detrazioni_per_oneri_detraibili_19_annuali',
                                'detrazioni_per_oneri_detraibili_26_annuali',
                                'detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue',
                                'detrazioni_per_spese_arredo_immobili_giovani_coppie_iva_acquisto_abitazione_annue',
                                'detrazioni_per_spese_per_interventi_finalizzati_al_risparmio_energetico_annue',
                                'altre_detrazioni_annue_totali',
                                'detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2014',
                                'detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2015',
                                'detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2016'
                                ]
        totale_da_sottrarre = round_(sum(person(detrazione, period) for detrazione in altre_detrazioni_da_sottrarre),2)
        capienza = irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro - totale_da_sottrarre
        return select([capienza<=0,
                        capienza >= person('detrazioni_per_investimenti_startup',period),
                        capienza < person('detrazioni_per_investimenti_startup',period)],
                        [0,
                        person('detrazioni_per_investimenti_startup',period),
                        where(capienza<=person('detrazioni_per_investimenti_startup',period),capienza,person('detrazioni_per_investimenti_startup',period))])
