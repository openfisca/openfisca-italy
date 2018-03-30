# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class basic_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Reddito di base fornito agli adulti"
    reference = "https://law.gov.example/basic_income"  # Always use the most official source
    # Since Dec 1st 2016, the basic income is provided to any adult, without considering their income.
    def formula_2016_12(person, period, parameters):
        age_condition = person ('age', period) >= parameters(period).eta.maggiore_eta
        return age_condition * parameters(period).benefici.reddito_base  # This '*' is a vectorial 'if'. See http://openfisca.org/doc/coding-the-legislation/30_case_disjunction.html#simple-multiplication

    # From Dec 1st 2015 to Nov 30 2016, the basic income is provided to adults who have no income.
    # Before Dec 1st 2015, the basic income does not exist in the law, and calculating it returns its default value, which is 0.
    def formula_2015_12(person, period, parameters):
        age_condition = person('age', period) >= parameters(period).eta.maggiore_eta
        salary_condition = person('salary', period) == 0
        return age_condition * salary_condition * parameters(period).benefici.reddito_base  # The '*' is also used as a vectorial 'and'. See http://openfisca.org/doc/coding-the-legislation/25_vectorial_computing.html#forbidden-operations-and-alternatives


class housing_allowance(Variable):
    value_type = float
    entity = Household
    definition_period = MONTH
    label = "Indennità di alloggio"
    reference = "https://law.gov.example/housing_allowance"  # Always use the most official source
    end = '2016-11-30'  # This allowance was removed on the 1st of Dec 2016. Calculating it before this date will always return the variable default value, 0.

    # This allowance was introduced on the 1st of Jan 1980. Calculating it before this date will always return the variable default value, 0.
    def formula_1980(household, period, parameters):
        return household('rent', period) * parameters(period).benefici.indennita_alloggio


# By default, you can use utf-8 characters in a variable. OpenFisca web API manages utf-8 encoding.
class pension(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Pensione per gli anziani. Pensione assegnata agli anziani."
    reference = [u"https://www.inps.it/nuovoportaleinps/default.aspx?itemdir=46023"]
    def formula(person, period):
        '''
        A person's pension depends on its birth date.
		In Italy: Pensionable age depends on sex, type of work and type of pension required (anticipata/non anticipata)
        '''
        age_condition = person('age', period) >= parameters(period).eta.eta_pensionamento
        return age_condition
