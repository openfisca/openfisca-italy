# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_II_common import *

import numpy as np


class RP29_contributi_per_fondi_in_squilibrio_finanziario_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = " Rigo RP29 col.1 - Indicare l’importo dei contributi per Contributi versati a fondi in squilibrio finanziario che il sostituto d’imposta ha dedotto dall’imponibile, relativi al punto 411 della certificazione Unica codice 2."
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_due
            importo = person('importo_punto_412_certificazione_unica',period)
            return where (codice_campo_411_valido,importo, np.array(0))


class RP29_contributi_per_fondi_in_squilibrio_finanziario_non_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = " Rigo RP29 col.2 - Indicare l’importo dei contributi per Contributi versati a fondi in squilibrio finanziario che il sostituto d’imposta non ha dedotto dall’imponibile, relativi al punto 411 della certificazione Unica codice 2."
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            # controllo se almeno un campo è compilato
            lista_campi_da_controllare = ['RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto','RP28_contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto','RP27_contributi_deducibilita_ordinaria_non_dedotti_dal_sostituto',
            'RP29_contributi_per_fondi_in_squilibrio_finanziario_dedotti_dal_sostituto','RP28_contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto','RP30_contributi_versati_per_familiari_a_carico_dedotti_dal_sostituto',
            'RP30_contributi_versati_per_familiari_a_carico_non_dedotti_dal_sostituto',
            'RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_dedotti_dal_sostituto','RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_quota_TFR','RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_non_dedotti_dal_sostituto']
            # conto campi compilati
            almeno_un_campo_compilato = False
            for campo in lista_campi_da_controllare:
                almeno_un_campo_compilato = where(almeno_un_campo_compilato,almeno_un_campo_compilato,not_(person.get_holder(campo).get_array(period) is None))
            # calcolo importo
            importo_punto_413_certificazione_unica = person('importo_punto_413_certificazione_unica',period)
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_due
            return where (almeno_un_campo_compilato * codice_campo_411_valido, importo_punto_413_certificazione_unica ,0)
