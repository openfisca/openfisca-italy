# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from numpy import datetime64


class age(Variable):
    value_type = int
    entity = Persona
    definition_period = MONTH
    label = u"Eta' della persona (in anni)"
    # A person's age is computed according to its birth date.
    def formula(person, period, parameters):
        birth = person('birth', period)
        return (datetime64(period.date) - birth).astype('timedelta64[Y]')


# This variable is a pure input: it doesn't have a formula
class birth(Variable):
    value_type = date
    default_value = date(1970, 1, 1)  # By default, is no value is set for a simulation, we consider the people involed in a simulation to be born on the 1st of Jan 1970.
    entity = Persona
    label = u"Data di nascita"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"https://it.wiktionary.org/wiki/compleanno"


# This variable is to know if a person is in retirement age
class isAgeRetirement(Variable):
    value_type = bool
    default_value = False
    entity = Persona
    definition_period = MONTH
    label = u"La persona è in età pensionabile?"
    def formula(person,period,parameters):
        age = person('age', period).astype(int)# to be secure that age is an int
        return age >= parameters(period).eta.eta_pensionamento

# This variable is to know if a person could work
class isAgeOfWork(Variable):
    value_type = bool
    default_value = False
    entity = Persona
    definition_period = MONTH
    label = u"La persona è in età lavorativa?"
    def formula(person,period,parameters):
        age = person('age', period).astype(int)
        return age >= parameters(period).eta.eta_lavorativa

# This variable is to know if a person is adult
class isAdult(Variable):
    value_type = bool
    default_value = False
    entity = Persona
    definition_period = MONTH
    label = u"La persona è maggiorenne?"
    def formula(person,period,parameters):
        age = person('age', period).astype(int)
        return age >= parameters(period).eta.maggiore_eta
