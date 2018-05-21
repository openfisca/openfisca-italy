# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpt
import numpy as np


class RN33_importo_negativo_LC1_col_5(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Valore diverso da 0 se valore in LC1 colonna 5 è negativo"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        importo = person('LC1_totale_imposta_complessiva',period)- person('LC1_ritenute_CU_locazioni_brevi',period)
        return where (importo < 0, abs(importo), np.array(0))
