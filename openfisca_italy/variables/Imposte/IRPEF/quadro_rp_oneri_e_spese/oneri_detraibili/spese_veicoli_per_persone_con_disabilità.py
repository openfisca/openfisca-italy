# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# Spese sanitarie rigo rp4

class spese_veicoli_per_persone_con_disabilita(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese veicoli per persone con disabilita (Rigo RP4 col 2), puo essere importo totale o una rata"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    
class AnnoRataDellaDetrazioneSpesePerVeicoliPersoneDisabili(Enum):
    nessun_numero = u"Indica che non si vuole rateizzare la detrazione sull'importo per la spesa sui veicoli per persone con disabilita'"
    primo_anno_rata = u"Si e deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilita e questo e' il primo anno"
    secondo_anno_rata = u"Si e deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilita e questo e' il secondo anno"
    terzo_anno_rata = u"Si e deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilita  e questo e' il terzo anno"
    quarto_anno_rata = u"Si e deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilita  e questo e' il quarto anno"


class anno_rata_sulla_detrazione_per_spese_veicoli_per_persone_con_disabilita(Variable):
    value_type = Enum
    possible_values = AnnoRataDellaDetrazioneSpesePerVeicoliPersoneDisabili
    default_value = AnnoRataDellaDetrazioneSpesePerVeicoliPersoneDisabili.nessun_numero  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Anno della rata da indicare nel rigo RP4 se si e' deciso quest anno di rateizzare o se l'importo e' stato rateizzato fino a tre anni fa e l'anno corrente e' il quarto"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
