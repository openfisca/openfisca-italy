# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


# This variable is a pure input: it doesn't have a formula
class salary(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    set_input = set_input_divide_by_period  # Optional attribute. Allows user to declare a salary for a year. OpenFisca will spread the yearly amount over the months contained in the year.
    label = "Stipendio"
    reference = "https://law.gov.example/salary"  # Always use the most official source


class disposable_income(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Importo effettivo disponibile alla persona alla fine del mese"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(person, period, parameters):
        return (
            + person('salary', period)
            + person('basic_income', period)
            - person('income_tax', period)
            - person('social_security_contribution', period)
            )
