# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class canone_di_locazione_spettante_ai_lavoratori_dipendenti_che_trasferiscono_la_propria_residenza_per_motivi_di_lavoro_compilato(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "E' stato compilato rigo RP72 "
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class numero_giorni_dell_anno_immobile_adibito_ad_abitazione_principale_con_canone_di_locazione_spettante_ai_lavoratori_dipendenti(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Numero di giorni per cui è valso il contratto tra inquilini alloggi_adibiti_ad_abitazione_principale con contratti a regime convenzionale"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class numero_inquilini_relativo_a_immobile_adibito_ad_abitazione_principale_con_canone_di_locazione_spettante_ai_lavoratori_dipendenti(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Numero di inquilini per cui è valso il contratto tra inquilini alloggi_adibiti_ad_abitazione_principale con contratti a regime convenzionale"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
