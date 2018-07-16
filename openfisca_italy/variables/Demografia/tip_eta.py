# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from numpy import datetime64

# This variable is to know if a person is in retirement age
class is_age_retirement(Variable):
    value_type = bool
    default_value = False
    entity = Persona
    definition_period = MONTH
    label = u"La persona è in età pensionabile?"
    def formula(person,period,parameters):
        age = person('age', period).astype(int)# to be secure that age is an int
        return age >= parameters(period).eta.eta_pensionamento

# This variable is to know if a person could work
class is_age_of_work(Variable):
    value_type = bool
    default_value = False
    entity = Persona
    definition_period = MONTH
    label = u"La persona è in età lavorativa?"
    def formula(person,period,parameters):
        age = person('age', period).astype(int)
        return age >= parameters(period).eta.eta_lavorativa

# This variable is to know if a person is adult
class is_adult(Variable):
    value_type = bool
    default_value = False
    entity = Persona
    definition_period = MONTH
    label = u"La persona è maggiorenne?"
    def formula(person,period,parameters):
        age = person('age', period).astype(int)
        return age >= parameters(period).eta.maggiore_eta

# This variable is to know if a person is adult
class eta_contributiva(Variable):
    value_type = float
    default_value = 0.0
    entity = Persona
    definition_period = MONTH
    label = u"Per quanti anni la persona ha versato i contributi"