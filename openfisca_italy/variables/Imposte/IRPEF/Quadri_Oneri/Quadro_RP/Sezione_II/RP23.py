# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class contributi_addetti_servizi_domestici_e_familiari(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Contributi per addetti ai servizi domestici e familiari"
    reference = "https://www.fiscoetasse.com/rassegna-stampa/23384-deducibilit-dei-contributi-per-gli-addetti-ai-servizi-domestici-e-familiari-730.html"  # Always use the most official source
