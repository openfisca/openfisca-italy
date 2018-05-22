# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.common import *


class Variable_A(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "Variabile prova"

    def formula(person,period,parameters):
        code_used = person('code_used',period) #code used take values from SimpleEnum
        return code_used == SimpleEnum.code_one
