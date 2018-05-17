# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# Spese sanitarie rigo rp6

# Questo rigo e' riservato ai contribuenti che nelle precedenti dichiarazioni dei redditi, avendo sostenuto spese sanitarie per un importo superiore a euro 15.493,71, hanno optato nel 2014 e/o 2015 e/o 2016 per la rateazione di tali spese.

class AnnoRataDellaDetrazioneSpeseRateizzateInPrecedenza(Enum):
    nessun_numero = u"Indica che non non si e' deciso di raetizzare la spesa negli anni di imposta passati"
    # non c'e' il primo anno in quanto dato che si parla di rateizzazione passata, se anche si fosse deciso di raetizzare l'anno scorso, l'anno presente sarebbe il secondo
    secondo_anno_rata = u"Si e' deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo e' il secondo anno"
    terzo_anno_rata = u"Si e' deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo e' il terzo anno"
    quarto_anno_rata = u"Si e' deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo e' il quarto anno"


class anno_rata_sulla_detrazione_per_spese_rateizzate_in_precedenza(Variable):
    value_type = Enum
    possible_values = AnnoRataDellaDetrazioneSpeseRateizzateInPrecedenza
    default_value = AnnoRataDellaDetrazioneSpeseRateizzateInPrecedenza.nessun_numero  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Anno della rata da indicare nel rigo RP6 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=54"  # Always use the most official source


class spese_sanitarie_raetizzate_in_precedenza(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie rateizzate in precedenza (Rigo RP6 col.2): Indicare l'importo della rata spettante per quest'anno (reperibile nei modelli dei redditi precedenti)"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=54"  # Always use the most official source
