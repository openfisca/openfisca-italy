# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

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
