# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# The variable possiede_investimenti_in_startup, is a boolean and its used during the calculation of the Irpef
# Togheter with another boolean called interessi_su_detrazione_fruita_compilato to understand if the subject can benefit the startup return of investment facilitation

class possiede_investimenti_in_startup(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "La persona possiede investimenti in startup?"
    reference = "https://www.ecnews.it/wp-content/uploads/pdf/2017-05-18_modello-redditi-pf-2017-detrazione-investimenti-start.pdf"  # Always use the most official source


class interessi_su_detrazione_fruita_compilato (Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "La persona ha compilato il rigo RP80 colonna 8 riguardo parte di Recupero per decadenza Start-up nella dichiarazione dei redditi"
    reference = "https://www.ecnews.it/wp-content/uploads/pdf/2017-05-18_modello-redditi-pf-2017-detrazione-investimenti-start.pdf"  # Always use the most official source

class possiede_diritto_agevolazione_per_recupero_detrazione_startup(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "La persona ha diritto all'agevolazione per il recupero della detrazione da startup"
    reference = "https://www.ecnews.it/wp-content/uploads/pdf/2017-05-18_modello-redditi-pf-2017-detrazione-investimenti-start.pdf"  # Always use the most official source

    def formula(person, period,parameters):
        return person('possiede_investimenti_in_startup',period) and person('interessi_su_detrazione_fruita_compilato',period)

# The variable recupero_detrazione is the first column of interessi_su_detrazione_fruita_compilato field in
# RP square.
# This value is included in the calculation of gross IRPEF if possiede_diritto_agevolazione_per_recupero_detrazione_startup is TRUE.
# This will be transformed in deductions
class interessi_su_detrazione_fruita(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Compensi con ritenuta a titolo di imposta, campo del quadro RL contenente compensi per attività sportive dilettantistiche"
    reference = "https://www.ecnews.it/wp-content/uploads/pdf/2017-05-18_modello-redditi-pf-2017-detrazione-investimenti-start.pdf"  # Always use the most official source

    