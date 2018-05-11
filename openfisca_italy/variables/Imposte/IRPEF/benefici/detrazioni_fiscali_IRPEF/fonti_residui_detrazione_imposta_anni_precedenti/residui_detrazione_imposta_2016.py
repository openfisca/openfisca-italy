# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# Il rigo presente Rn20  utilizza le stesse variabili per il calcolo del residuo della detrazione per startup per il 2016 quindi le utilizzo

class residuo_detrazione_startup_2016(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni startup per periodo d'imposta del 2014 (Rigo RN19 col. 1 quadro RN)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('startup_RPF_2017_RN47_col3',period) - person('eccedenza_detrazione_non_fruita_e_non_piu_spettante',period)


class detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2016(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni startup per periodo d'imposta del 2016 (Rigo RN20 col. 2 quadro RN) dell'anno corrente"
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
                                'detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2015'
                                ]
        totale_da_sottrarre = round_(sum(person(detrazione, period) for detrazione in altre_detrazioni_da_sottrarre),2)
        print 'detrazione_fruita_da_detrazioni_locazione_affitto', person('detrazione_fruita_da_detrazioni_locazione_affitto',period)
        print 'detrazioni_per_oneri_detraibili_19_annuali', person('detrazioni_per_oneri_detraibili_19_annuali',period)
        print 'detrazioni_per_oneri_detraibili_26_annuali', person('detrazioni_per_oneri_detraibili_26_annuali',period)
        print 'detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue', person('detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue',period)
        print 'detrazioni_per_spese_arredo_immobili_giovani_coppie_iva_acquisto_abitazione_annue', person('detrazioni_per_spese_arredo_immobili_giovani_coppie_iva_acquisto_abitazione_annue',period)
        print 'detrazione_fruita_da_detrazioni_locazione_affitto', person('detrazione_fruita_da_detrazioni_locazione_affitto',period)
        print 'altre_detrazioni_annue_totali', person('altre_detrazioni_annue_totali',period)
        print 'detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2014', person('detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2014',period)
        print 'detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2015', person('detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2015',period)

        print 'totale da sottrarre',totale_da_sottrarre
        capienza = irpef_lorda_diminuita_di_detrazioni_famiglia_lavoro - totale_da_sottrarre
        print 'capienza',capienza
        return select([capienza<=0,
                        capienza >= person('residuo_detrazione_startup_2016',period),
                        capienza < person('residuo_detrazione_startup_2016',period)],
                        [0,
                        person('residuo_detrazione_startup_2016',period),
                        where(capienza<=person('residuo_detrazione_startup_2016',period),capienza,person('residuo_detrazione_startup_2016',period))])
