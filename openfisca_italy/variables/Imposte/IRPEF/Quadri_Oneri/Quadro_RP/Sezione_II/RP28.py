# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
import numpy as np


class contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Indicare l’importo dei contributi per lavoratori prima occupazione che il sostituto d’imposta ha dedotto dall’imponibile, relativi al punto 411 della certificazione Unica codice3. Rigo RP28 col.1"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            importo_punto_412_certificazione_unica_per_calcolo_RigoRP28_col_1 = person('importo_punto_412_certificazione_unica_per_calcolo_RigoRP28_col_1',period)
            importo_punto_417_certificazione_unica_per_calcolo_RigoRP28_col_1 = person('importo_punto_417_certificazione_unica_per_calcolo_RigoRP28_col_1',period)
            return  importo_punto_412_certificazione_unica_per_calcolo_RigoRP28_col_1 + importo_punto_417_certificazione_unica_per_calcolo_RigoRP28_col_1


class contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Indicare l’importo dei contributi per lavoratori prima occupazione che il sostituto d’imposta non ha dedotto dall’imponibile, relativi al punto 411 della certificazione Unica codice3. Rigo RP28 col.2"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
                # vedere se uno dei righi tra RP27 e RP31 e' stato compilato
                importo_punto_413_certificazione_unica_per_calcolo_RigoRP27_col_2 = person('importo_punto_413_certificazione_unica_per_calcolo_RigoRP27_col_2',period)
                operazione_limite_deducibilita = parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_importo_deducibile_contributi_versati_lavoratori_prima_occupazione - person('contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto',period)
                operazione_limite_deducibilita = where(operazione_limite_deducibilita>0,operazione_limite_deducibilita,np.array(0))
                return round_(min_(importo_punto_413_certificazione_unica_per_calcolo_RigoRP27_col_2,operazione_limite_deducibilita),2)


class importo_punto_412_certificazione_unica_per_calcolo_RigoRP28_col_1(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Punto 412 della Certificazione Unica"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source


class importo_punto_417_certificazione_unica_per_calcolo_RigoRP28_col_1(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Punto 417 della Certificazione Unica"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source
