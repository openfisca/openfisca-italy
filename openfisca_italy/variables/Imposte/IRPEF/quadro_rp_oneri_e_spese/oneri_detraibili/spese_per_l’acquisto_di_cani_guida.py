# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# Spese sanitarie rigo rp5

class spese_acquisto_cani_guida(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese per acquisto di cani guida (Rigo RP5 col.2). Anche in questo caso la detrazione spetta una volta ogni 4 anni salvo perdita dell'animale. Questo valore puo' essere il totale della spesa o una rata."
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class AnnoRataDellaDetrazioneSpesePerAcquistoCaniGuida(Enum):
    nessun_numero = u"Indica che non si vuola rateizzare la detrazione sull'importo per la spesa per acquisto cani guida"
    primo_anno_rata = u"Si e' deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo e' il primo anno"
    secondo_anno_rata = u"Si e' deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo e' il secondo anno"
    terzo_anno_rata = u"Si e' deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo e' il terzo anno"
    quarto_anno_rata = u"Si e' deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo e' il quarto anno"


class anno_rata_sulla_detrazione_per_spese_veicoli_per_acquisto_cani_guida(Variable):
    value_type = Enum
    possible_values = AnnoRataDellaDetrazioneSpesePerAcquistoCaniGuida
    default_value = AnnoRataDellaDetrazioneSpesePerAcquistoCaniGuida.nessun_numero  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Anno della rata da indicare nel rigo RP5 se si e' deciso quest'anno di rateizzare o se l'importo e' stato rateizzato fino a tre anni fa e l'anno corrente e' il quarto"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
