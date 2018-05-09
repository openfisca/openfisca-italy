# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class spese_per_detrazione_affitto_terreni_agricoli_ai_giovani(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese per detrazione affitto terreni agricoli ai giovani (Rigo RP73)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
