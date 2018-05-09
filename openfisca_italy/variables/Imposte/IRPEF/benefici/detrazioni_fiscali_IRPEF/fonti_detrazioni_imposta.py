# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class detrazioni_per_carichi_famigliari(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni dovute per carichi di famiglia rigo RN6"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula (person,period,parameter):
        tipi_detrazioni_carichi_famigliari = ['detrazioni_per_assegni_percepiti_ex_coniuge','detrazioni_per_conigue_a_carico',
        'detrazioni_per_figli_a_carico','detrazioni_per_altri_famigliari_a_carico']
        return round_(sum(person(detrazione, period) for detrazione in tipi_detrazioni_carichi_famigliari),2)


class detrazione_per_lavoro(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni dovute per lavoro rigo RN7"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_detrazioni_lavoro = ['detrazioni_per_lavoro_dipendente','detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi',
        'detrazioni_per_pensionati']
        return round_(sum(person(detrazione, period) for detrazione in tipi_detrazioni_lavoro),2)


class detrazione_canoni_di_locazione_e_affitto_terreni_annuo (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione canoni di locazione e affitto terreni (Rigo RN12)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_detrazioni_locazione_affitto = ['detrazioni_canoni_locazione_per_lavoratori_dipendenti_che_si_trasferiscono_per_lavoro','detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_a_regime_convenzionale',
        'detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni','detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale','detrazioni_per_affitto_terreni_agricoli_ai_giovani']
        return round_(sum(person(detrazione, period) for detrazione in tipi_detrazioni_locazione_affitto),2)


class detrazioni_per_oneri_detraibili_annuali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni per oneri detraibili totali (Rigo RN13)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return round_((person('detrazioni_per_oneri_detraibili_19_annuali',period) + person('detrazioni_per_oneri_detraibili_26_annuali',period)),2)


class detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = u"Detrazioni per interventi di recupero del patrimonio edilizio e misure antisismiche totali (Rigo RN14)"
        def formula(person,period,parameters):
            detrazioni_scaglioni = ['detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_36',
                                'detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_50',
                                'detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_65',
                                'detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_70',
                                'detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_75',
                                'detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_80',
                                'detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_85',]
            return round_(sum(person(detrazione, period) for detrazione in detrazioni_scaglioni),2)
