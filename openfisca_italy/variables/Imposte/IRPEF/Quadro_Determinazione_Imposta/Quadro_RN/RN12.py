# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np


class RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN12 col.1 - Detrazione canoni di locazione e affitto terreni."
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
        RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale = person('RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale',period) # Col.1 RP71
        RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale = person('RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale',period) / 100.00 # Col.3 RP71
        percentuale_giorni = round_((person('RP71_numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale',period)/365.00),2) # Col.2 RP71 su 365 giorni
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        detrazione_senza_percentuali = select([not_(RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale == 2),
                                                reddito_per_detrazioni<=15493.71,
                                                reddito_per_detrazioni<=30987.41,
                                                reddito_per_detrazioni>=30987.41],
                                                [0,495.80,247.90,0])
        return round_((detrazione_senza_percentuali * RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale * percentuale_giorni),0)


class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale con contratti per i giovani di età compresa tra i 20 ed i 30 anni (Da inserire nel rigo RN12 e relativa al rigo RP71)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale = person('RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale',period) # Col.1 RP71
        RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale = person('RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale',period) / 100.00 # Col.3 RP71
        percentuale_giorni = round_((person('RP71_numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale',period)/365.00),2) # Col.2 RP71 su 365 giorni
        RN1_reddito_complessivo = person('RN1_reddito_complessivo',period)
        detrazione_senza_percentuali = select([not_(RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale == 0), # 0 è il corrispondente di codice_tre
                                                RN1_reddito_complessivo<=15493.71,
                                                RN1_reddito_complessivo>=15493.71],
                                                [0,991.60,0])
        return round_((detrazione_senza_percentuali * RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale * percentuale_giorni),0)


class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale (Da inserire nel rigo RN12 e relativa al rigo RP71)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale = person('RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale',period) # Col.1 RP71
        RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale = person('RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale',period) / 100.00 # Col.3 RP71
        percentuale_giorni = round_((person('RP71_numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale',period)/365.00),2) # Col.2 RP71 su 365 giorni
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        detrazione_senza_percentuali = select([not_(RP71_tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale == 1),
                                                reddito_per_detrazioni<=15493.71,
                                                reddito_per_detrazioni<=30987.41,
                                                reddito_per_detrazioni>=30987.41], # in all the other case
                                                [0,300,150,0])
        return round_((detrazione_senza_percentuali * RP71_percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale * percentuale_giorni),0)

# Detrazioni relative a rigo RP72

class detrazioni_canoni_locazione_per_lavoratori_dipendenti_che_si_trasferiscono_per_lavoro(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione per canone di locazione spettante ai lavoratori dipendenti che trasferiscono la propria residenza per motivi di lavoro (Da inserire nel rigo RN12 e relativa al rigo RP72)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        RP72_percentuale_di_spettanza_relativa_a_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro = person('RP72_percentuale_di_spettanza_relativa_a_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro',period) / 100.00
        percentuale_giorni = round_((person('RP72_numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro',period)/365.00),2)
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        # non importa sapere se il rigo è stato compilato, in quanto la percentuale di spettanza e i giorni hanno valore di default 0 e quindi se il rigo non viene compilato il risultato sara' 0
        detrazione_senza_percentuali = select([reddito_per_detrazioni<=15493.71,
                                                reddito_per_detrazioni<=30987.41,
                                                reddito_per_detrazioni>=30987.41], # in all the other case
                                                [991.60,495.80,0])
        return round_((detrazione_senza_percentuali * RP72_percentuale_di_spettanza_relativa_a_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro * percentuale_giorni),0)

# Colonna 2

class RN12_credito_residuo_da_detrazioni_locazione_affitto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = " Rigo RN12 col 2 - Credito residuo che non ha trovato capienza nell'imposta IRPEF in quanto l'ammontare delle detrazione da locazione e affitto erano maggiore dell'irpef lorda diminuita di detrazioni per lavoro e famiglia."
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
            RN5_irpef_lorda = person('RN5_irpef_lorda',period)
            detrazioni_imposta_famiglia_lavoro = person('RN8_totale_detrazioni_per_carichi_di_famiglia_e_lavoro',period)
            irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia =  RN5_irpef_lorda - detrazioni_imposta_famiglia_lavoro
            residui_detrazione_startup = person('RN18_residuo_detrazione_startup_2014',period)  + person('RN19_residuo_detrazione_startup_2015',period) +  person('RN20_residuo_detrazione_startup_2016',period) +  person('RN21_detrazioni_per_investimenti_startup',period)
            capienza = irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia - residui_detrazione_startup
            RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo = person('RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo',period)
            return select([capienza<=0,
                    capienza<RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo,
                    capienza>=RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo],
                    [RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo,
                    RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo-capienza,
                    0
                    ])
# Colonna 3

class RN12_detrazione_fruita_da_detrazioni_locazione_affitto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione fruita nell'imposta IRPEF in quanto l'ammontare delle detrazione da locazione e affitto erano minori o uguali dell'irpef lorda diminuita di detrazioni per lavoro e famiglia (Rigo RN12 col 3)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
            RN5_irpef_lorda = person('RN5_irpef_lorda',period)
            detrazioni_imposta_famiglia_lavoro = person('RN8_totale_detrazioni_per_carichi_di_famiglia_e_lavoro',period)
            irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia =  RN5_irpef_lorda - detrazioni_imposta_famiglia_lavoro
            residui_detrazione_startup = person('RN18_residuo_detrazione_startup_2014',period)  + person('RN19_residuo_detrazione_startup_2015',period) +  person('RN20_residuo_detrazione_startup_2016',period) +  person('RN21_detrazioni_per_investimenti_startup',period)
            capienza = irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia - residui_detrazione_startup
            RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo = person('RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo',period)
            return select([capienza<=0,
                    capienza<RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo,
                    capienza>=RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo],
                    [0,
                    RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo - person('RN12_credito_residuo_da_detrazioni_locazione_affitto',period),
                    RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo
                    ])
