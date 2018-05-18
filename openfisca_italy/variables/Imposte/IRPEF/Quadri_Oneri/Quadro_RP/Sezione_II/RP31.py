# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
import numpy as np

class contributi_fondo_pensione_negoziale_dipendenti_pubblici_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Indicare l’importo dei contributi per Contributi Fondo pensione negoziale dipendenti pubblici che il sostituto d’imposta ha dedotto dall’imponibile, relativi al punto 411 codice 4. della certificazione Unica. Rigo RP31 col.1"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == 5
            return where (codice_campo_411_valido, person('importo_punto_412_certificazione_unica',period) , np.array(0))


class contributi_fondo_pensione_negoziale_dipendenti_pubblici_quota_TFR(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Indicare l’importo dela quota TFR per Contributi Fondo pensione negoziale dipendenti pubblici che il sostituto d’imposta ha dedotto dall’imponibile, relativi al punto 411 codice 4. della certificazione Unica. Rigo RP31 col.2"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == 5
            return where (codice_campo_411_valido, person('importo_punto_414_certificazione_unica',period) , np.array(0))

# La classe contributi_fondo_pensione_negoziale_dipendenti_pubblici_non_dedotti_dal_sostituto segue un prospetto nelle appendici,essendo complessa sara' composta da più variabili
class contributi_fondo_pensione_negoziale_dipendenti_pubblici_non_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Indicare l’importo dei contributi per Contributi Fondo pensione negoziale dipendenti pubblici che il sostituto d’imposta non ha dedotto dall’imponibile, relativi al punto 411 codice 4. della certificazione Unica. Rigo RP31 col.1"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            # controllare che sia stato compilato uno dei vari righi
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == 5
            return where (codice_campo_411_valido, person('importo_punto_412_certificazione_unica',period) , np.array(0))
