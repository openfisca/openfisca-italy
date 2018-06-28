# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np
# to avoid python runtime warning
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)



# This variable is a pure input: it doesn't have a formula
class reddito_catastale_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito catastale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


# This variable is a pure input: it doesn't have a formula
class reddito_affitto_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da affitti"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


# The sum of reddito_terreni_annuali and reddito_fabbricati_annuale
class reddito_fabbricati_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da fabbricati"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        reddito_catastale_annuale = person ('reddito_catastale_annuale',period)
        reddito_affitto_annuale = person('reddito_affitto_annuale',period)
        return reddito_catastale_annuale + reddito_affitto_annuale

# This variable is a pure input: it doesn't have a formula
class reddito_agrario_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito catastale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class reddito_dominicale_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito dominicale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


# The sum of reddito_catastale_annuali and reddito_dominicale_annuale
class reddito_terreni_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da terreni"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        reddito_agrario_annuale = person ('reddito_agrario_annuale',period)
        reddito_dominicale_annuale = person('reddito_dominicale_annuale',period)
        return reddito_agrario_annuale + reddito_dominicale_annuale

# The sum of reddito_terreni_annuali and reddito_fabbricati_annuale
class reddito_fondiari_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito fondiari"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"
    def formula(person,period,parameters):
        reddito_terreni_annuale = person('reddito_terreni_annuale',period)
        reddito_fabbricati_annuale = person('reddito_fabbricati_annuale',period)
        return reddito_terreni_annuale + reddito_fabbricati_annuale
