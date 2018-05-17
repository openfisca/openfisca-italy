# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np


# Colonna 1
class detrazione_canoni_di_locazione_e_affitto_terreni_annuo (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione canoni di locazione e affitto terreni (Rigo RN12 col.1)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_detrazioni_locazione_affitto = ['detrazioni_canoni_locazione_per_lavoratori_dipendenti_che_si_trasferiscono_per_lavoro','detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_a_regime_convenzionale',
        'detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni','detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale','detrazioni_per_affitto_terreni_agricoli_ai_giovani']
        return round_(sum(person(detrazione, period) for detrazione in tipi_detrazioni_locazione_affitto),2)

# Possono essere indicate una delle seguenti detrazioni, in base al codice inserito nella colonna 1 del rigo Rp71 o più di una se vengono compilate più dichiarazioni

class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_a_regime_convenzionale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale con contratti a regime convenzionale (Da inserire nel rigo RN12 e relativa al rigo RP71)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71 = person('tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71',period) # Col.1 RP71
        percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale = person('percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale',period) / 100.00 # Col.3 RP71
        percentuale_giorni = round_((person('numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale',period)/365.00),2) # Col.2 RP71 su 365 giorni
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        detrazione_senza_percentuali = select([not_(tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71 == 2),
                                                reddito_per_detrazioni<=15493.71,
                                                reddito_per_detrazioni<=30987.41,
                                                reddito_per_detrazioni>=30987.41], # in all the other case
                                                [0,495.80,247.90,0])
        return round_((detrazione_senza_percentuali * percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale * percentuale_giorni),0)


class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale con contratti per i giovani di età compresa tra i 20 ed i 30 anni (Da inserire nel rigo RN12 e relativa al rigo RP71)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71 = person('tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71',period) # Col.1 RP71
        percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale = person('percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale',period) / 100.00 # Col.3 RP71
        percentuale_giorni = round_((person('numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale',period)/365.00),2) # Col.2 RP71 su 365 giorni
        reddito_complessivo = person('reddito_complessivo',period)
        detrazione_senza_percentuali = select([not_(tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71 == 0), # 0 è il corrispondente di codice_tre
                                                reddito_complessivo<=15493.71,
                                                reddito_complessivo>=15493.71],
                                                [0,991.60,0])
        return round_((detrazione_senza_percentuali * percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale * percentuale_giorni),0)


class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale (Da inserire nel rigo RN12 e relativa al rigo RP71)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71 = person('tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71',period) # Col.1 RP71
        percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale = person('percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale',period) / 100.00 # Col.3 RP71
        percentuale_giorni = round_((person('numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale',period)/365.00),2) # Col.2 RP71 su 365 giorni
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        detrazione_senza_percentuali = select([not_(tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71 == 1),
                                                reddito_per_detrazioni<=15493.71,
                                                reddito_per_detrazioni<=30987.41,
                                                reddito_per_detrazioni>=30987.41], # in all the other case
                                                [0,300,150,0])
        return round_((detrazione_senza_percentuali * percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale * percentuale_giorni),0)

# Detrazioni relative a rigo RP72

class detrazioni_canoni_locazione_per_lavoratori_dipendenti_che_si_trasferiscono_per_lavoro(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione per canone di locazione spettante ai lavoratori dipendenti che trasferiscono la propria residenza per motivi di lavoro (Da inserire nel rigo RN12 e relativa al rigo RP72)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        percentuale_di_spettanza_relativa_a_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro = person('percentuale_di_spettanza_relativa_a_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro',period) / 100.00
        percentuale_giorni = round_((person('numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro',period)/365.00),2)
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        # non importa sapere se il rigo è stato compilato, in quanto la percentuale di spettanza e i giorni hanno valore di default 0 e quindi se il rigo non viene compilato il risultato sara' 0
        detrazione_senza_percentuali = select([reddito_per_detrazioni<=15493.71,
                                                reddito_per_detrazioni<=30987.41,
                                                reddito_per_detrazioni>=30987.41], # in all the other case
                                                [991.60,495.80,0])
        return round_((detrazione_senza_percentuali * percentuale_di_spettanza_relativa_a_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro * percentuale_giorni),0)

# Detrazioni relative a rigo RP73
class detrazioni_per_affitto_terreni_agricoli_ai_giovani(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione per l’affitto di terreni agricoli ai giovani (Da inserire nel rigo RN12 e relativa al rigo RP73)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        detrazione_spettante_teorica = 0.19 * person('spese_per_detrazione_affitto_terreni_agricoli_ai_giovani',period)
        detrazione_spettante_teorica = where(detrazione_spettante_teorica>1200, 1200,detrazione_spettante_teorica)
        detrazione_senza_percentuali = select([not_(person('spese_per_detrazione_affitto_terreni_agricoli_ai_giovani_compilato',period)),
                                                True], # in all the other case
                                                [0,detrazione_spettante_teorica])
        return round_((detrazione_senza_percentuali),0)

class spese_per_detrazione_affitto_terreni_agricoli_ai_giovani_compilato(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "E' stato compilato rigo RP72 "
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

# Colonna 2


class credito_residuo_da_detrazioni_locazione_affitto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Credito residuo che non ha trovato capienza nell'imposta IRPEF in quanto l'ammontare delle detrazione da locazione e affitto erano maggiore dell'irpef lorda diminuita di detrazioni per lavoro e famiglia (Rigo RN12 col 2)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
            irpef_lorda = person('irpef_lorda',period)
            detrazioni_imposta_famiglia_lavoro = person('detrazioni_per_carichi_famigliari',period) + person('detrazione_per_lavoro',period)
            irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia =  irpef_lorda - detrazioni_imposta_famiglia_lavoro
            residuo_detrazione_startup = 0 # TODO
            capienza = irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia - residuo_detrazione_startup
            detrazione_canoni_di_locazione_e_affitto_terreni_annuo = person('detrazione_canoni_di_locazione_e_affitto_terreni_annuo',period)
            return select([capienza<=0,
                    capienza<detrazione_canoni_di_locazione_e_affitto_terreni_annuo,
                    capienza>=detrazione_canoni_di_locazione_e_affitto_terreni_annuo],
                    [detrazione_canoni_di_locazione_e_affitto_terreni_annuo,
                    detrazione_canoni_di_locazione_e_affitto_terreni_annuo-capienza,
                    0
                    ])
# Colonna 3

class detrazione_fruita_da_detrazioni_locazione_affitto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione fruita nell'imposta IRPEF in quanto l'ammontare delle detrazione da locazione e affitto erano minori o uguali dell'irpef lorda diminuita di detrazioni per lavoro e famiglia (Rigo RN12 col 3)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
            irpef_lorda = person('irpef_lorda',period)
            detrazioni_imposta_famiglia_lavoro = person('detrazioni_per_carichi_famigliari',period) + person('detrazione_per_lavoro',period)
            irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia =  irpef_lorda - detrazioni_imposta_famiglia_lavoro
            residuo_detrazione_startup = 0 # TODO
            capienza = irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia - residuo_detrazione_startup
            detrazione_canoni_di_locazione_e_affitto_terreni_annuo = person('detrazione_canoni_di_locazione_e_affitto_terreni_annuo',period)
            return select([capienza<=0,
                    capienza<detrazione_canoni_di_locazione_e_affitto_terreni_annuo,
                    capienza>=detrazione_canoni_di_locazione_e_affitto_terreni_annuo],
                    [0,
                    detrazione_canoni_di_locazione_e_affitto_terreni_annuo - person('credito_residuo_da_detrazioni_locazione_affitto',period),
                    detrazione_canoni_di_locazione_e_affitto_terreni_annuo
                    ])
