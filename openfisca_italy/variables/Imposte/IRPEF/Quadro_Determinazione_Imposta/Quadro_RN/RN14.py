# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np


class RN14_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = u"Rigo RN14 - Detrazioni per interventi di recupero del patrimonio edilizio e misure antisismiche totali."

    def formula(person,period,parameters):
        detrazioni_scaglioni = ['RP49_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_36',
                            'RP49_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_50',
                            'RP49_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_65',
                            'RP49_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_70',
                            'RP49_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_75',
                            'RP49_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_80',
                            'RP49_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_85',]
        return round_(sum(person(detrazione, period) for detrazione in detrazioni_scaglioni),2)
