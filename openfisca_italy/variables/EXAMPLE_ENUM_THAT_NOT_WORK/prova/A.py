# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.EXAMPLE_ENUM_THAT_NOT_WORK.common import *


class code_used(Variable):
    value_type = Enum
    possible_values=SimpleEnum
    default_value = SimpleEnum.code_one
    definition_period = YEAR
    entity = Persona
