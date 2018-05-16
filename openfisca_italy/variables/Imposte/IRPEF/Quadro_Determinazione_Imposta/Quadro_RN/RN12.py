# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np



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

# Possono essere indicate una delle seguenti detrazioni, in base al codice inserito nella colonna 1 del rigo Rp71 o più di una se vengono compilati più dichiarazioni

class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_a_regime_convenzionale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale con contratti a regime convenzionale (Da inserire nel rigo RN12 e relativa al rigo RP71)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        percentuale_di_spettanza = round_((1.00 / person('numero_inquilini_relativo_a_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_a_regime_convenzionale',period)),2)
        percentuale_giorni = round_((person('numero_giorni_dell_anno_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_a_regime_convenzionale',period)/365.00),2)
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        detrazione_senza_percentuali = select([not_(person('inquilini_di_alloggi_adibiti_ad_abitazione_principale_con_contratti_a_regime_convenzionale_compilato',period)),
                                                reddito_per_detrazioni<=15493.71,
                                                reddito_per_detrazioni<=30987.41,
                                                reddito_per_detrazioni>=30987.41], # in all the other case
                                                [0,495.80,247.90,0])
        return round_((detrazione_senza_percentuali * percentuale_di_spettanza * percentuale_giorni),0)


class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale con contratti per i giovani di età compresa tra i 20 ed i 30 anni (Da inserire nel rigo RN12 e relativa al rigo RP71)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        percentuale_di_spettanza = round_((1.00 / person('numero_inquilini_relativo_a_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni',period)),2)
        percentuale_giorni = round_((person('numero_giorni_immobile_adibito_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni',period)/365.00),2)
        reddito_totale_lordo_annuale = person('reddito_totale_lordo_annuale',period)
        detrazione_senza_percentuali = select([not_(person('canoni_di_locazione_relativi_a_contratti_di_locazione_per_abitazione_principale_per_giovani_tra_20_e_30_anni_compilato',period)),
                                                reddito_totale_lordo_annuale<=15493.71,
                                                reddito_totale_lordo_annuale>=15493.71],
                                                [0,991.60,0])
        return round_((detrazione_senza_percentuali * percentuale_di_spettanza * percentuale_giorni),0)


class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale (Da inserire nel rigo RN12 e relativa al rigo RP71)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        percentuale_di_spettanza = round_((1.00 / person('numero_inquilini_relativo_a_inquilini_alloggi_adibiti_ad_abitazione_principale',period)),2)
        percentuale_giorni = round_((person('numero_giorni_dell_anno_inquilini_alloggi_adibiti_ad_abitazione_principale',period)/365.00),2)
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        detrazione_senza_percentuali = select([not_(person('inquilini_di_alloggi_adibiti_ad_abitazione_principale_compilato',period)),
                                                reddito_per_detrazioni<=15493.71,
                                                reddito_per_detrazioni<=30987.41,
                                                reddito_per_detrazioni>=30987.41], # in all the other case
                                                [0,300,150,0])
        return round_((detrazione_senza_percentuali * percentuale_di_spettanza * percentuale_giorni),0)



class detrazioni_canoni_locazione_per_lavoratori_dipendenti_che_si_trasferiscono_per_lavoro(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione per canone di locazione spettante ai lavoratori dipendenti che trasferiscono la propria residenza per motivi di lavoro (Da inserire nel rigo RN12 e relativa al rigo RP72)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        percentuale_di_spettanza = round_((1.00 / person('numero_inquilini_relativo_a_immobile_adibito_ad_abitazione_principale_con_canone_di_locazione_spettante_ai_lavoratori_dipendenti',period)),2)
        percentuale_giorni = round_((person('numero_giorni_dell_anno_immobile_adibito_ad_abitazione_principale_con_canone_di_locazione_spettante_ai_lavoratori_dipendenti',period)/365.00),2)
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        detrazione_senza_percentuali = select([not_(person('canone_di_locazione_spettante_ai_lavoratori_dipendenti_che_trasferiscono_la_propria_residenza_per_motivi_di_lavoro_compilato',period)),
                                                reddito_per_detrazioni<=15493.71,
                                                reddito_per_detrazioni<=30987.41,
                                                reddito_per_detrazioni>=30987.41], # in all the other case
                                                [0,991.60,495.80,0])
        return round_((detrazione_senza_percentuali * percentuale_di_spettanza * percentuale_giorni),0)
