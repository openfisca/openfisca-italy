# -*- coding: utf-8 -*-

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
    # A person's age is computed according to its data_di_nascita date.
    def formula(person, period, parameters):
        data_di_nascita = person('data_di_nascita', period)
        birth_year = data_di_nascita.astype('datetime64[Y]').astype(int) + 1970
        birth_month = data_di_nascita.astype('datetime64[M]').astype(int) % 12 + 1
        birth_day = (data_di_nascita - data_di_nascita.astype('datetime64[M]') + 1).astype(int)
        is_birthday_past = (birth_month <= period.start.month) + (birth_month == period.start.month) * (birth_day <= period.start.day)
        return (period.start.year - birth_year) - where(is_birthday_past, 0, 1)  # If the birthday is not passed this year, substract one year


class age_year(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = u"Eta' della persona (in anni)"

    def formula(person,period,parameters):
        return person('age',period)


# This variable is a pure input: it doesn't have a formula
class data_di_nascita(Variable):
    value_type = date
    default_value = date(1970, 1, 1)  # By default, is no value is set for a simulation, we consider the people involed in a simulation to be born on the 1st of Jan 1970.
    entity = Persona
    label = u"Data di nascita"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"https://it.wiktionary.org/wiki/compleanno"
