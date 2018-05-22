# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_I_common import *
# import numpy
import numpy as np


class codice_altra_spesa_rigo_RP9(Variable):
    value_type = Enum
    possible_values = CodiciAltreSpeseDetraibili
    default_value = CodiciAltreSpeseDetraibili.nessun_codice  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Codice di altra spesa indicato nel Rigo RP9 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=56"  # Always use the most official source


class importo_altra_spesa_rigo_RP9(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Importo indicato nel Rigo RP9 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=56"  # Always use the most official source
