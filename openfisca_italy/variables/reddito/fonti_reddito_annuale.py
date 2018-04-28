# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


# This variable is a pure input: it doesn't have a formula
class reddito_lavoro_dipendente_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period 
    label = "Reddito da lavoro dipendente"
    reference = "http://www.treccani.it/enciclopedia/redditi-da-lavoro-dipendente-dir-trib_%28Diritto-on-line%29/"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class reddito_lavoro_autonomo_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito da lavoro autonomo al netto delle detrazioni del datore di lavoro"
    reference = "http://www.ilsole24ore.com/art/SoleOnLine4/dossier/Norme%20e%20Tributi/2010/annuario-contribuente/lavoro-autonomo/2-reddito-lavoro-autonomo.shtml"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class reddito_fondiario_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito da fondiario composto da terreni e fabbricati"
    reference = "https://it.wikipedia.org/wiki/Redditi_fondiari"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class reddito_di_impresa_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito d'imprese"
    reference = "https://it.wikipedia.org/wiki/Redditi_di_impresa"  # Always use the most official source

