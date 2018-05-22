# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_II_common import *
import numpy as np


class RP28_hanno_diritto_a_maggior_limite_di_deducibilita(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "RP28 La persona ha diritto a un maggior limite di deducibilità"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source


class RP28_contributi_versati_nei_primi_5_anni_per_maggior_limite_deducibilita(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "RP28 Contributi versati nei primi 5 anni"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source


class contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "RP28  col.1 - Indicare l’importo dei contributi per lavoratori prima occupazione che il sostituto d’imposta ha dedotto dall’imponibile, relativi al punto 411 della certificazione Unica codice3."
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            importo_punto_412_certificazione_unica = person('importo_punto_412_certificazione_unica',period)
            importo_punto_417_certificazione_unica = person('importo_punto_417_certificazione_unica',period)
            importo = importo_punto_412_certificazione_unica + importo_punto_417_certificazione_unica
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_tre
            return where (codice_campo_411_valido, importo ,0)


class contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "RP28 col.2 - Indicare l’importo dei contributi per lavoratori prima occupazione che il sostituto d’imposta non ha dedotto dall’imponibile, relativi al punto 411 della certificazione Unica codice3."
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
                # vedere se uno dei righi tra RP27 e RP31 e' stato compilato
                importo_punto_413_certificazione_unica = person('importo_punto_413_certificazione_unica',period)
                limite_deducibilita = parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_importo_deducibile_contributi_versati_lavoratori_prima_occupazione #limite di deducibilità normale
                # eventuale maggiorazione del limite di deduciblità
                eventuale_aumento_limite_deducibilita_maggiorato = (25822.85 - person('RP28_contributi_versati_nei_primi_5_anni_per_maggior_limite_deducibilita',period))
                eventuale_aumento_limite_deducibilita_maggiorato = where(eventuale_aumento_limite_deducibilita_maggiorato<2582,eventuale_aumento_limite_deducibilita_maggiorato,2582)
                limite_deducibilita = round((where(person('RP28_hanno_diritto_a_maggior_limite_di_deducibilita',period),(eventuale_aumento_limite_deducibilita_maggiorato + limite_deducibilita) ,limite_deducibilita)),2)
                operazione_limite_deducibilita = limite_deducibilita - person('contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto',period)
                operazione_limite_deducibilita = where(operazione_limite_deducibilita>0,operazione_limite_deducibilita,np.array(0))
                importo = round_(min_(importo_punto_413_certificazione_unica,operazione_limite_deducibilita),2)
                codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_tre
                return where (codice_campo_411_valido, importo ,0)


class RP_28_importo_deducibile_contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Rigo RP28 Col.2 sottoposto al limite di deducibilità da utilizzare per il calcolo degli oneri deducibili"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source
        def formula(person,period,parameters):
            limite_deducibilita = parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_importo_deducibile_contributi_versati_lavoratori_prima_occupazione #limite di deducibilità normale
            # eventuale maggiorazione del limite di deduciblità
            eventuale_aumento_limite_deducibilita_maggiorato = (25822.85 - person('RP28_contributi_versati_nei_primi_5_anni_per_maggior_limite_deducibilita',period))
            eventuale_aumento_limite_deducibilita_maggiorato = where(eventuale_aumento_limite_deducibilita_maggiorato<2582,eventuale_aumento_limite_deducibilita_maggiorato,2582)
            limite_deducibilita = round((where(person('RP28_hanno_diritto_a_maggior_limite_di_deducibilita',period),(eventuale_aumento_limite_deducibilita_maggiorato + limite_deducibilita) ,limite_deducibilita)),2)
            capienza_RP28 = limite_deducibilita - person('RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto',period) - person('contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto',period) - person('contributi_per_fondi_in_squilibrio_finanziario_dedotti_dal_sostituto',period) - person('contributi_versati_per_familiari_a_carico_dedotti_dal_sostituto',period) - person('contributi_fondo_pensione_negoziale_dipendenti_pubblici_dedotti_dal_sostituto',period)
            capienza_RP28 = where(capienza_RP28<0, 0, capienza_RP28)
            RP28_col2 = person('contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto',period)
            return where(RP28_col2<=capienza_RP28,RP28_col2,capienza_RP28)
