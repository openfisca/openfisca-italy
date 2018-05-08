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
        detrazioni_per_conigue_a_carico = person('detrazioni_per_conigue_a_carico',period)
        detrazioni_per_figli_a_carico = person('detrazioni_per_figli_a_carico',period)
        detrazioni_per_altri_famigliari_a_carico = person('detrazioni_per_altri_famigliari_a_carico',period)
        return detrazioni_per_conigue_a_carico + detrazioni_per_figli_a_carico + detrazioni_per_altri_famigliari_a_carico


class detrazione_per_lavoro(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni dovute per lavoro rigo RN8"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        detrazioni_per_lavoro_dipendente = person('detrazioni_per_lavoro_dipendente',period)
        detrazioni_per_pensionati = person('detrazioni_per_pensionati',period)
        detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi = person('detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi',period)
        return detrazioni_per_lavoro_dipendente + detrazioni_per_pensionati + detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi
