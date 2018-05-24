# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
#import numpy
import numpy as np


class RN3_oneri_deducibili_totali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Oneri deducibili annuali da sottrarre al reddito lordo annuale per il calcolo dell'IRPEF"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=85"  # Always use the most official source
    def formula(person, period, parameters):
        return person('RP_39_totale_oneri_deducibili',period)
