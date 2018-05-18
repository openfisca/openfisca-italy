# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
import numpy as np


class contributi_per_fondi_in_squilibrio_finanziario_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Indicare l’importo dei contributi per Contributi versati a fondi in squilibrio finanziario che il sostituto d’imposta ha dedotto dall’imponibile, relativi al punto 411 della certificazione Unica codice 2. Rigo RP29 col.1"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == 1
            importo = person('importo_punto_412_certificazione_unica',period)
            return where (codice_campo_411_valido,importo, np.array(0))


class contributi_per_fondi_in_squilibrio_finanziario_non_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Indicare l’importo dei contributi per Contributi versati a fondi in squilibrio finanziario che il sostituto d’imposta non ha dedotto dall’imponibile, relativi al punto 411 della certificazione Unica codice 2. Rigo RP29 col.1"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            importo_punto_413_certificazione_unica = person('importo_punto_413_certificazione_unica',period)
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == 1
            return where (codice_campo_411_valido, importo_punto_413_certificazione_unica ,0)
