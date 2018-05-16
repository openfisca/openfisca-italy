# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np

# Totale
class detrazioni_per_spese_per_interventi_finalizzati_al_risparmio_energetico_annue(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = u"Detrazione per spese indicate nella sezione IV C del Quadro RP (arredo immobili ristrutturati, giovani coppie, IVA per acquisto abitazione classe energetica A o B) (Rigo RN16)"
    def formula(person,period,parameters):
        tipi_detrazioni_spese_risparmio_energetico = ['detrazioni_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_55',
                                                    'detrazioni_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_65',
                                                    'detrazioni_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_70',
                                                    'detrazioni_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_75',]
        return round_(sum(person(detrazione, period) for detrazione in tipi_detrazioni_spese_risparmio_energetico),2)
