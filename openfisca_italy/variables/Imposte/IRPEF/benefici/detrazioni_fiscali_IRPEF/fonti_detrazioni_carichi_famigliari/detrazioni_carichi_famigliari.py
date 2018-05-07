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
    label = "Detrazioni dovute per carichi di famiglia "
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula (person,period,parameter):
        detrazioni_per_conigue_a_carico = person('detrazioni_per_conigue_a_carico',period)
        detrazioni_per_figli_a_carico = person('detrazioni_per_figli_a_carico',period)
        detrazioni_per_altri_famigliari_a_carico = person('detrazioni_per_altri_famigliari_a_carico',period)
        return detrazioni_per_conigue_a_carico + detrazioni_per_figli_a_carico + detrazioni_per_altri_famigliari_a_carico