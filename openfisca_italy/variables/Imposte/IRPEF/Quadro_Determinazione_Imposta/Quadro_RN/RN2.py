# coding=utf-8
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# This variable is substracted from gross annual income to calculate the gross annual IRPEF, it is a fixes value decide from the State
class deduzione_abitazione_principale_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Deduzione abitazione principale annuale"
    reference = "https://www.guidafisco.it/deduzione-abitazione-principale-730-unico-rendita-catastale-1356"  # Always use the most official source

# This variable is substracted from gross monthly income to calculate the gross monthly IRPEF, it is a fixes value decide from the State
class deduzione_abitazione_principale_mensile(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = "Deduzione abitazione principale mensile"
    reference = "https://www.guidafisco.it/deduzione-abitazione-principale-730-unico-rendita-catastale-1356"  # Always use the most official source
    def formula(person,period,parameter):
        return np.array(round_(person('deduzione_abitazione_principale_annuale',period,options=[DIVIDE]),2))
