# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class RN6_detrazioni_per_coniuge_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RN 26 col.1 - Detrazioni dovute per coniuge a carico"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('detrazioni_per_conigue_a_carico',period)



class RN6_detrazioni_per_figli_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RN 26 col.2 - Detrazioni dovute per figli a carico"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('detrazioni_per_figli_a_carico',period)


class RN6_detrazioni_per_altri_familiari_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RN 26 col.4 - Detrazioni dovute per altri familiari a carico"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('detrazioni_per_altri_famigliari_a_carico',period)


class RN6_detrazione_ulteriore_per_figli_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RN 26 col.3 - Detrazioni dovute per ulteriori figli a carico"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('detrazione_ulteriore_per_figli_a_carico',period)


class RN6_detrazioni_per_carichi_famigliari(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RN 26 totale - Detrazioni dovute per carichi di famiglia"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula (person,period,parameter):
        tipi_detrazioni_carichi_famigliari = ['RN6_detrazioni_per_coniuge_a_carico',
        'RN6_detrazioni_per_figli_a_carico','RN6_detrazioni_per_altri_familiari_a_carico','RN6_detrazione_ulteriore_per_figli_a_carico']
        return round_(sum(person(detrazione, period) for detrazione in tipi_detrazioni_carichi_famigliari),2)
