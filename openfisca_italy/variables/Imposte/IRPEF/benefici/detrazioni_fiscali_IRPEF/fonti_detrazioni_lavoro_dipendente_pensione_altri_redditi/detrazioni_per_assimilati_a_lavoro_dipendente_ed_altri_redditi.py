# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np
class detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni per redditi assimilati a quelli del lavoro dipendente e altri redditi"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        sono_stati_percepiti_redditi_assimilati_a_quelli_di_lavoro_dipendente = person('sono_stati_percepiti_redditi_assimilati_a_quelli_di_lavoro_dipendente',period)
        return select([not_(sono_stati_percepiti_redditi_assimilati_a_quelli_di_lavoro_dipendente),
            reddito_per_detrazioni<=4800,reddito_per_detrazioni<=55000,reddito_per_detrazioni>=55000],
                    [0,
                    person('detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi_con_reddito_detrazione_inferiore_4800',period),
                    person('detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi_con_reddito_detrazione_inferiore_55000',period),
                    0])


class sono_stati_percepiti_redditi_assimilati_a_quelli_di_lavoro_dipendente(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha percepito redditi assimilati a quelli di lavoro dipendente"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi_con_reddito_detrazione_inferiore_4800(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Detrazioni con redditi assimilati a lav.dip. e altri redditi con reddito di detrazione inferiore a 4800"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return np.array(1104.00) #fixed value


class detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi_con_reddito_detrazione_inferiore_55000(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Detrazioni con redditi assimilati a lav.dip. e altri redditi con reddito di detrazione inferiore a 55000"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        quoziente = round_(((55000.00-person('reddito_per_detrazioni',period))/50200.00),4)
        quoziente_valido = quoziente>0 * quoziente<1
        return where(quoziente_valido,round_((quoziente * 1104.00),2),np.array(0))
