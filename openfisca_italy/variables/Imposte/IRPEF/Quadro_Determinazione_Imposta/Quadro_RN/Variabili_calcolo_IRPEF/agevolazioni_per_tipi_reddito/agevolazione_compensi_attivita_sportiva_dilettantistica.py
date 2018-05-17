# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# The variable possiede_reddito_da_attivita_sportiva_dilettantistica, is a boolean and its used during the calculation of the Irpef
# Togheter with another boolean called deduzione_per_capitale_investito_proprio_compilato to understand if the subject can benefit the ACE facilitation

class possiede_reddito_da_attivita_sportiva_dilettantistica(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La persona possiede reddito d'impresa?"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return person('redditi_da_attivita_sportive_dilettantistiche',period) > 0

class compensi_per_attivita_sportive_compilato (Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La persona ha compilato il rigo RL 22 col 1 riguardo parte di reddito soggetta a ritenuta a titolo d’imposta nella dichiarazione dei redditi"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

class possiede_diritto_agevolazione_per_attivita_sportive(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La persona ha diritto all'agevolazione ACE"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period,parameters):
        return person('possiede_reddito_da_attivita_sportiva_dilettantistica',period) and person('compensi_per_attivita_sportive_compilato',period)

# The variable compensi_con_ritenuta_a_titolo_di_imposta is the first column of compensi_per_attivita_sportive_compilato field in
# RS square.
# This value is included in the calculation of gross IRPEF if possiede_diritto_agevolazione_ACE is TRUE.
# This will be transformed in credito_di_imposta
class compensi_con_ritenuta_a_titolo_di_imposta(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Compensi con ritenuta a titolo di imposta, campo del quadro RL contenente compensi per attività sportive dilettantistiche"
    reference = "https://telematici.agenziaentrate.gov.it/pdf/uni08/help/Quadro_RL.pdf"  # Always use the most official source
