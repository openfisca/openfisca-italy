# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class RN8_totale_detrazioni_per_carichi_di_famiglia_e_lavoro(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Totale detrazioni per carici di famiglia e lavoro Rigo RN8"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula (person,period,parameter):
        return person('RN6_detrazioni_per_carichi_famigliari',period) + person('RN7_detrazione_per_lavoro',period)
