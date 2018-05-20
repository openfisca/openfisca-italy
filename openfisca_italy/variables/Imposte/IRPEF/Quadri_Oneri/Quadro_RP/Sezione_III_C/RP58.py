# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class RP58_spesa_arredo_immobili_giovani_coppie(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP58 col.2 - Spesa arredo immobili giovani coppie - Limite massimo 16000"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source


class RP58_importo_rata_spesa_arredo_immobili_giovani_coppie(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP58 col.3 - Importo rata arredo immobili giovani coppie"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source

    def formula(person,period,parameters):
        return person('RP58_spesa_arredo_immobili_giovani_coppie',period) / 10.0

class RP58_meno_di_35_anni(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "Rigo RP58 col.1 - Barrare la casella se il requisito anagrafico è posseduto dal coniuge o dal convivente more uxorio nel 2016"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source
