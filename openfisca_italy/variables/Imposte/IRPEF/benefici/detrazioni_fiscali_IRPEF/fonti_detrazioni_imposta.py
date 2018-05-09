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
    label = "Detrazioni dovute per lavoro rigo RN8"
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
    label = "Detrazione canoni di locazione e affitto terreni"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_detrazioni_locazione_affitto = ['detrazioni_canoni_locazione_per_lavoratori_dipendenti_che_si_trasferiscono_per_lavoro','detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_a_regime_convenzionale',
        'detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni','detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale','detrazioni_per_affitto_terreni_agricoli_ai_giovani']
        return round_(sum(person(detrazione, period) for detrazione in tipi_detrazioni_locazione_affitto),2)
