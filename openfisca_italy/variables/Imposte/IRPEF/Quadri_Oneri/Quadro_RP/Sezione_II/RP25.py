# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class spese_mediche_e_assistenza_disabili(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese mediche e di assistenza per disabili"
    reference = "http://www.fiscooggi.it/normativa-e-prassi/articolo/erogazioni-istituzioni-religiosededucibili-se-quietanzate-dallente"  # Always use the most official source
