# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# The variable possiede_reddito_impresa, is a boolean and its used during the calculation of the Irpef
# Togheter with another boolean called compilato_RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore to understand if the subject can benefit the ACE facilitation

class possiede_reddito_impresa(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La persona possiede reddito d'impresa?"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return person('reddito_di_impresa_annuale',period) > 0

class possiede_diritto_agevolazione_ACE(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La persona ha diritto all'agevolazione ACE"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period,parameters):
        return person('possiede_reddito_impresa',period) and person('compilato_RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period)

class compilato_RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La persona ha compilato il rigo RS37 colonna 14 riguardo importo del rendimento nozionale di spettanza dell imprenditore"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
    def formula(person,period,parameters):
        return not_(person('RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period) == 0)
