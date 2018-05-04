# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class soglia_reddito_non_tassabile_per_reddito_da_pensione(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    set_input = set_input_divide_by_period 
    label = "Reddito non tassabile per reddito da sola pensione"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    # This value should be a parameter, but the calculation of a parameter using comparison like
    # '<=' or '>=' it's an unsupport operating in OpenFisca. This is link to the Open Issue: https://github.com/openfisca/openfisca-core/issues/657 
    def formula(person,period,parameters):
        eta = person('age',period) <= 70
        return where(eta,7500,8000)