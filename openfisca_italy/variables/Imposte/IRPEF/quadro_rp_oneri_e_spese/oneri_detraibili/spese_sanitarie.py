# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# Spese sanitarie rigo rp1

class spese_sanitarie_comprensive_di_franchigia_rigo_RP1(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie (Rigo RP1 col.2)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class spese_patologie_esenti_sostenute_da_familiare(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie (Rigo RP1 col.1)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class spese_sanitarie_annue(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie (Rigo RP1 totale)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return person('spese_sanitarie_comprensive_di_franchigia_rigo_RP1',period) + person('spese_patologie_esenti_sostenute_da_familiare',period)
