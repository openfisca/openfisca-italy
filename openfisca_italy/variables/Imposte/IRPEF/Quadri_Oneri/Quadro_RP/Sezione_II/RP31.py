# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_II_common import *

import numpy as np

class RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Rigo RP31 col.1 - Indicare l’importo dei contributi per Contributi Fondo pensione negoziale dipendenti pubblici che il sostituto d’imposta ha dedotto dall’imponibile, relativi al punto 411 codice 4. della certificazione Unica."
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_quattro
            return where (codice_campo_411_valido, person('importo_punto_412_certificazione_unica',period) , np.array(0))


class RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_quota_TFR(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Rigo RP31 col.2 - Indicare l’importo dela quota TFR per Contributi Fondo pensione negoziale dipendenti pubblici, relativi al punto 411 codice 4. della certificazione Unica."
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

        def formula(person,period,parameters):
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_quattro
            return where (codice_campo_411_valido, person('importo_punto_414_certificazione_unica',period) , np.array(0))

# Column 3 section
# La classe RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_non_dedotti_dal_sostituto segue un prospetto nelle appendici,essendo complessa sara' composta da più variabili
class RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_non_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = " Rigo RP31 col.3 - Indicare l’importo dei contributi per Contributi Fondo pensione negoziale dipendenti pubblici che il sostituto d’imposta non ha dedotto dall’imponibile, relativi al punto 411 codice 4. della certificazione Unica."
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source

        def formula(person,period,parameters):
            # controllo se almeno un campo è compilato
            lista_campi_da_controllare = ['RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto','RP28_contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto','RP27_contributi_deducibilita_ordinaria_non_dedotti_dal_sostituto',
            'RP29_contributi_per_fondi_in_squilibrio_finanziario_dedotti_dal_sostituto','RP28_contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto','RP30_contributi_versati_per_familiari_a_carico_dedotti_dal_sostituto',
            'RP29_contributi_per_fondi_in_squilibrio_finanziario_non_dedotti_dal_sostituto',
            'RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_dedotti_dal_sostituto','RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_quota_TFR','RP30_contributi_versati_per_familiari_a_carico_non_dedotti_dal_sostituto']
            # conto campi compilati
            almeno_un_campo_compilato = False
            for campo in lista_campi_da_controllare:
                almeno_un_campo_compilato = where(almeno_un_campo_compilato,almeno_un_campo_compilato,not_(person.get_holder(campo).get_array(period) is None))
            # controllare che sia stato compilato uno dei vari righi
            codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_quattro
            return where (codice_campo_411_valido, person('casella_11_prospetto_compilazione_Rigo_RP31',period) , np.array(0))

 #prospetto
class casella_1_prospetto_compilazione_Rigo_RP31(Variable):
     value_type = float
     entity = Persona
     definition_period = YEAR
     label = "Casella 1 prospetto compilazione rigo rp31"
     reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source

     def formula(person,period,parameters):
        return person('RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_dedotti_dal_sostituto',period)


class casella_2_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella 2 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source

        def formula(person,period,parameters):
            return person('RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_quota_TFR',period)


class casella_3_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella 3 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source

        def formula(person,period,parameters):
            # caso 1
            casella_411_certificazione_unica_compilata = not_(person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.nessun_codice) #nessun codice
            importo_punto_413_certificazione_unica = person('importo_punto_413_certificazione_unica',period)
            # caso 2
            nella_casella_411_certificazione_unica_compilata_presente_codice_uno = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_uno
            codice_inserito_campo_421_modello_unico = not_(person('importo_punto_421_certificazione_unica',period) == 0)
            importo_punto_423_certificazione_unica = person('importo_punto_423_certificazione_unica',period)
            return select([nella_casella_411_certificazione_unica_compilata_presente_codice_uno*codice_inserito_campo_421_modello_unico,
                            casella_411_certificazione_unica_compilata],
                            [importo_punto_413_certificazione_unica-importo_punto_423_certificazione_unica,
                            importo_punto_413_certificazione_unica])


class casella_4_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella  4 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source
        def formula(person,period,parameters):
            return person('reddito_complessivo',period)


class casella_5_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella 5 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source
        def formula(person,period,parameters):
            return person('reddito_lavoro_dipendente_annuale',period)


class casella_6_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella 6 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source

        def formula(person,period,parameters):
            minimo_colonna_2_colonna_5 = min_(person('casella_5_prospetto_compilazione_Rigo_RP31',period),(2*person('casella_2_prospetto_compilazione_Rigo_RP31',period)))
            importo = minimo_colonna_2_colonna_5 - person('casella_1_prospetto_compilazione_Rigo_RP31',period)
            return where(importo>0,importo,np.array(0))


class casella_7_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella 7 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source
        def formula(person,period,parameters):
            return person('casella_4_prospetto_compilazione_Rigo_RP31',period) - person('casella_5_prospetto_compilazione_Rigo_RP31',period)


class casella_8_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella 8 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source
        def formula(person,period,parameters):
            return person('casella_6_prospetto_compilazione_Rigo_RP31',period) + person('casella_7_prospetto_compilazione_Rigo_RP31',period)


class casella_9_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella 9 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source
        def formula(person,period,parameters):
            return parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_importo_deducibile_contributi_versati_fondi_pensione_negoziali_dip_pubblici - person('casella_1_prospetto_compilazione_Rigo_RP31',period)


class casella_10_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella 10 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source
        def formula(person,period,parameters):
            return (person('reddito_di_riferimento_per_agevolazioni_fiscali',period)*0.12) - person('casella_1_prospetto_compilazione_Rigo_RP31',period)


class casella_11_prospetto_compilazione_Rigo_RP31(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Casella 11 prospetto compilazione rigo rp31"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=120"  # Always use the most official source
        def formula(person,period,parameters):
            minimo = person('casella_3_prospetto_compilazione_Rigo_RP31',period) #prima casella da controllare
            caselle_da_controllare = ['casella_8_prospetto_compilazione_Rigo_RP31',
                                    'casella_9_prospetto_compilazione_Rigo_RP31','casella_10_prospetto_compilazione_Rigo_RP31']
            for caselle in caselle_da_controllare:
                minimo = where(minimo<person(caselle,period),minimo,person(caselle,period))
            return minimo
