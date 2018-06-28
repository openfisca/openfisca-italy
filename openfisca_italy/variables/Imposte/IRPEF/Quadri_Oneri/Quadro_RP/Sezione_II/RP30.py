# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_II_common import *

import numpy as np


class RP30_contributi_versati_per_familiari_a_carico_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Indicare l’importo dei contributi per Contributi versati per carichi familiari che il sostituto d’imposta ha dedotto dall’imponibile, relativi al punto 421 della certificazione Unica. Rigo RP30 col.1"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            punto_421_certificazione_unica_compilato = not_(person('importo_punto_421_certificazione_unica',period)==0)
            return where(punto_421_certificazione_unica_compilato,person('importo_punto_422_certificazione_unica',period),np.array(0))


class RP30_contributi_versati_per_familiari_a_carico_non_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Indicare l’importo dei contributi per Contributi versati per carichi familiari che il sostituto d’imposta non ha dedotto dall’imponibile, relativi al punto 421 della certificazione Unica. Rigo RP30 col.2"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            # controllo se almeno un campo è compilato
            lista_campi_da_controllare = ['RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto','RP28_contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto','RP27_contributi_deducibilita_ordinaria_non_dedotti_dal_sostituto',
            'RP29_contributi_per_fondi_in_squilibrio_finanziario_dedotti_dal_sostituto','RP28_contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto','RP30_contributi_versati_per_familiari_a_carico_dedotti_dal_sostituto',
            'RP29_contributi_per_fondi_in_squilibrio_finanziario_non_dedotti_dal_sostituto',
            'RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_dedotti_dal_sostituto','RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_quota_TFR','RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_non_dedotti_dal_sostituto']
            # conto campi compilati
            almeno_un_campo_compilato = False
            for campo in lista_campi_da_controllare:
                almeno_un_campo_compilato = where(almeno_un_campo_compilato,almeno_un_campo_compilato,not_(person.get_holder(campo).get_array(period) is None))

            importo_punto_423_certificazione_unica = person('importo_punto_423_certificazione_unica',period)
            importo_limite_deducibilita = parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_importo_deducibile_contributi_versati_familiari_carico - person('RP30_contributi_versati_per_familiari_a_carico_dedotti_dal_sostituto',period)
            importo_limite_deducibilita = where(importo_limite_deducibilita>0,importo_limite_deducibilita,np.array(0))
            importo = min_(importo_punto_423_certificazione_unica,importo_limite_deducibilita)
            punto_421_certificazione_unica_compilato = not_(person('importo_punto_421_certificazione_unica',period)==0)
            return where(almeno_un_campo_compilato * punto_421_certificazione_unica_compilato,importo, np.array(0))
