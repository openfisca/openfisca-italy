# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
class detrazioni_fiscali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni"
    reference = "http://www.dirittierisposte.it/Schede/Tasse/Agevolazioni-fiscali/detrazioni_id1109749_art.aspx"  # Always use the most official source
