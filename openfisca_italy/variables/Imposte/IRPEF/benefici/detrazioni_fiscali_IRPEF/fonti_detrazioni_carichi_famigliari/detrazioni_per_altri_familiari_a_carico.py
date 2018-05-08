# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class detrazioni_per_altri_famigliari_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni dovute per altri famigliari a carico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameter):
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        quoziente = round_(((80000.00 - reddito_per_detrazioni)/80000.00),4)
        detrazione_spettante = round_((person('detrazioni_per_altri_famigliari_a_carico_teorica',period) * quoziente),2)
        # check if quoziente is valid or not
        print(quoziente)
        quoziente_valido = quoziente > 0 * quoziente < 1
        print(quoziente_valido)
        # if quoziente is less than 0 the deduction is 0 instead there is a formula to calculate it use the theoretical deduction
        return select( [not_(quoziente_valido),quoziente_valido],[0,detrazione_spettante])

# For the same reason introduce in deduction for child in charge i can't evaluate the month in charge.
# and the percentage of responsibility

class detrazioni_per_altri_famigliari_a_carico_teorica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni dovute per altri famigliari a carico teorica"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameter):
        return person('numero_altri_famigliari_a_carico',period) * 750


class numero_altri_famigliari_a_carico(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Numero famigliari a carico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source
