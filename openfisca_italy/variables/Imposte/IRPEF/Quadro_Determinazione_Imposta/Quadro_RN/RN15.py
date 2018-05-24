# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np



class RN15_detrazioni_per_spese_arredo_immobili_giovani_coppie_iva_acquisto_abitazione_annue(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = u"Rigo RN15 - Detrazione per spese indicate nella sezione III C del Quadro RP (arredo immobili ristrutturati, giovani coppie, IVA per acquisto abitazione classe energetica A o B)."
    def formula(person,period,parameters):
        return round_((person('RP60_totale_rate_spesa_arredo_immobili_ristrutturati_gc_iva_acquisto_abitazione',period)*0.5),2)
