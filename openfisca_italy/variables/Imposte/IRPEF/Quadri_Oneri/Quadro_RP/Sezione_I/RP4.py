# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_I_common import *
# import numpy
import numpy as np

# Spese sanitarie rigo rp4

class RP4_spese_veicoli_per_persone_con_disabilita(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP4 col 2 - Spese veicoli per persone con disabilita, puo essere importo totale o una rata"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=53"  # Always use the most official source


class RP4_AnnoRataDellaDetrazioneSpesePerVeicoliPersoneDisabili(Enum):
    nessun_numero = u"Indica che non si vuole rateizzare la detrazione sull'importo per la spesa sui veicoli per persone con disabilita'"
    primo_anno_rata = u"Si e deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilita e questo e' il primo anno"
    secondo_anno_rata = u"Si e deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilita e questo e' il secondo anno"
    terzo_anno_rata = u"Si e deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilita  e questo e' il terzo anno"
    quarto_anno_rata = u"Si e deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilita  e questo e' il quarto anno"


class RP4_anno_rata_sulla_detrazione_per_spese_veicoli_per_persone_con_disabilita(Variable):
    value_type = Enum
    possible_values = RP4_AnnoRataDellaDetrazioneSpesePerVeicoliPersoneDisabili
    default_value = RP4_AnnoRataDellaDetrazioneSpesePerVeicoliPersoneDisabili.nessun_numero  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Rigo RP4 col 1 - Anno della rata da indicare nel rigo RP4 se si e' deciso quest anno di rateizzare o se l'importo e' stato rateizzato fino a tre anni fa e l'anno corrente e' il quarto"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=53"  # Always use the most official source
