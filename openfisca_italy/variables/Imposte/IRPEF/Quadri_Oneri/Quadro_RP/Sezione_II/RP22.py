# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *



class assegno_periodico_al_coniuge(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Assegni periodici corrisposti al coniuge"
    reference = "https://www.ecnews.it/le-deducibilita-dellassegno-periodico-corrisposto-al-coniuge/"  # Always use the most official source
