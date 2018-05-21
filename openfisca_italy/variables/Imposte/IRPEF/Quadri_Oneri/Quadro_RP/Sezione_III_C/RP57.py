# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class RP57_spesa_arredo_immobili_ristrutturati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP57 col.2-5 Spesa arredo immobili ristrutturati - Limite massimo 10000 euro"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source


class RP57_importo_rata_spesa_arredo_immobili_ristrutturati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP57 col.3-6 - Importo rata arredo immobili ristrutturati"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source

    def formula(person,period,parameters):
        return person('RP57_spesa_arredo_immobili_ristrutturati',period) / 10.0

class RP57_numero_rata_spesa_arredo_immobili_ristrutturati(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = "Rigo RP57 col.1-4 - Numero rata arredo immobili ristrutturati"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source
