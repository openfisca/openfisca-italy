# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


#Sezione spese


class RP59_iva_per_acquisto_abitazione_classe_energetica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP59 col.2 - IVA per acquisto abitazione classe energetica A o B"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source

#Sezione rate

class RP59_importo_rata_iva_per_acquisto_abitazione_classe_energetica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP59 col.3 - Importo rata IVA per acquisto abitazione classe energetica A o B"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source

    def formula(person,period,parameters):
        return person('RP59_iva_per_acquisto_abitazione_classe_energetica',period) / 10.0


class RP59_numero_rata_iva_per_acquisto_abitazione_classe_energetica(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = "Rigo RP59 col.1 - Numero rata importo iva per acquisto abitazione classe energetica"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source
