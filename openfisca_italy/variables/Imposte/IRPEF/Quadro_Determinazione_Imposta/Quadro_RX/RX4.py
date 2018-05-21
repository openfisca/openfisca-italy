# -*- coding: utf-8 -*-
# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class RX4_imposta_a_debito_risultante_dalla_dichiarazione_IRPEF(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RX4 col.1 - Riportare importo rigo LC1 col.13"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        return person('LC1_imposta_a_debito',period)


class RX4_imposta_a_credito_risultante_dalla_dichiarazione_IRPEF(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RX4 col.2 - Riportare importo rigo LC1 col.14"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        return person('LC1_imposta_a_credito',period)
