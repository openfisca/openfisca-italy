# -*- coding: utf-8 -*-
from openfisca_core.model_api import *


class detrazioni_per_conigue_a_carico_reddito_inferiore_15000(Variable):
    def formula(person,period,parameters):
        quoziente = round_((person('reddito_per_detrazioni',period) / 15000),4)
        mesi_coniuge_a_carico = person('mesi_coniuge_a_carico',period)
        detrazione_spettante = round_(((800-(50*quoziente)) * (mesi_coniuge_a_carico/12)),2)
        # if quoziente is 0 this deduction can not be calculated
        return where(quoziente==0,0,detrazione_spettante)


class riforma_detrazioni_per_conigue_a_carico_reddito_inferiore_15000(Reform):
    name = "Riforma per aumentare il moltiplicatore del quoziente per consentire una detrazione maggiore a chi possiede un reddito compreso tra 0 e 15000"

    def apply(self):
        self.update_variable(detrazioni_per_conigue_a_carico_reddito_inferiore_15000)
