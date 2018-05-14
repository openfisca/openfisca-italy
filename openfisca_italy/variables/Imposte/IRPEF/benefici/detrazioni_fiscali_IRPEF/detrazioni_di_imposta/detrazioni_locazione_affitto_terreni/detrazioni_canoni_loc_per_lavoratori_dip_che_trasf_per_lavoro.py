# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class detrazioni_canoni_locazione_per_lavoratori_dipendenti_che_si_trasferiscono_per_lavoro(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione per canone di locazione spettante ai lavoratori dipendenti che trasferiscono la propria residenza per motivi di lavoro (Rigo RP72)"
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
