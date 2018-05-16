# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Numero di  giorni dell’anno in cui l’immobile è stato adibito ad abitazione principale relativo a Detrazione per canone di locazione spettante ai lavoratori dipendenti che trasferiscono la propria residenza per motivi di lavoro (Rigo RP72 col.1)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class percentuale_di_spettanza_relativa_a_lavoratori_dipendenti_che_si_trasferiscono_per_motivi_di_lavoro(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Percentuale di spettanza relativa a Lavoratori dipendenti che trasferiscono la residenza per motivi di lavoro Rigo RP72 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
