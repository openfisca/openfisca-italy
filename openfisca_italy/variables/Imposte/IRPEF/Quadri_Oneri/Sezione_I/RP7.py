# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


# Spese interessi rigo rp7

class interessi_mutui_ipotecari_acquisto_abitazione_principale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Interessi mutui ipotecari acquisto abitazione principale (Rigo RP7) : Indicare gli interessi passivi, oneri accessori e quote di rivalutazione dipendenti da clausole di indicizzazione pagati per mutui ipotecari destinati all'acquisto dell'abitazione principale"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
