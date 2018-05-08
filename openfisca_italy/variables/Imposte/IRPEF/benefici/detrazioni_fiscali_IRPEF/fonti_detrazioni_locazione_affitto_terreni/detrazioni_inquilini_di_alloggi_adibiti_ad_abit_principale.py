# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale"
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
        print not_(person('inquilini_di_alloggi_adibiti_ad_abitazione_principale_compilato',period))
        print(detrazione_senza_percentuali)
        print(percentuale_di_spettanza)
        print(percentuale_giorni)
        return detrazione_senza_percentuali * percentuale_di_spettanza * percentuale_giorni


class inquilini_di_alloggi_adibiti_ad_abitazione_principale_compilato(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "E' stato indicato il codice “1” nella colonna 1 del rigo RP71 "
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class numero_giorni_dell_anno_inquilini_alloggi_adibiti_ad_abitazione_principale(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Numero di giorni per cui è valso il contratto tra inquilini"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class numero_inquilini_relativo_a_inquilini_alloggi_adibiti_ad_abitazione_principale(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Numero di inquilini"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
