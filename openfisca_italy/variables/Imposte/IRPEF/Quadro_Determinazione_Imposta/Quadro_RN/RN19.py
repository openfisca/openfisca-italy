# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


class startup_RPF_2017_RN47_col3(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni e crediti d'imposta e deduzioni per startup del 2017 (Rigo RN47 col. 3 del modello REDDITI 2017)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class residuo_detrazione_startup_2015(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni startup per periodo d'imposta del 2014 (Rigo RN19 col. 1 quadro RN)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('startup_RPF_2017_RN47_col3',period) - person('eccedenza_detrazione_non_fruita_e_non_piu_spettante',period)


class detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2015(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = u"Residui detrazioni startup per periodo d'imposta del 2015 (Rigo RN19 col. 2 quadro RN) dell'anno corrente"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro = person('irpef_lorda',period) - (person('detrazioni_per_carichi_famigliari',period) + person('detrazione_per_lavoro',period) - person('detrazione_ulteriore_per_figli_a_carico',period))
        altre_detrazioni_da_sottrarre = ['detrazione_fruita_da_detrazioni_locazione_affitto',
                                'detrazioni_per_oneri_detraibili_19_annuali',
                                'detrazioni_per_oneri_detraibili_26_annuali',
                                'detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue',
                                'detrazioni_per_spese_arredo_immobili_giovani_coppie_iva_acquisto_abitazione_annue',
                                'detrazioni_per_spese_per_interventi_finalizzati_al_risparmio_energetico_annue',
                                'totale_detrazione_oneri_Sez_VI_quadro_RP',
                                'detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2014'
                                ]
        totale_da_sottrarre = round_(sum(person(detrazione, period) for detrazione in altre_detrazioni_da_sottrarre),2)
        capienza = irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro - totale_da_sottrarre
        return select([capienza<=0,
                        capienza >= person('residuo_detrazione_startup_2015',period),
                        capienza < person('residuo_detrazione_startup_2015',period)],
                        [0,
                        person('residuo_detrazione_startup_2015',period),
                        where(capienza<=person('residuo_detrazione_startup_2015',period),capienza,person('residuo_detrazione_startup_2015',period))])
