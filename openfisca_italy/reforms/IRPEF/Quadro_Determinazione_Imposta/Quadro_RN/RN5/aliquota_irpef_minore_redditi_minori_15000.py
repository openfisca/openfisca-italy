# -*- coding: utf-8 -*-
from openfisca_core.model_api import *
from openfisca_core import periods

def modifica_scaglioni_IRPEF(parameters):
    reform_period = periods.period("2017")
    parameters.imposte.IRPEF.aliquote_scaglioni_IRPEF[0].rate.update(period = reform_period, value = 0.18)
    return parameters


class diminuzione_aliquota_IRPEF_redditi_inferiori_15000(Reform):
    name = "Riforma per aumentare il moltiplicatore del quoziente per consentire una detrazione maggiore a chi possiede un reddito compreso tra 0 e 15000"

    def apply(self):
        self.modify_parameters(modifier_function = modifica_scaglioni_IRPEF)
