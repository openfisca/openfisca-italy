# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

class detrazioni_per_assegni_percepiti_ex_coniuge(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni dovute per carichi di famiglia rigo RN6"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        sono_stati_percepiti_redditi_per_assegni_da_ex_coniuge = person('sono_stati_percepiti_redditi_per_assegni_da_ex_coniuge',period)
        return select([not_(sono_stati_percepiti_redditi_per_assegni_da_ex_coniuge),
            reddito_per_detrazioni<=8000,reddito_per_detrazioni<=15000,
            reddito_per_detrazioni<=55000,reddito_per_detrazioni>=55000],
                    [0,
                    person('detrazione_per_assegni_ex_coniuge_con_reddito_detrazione_inferiore_8000',period),
                    person('detrazione_per_assegni_ex_coniuge_con_reddito_detrazione_inferiore_15000',period),
                    person('detrazione_per_assegni_ex_coniuge_con_reddito_detrazione_inferiore_55000',period),
                    0])


class sono_stati_percepiti_redditi_per_assegni_da_ex_coniuge(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La persona ha percepito reddito tramite assegni dell'ex coniuge?"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source



class detrazione_per_assegni_ex_coniuge_con_reddito_detrazione_inferiore_8000(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Detrazioni per assegni ex coniuge con reddito di detrazione inferiore a 8000"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return np.array(1880.00) #fixed value


class detrazione_per_assegni_ex_coniuge_con_reddito_detrazione_inferiore_15000(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Detrazioni per assegni ex coniuge con reddito di detrazione inferiore a 15000"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        quoziente = round_(((15000.00-person('reddito_per_detrazioni',period))/7000.00),4)
        quoziente_valido = quoziente>0 * quoziente<1
        return where(quoziente_valido,round_((1297+(quoziente * 583.00)),2),np.array(0))


class detrazione_per_assegni_ex_coniuge_con_reddito_detrazione_inferiore_55000(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Detrazioni per assegni ex coniuge con reddito di detrazione inferiore a 55000"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        quoziente = round_(((55000.00-person('reddito_per_detrazioni',period))/40000.00),4)
        quoziente_valido = quoziente>0 * quoziente<1
        return where(quoziente_valido,round_((quoziente * 1297.00),2),np.array(0))
