# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# The variable possiede_reddito_impresa, is a boolean and its used during the calculation of the Irpef
# Togheter with another boolean called deduzione_per_capitale_investito_proprio_compilato to understand if the subject can benefit the ACE facilitation

class possiede_reddito_impresa(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "La persona possiede reddito d'impresa?"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
    
    def formula(person,period,parameters):
        return person('reddito_di_impresa_annuale',period) > 0 


class deduzione_per_capitale_investito_proprio_compilato(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "La persona ha compilato il rigo RS37 colonna 14 riguardo Deduzione per capitale investito proprio nella dichiarazione dei redditi"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

class possiede_diritto_agevolazione_ACE(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "La persona ha diritto all'agevolazione ACE"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period,parameters):
        return person('possiede_reddito_impresa',period) and person('deduzione_per_capitale_investito_proprio_compilato',period)

# The variable eccedenza_trasformata_in_credito_irap is the fourteenth column of deduzione_per_capitale_investito_proprio_compilato field in
# RS square.
# This value is included in the calculation of gross IRPEF if possiede_diritto_agevolazione_ACE is TRUE.
# This will be transformed in credito_di_imposta
class eccedenza_trasformata_in_credito_irap(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Eccedenza trasformata in credito IRAP"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    