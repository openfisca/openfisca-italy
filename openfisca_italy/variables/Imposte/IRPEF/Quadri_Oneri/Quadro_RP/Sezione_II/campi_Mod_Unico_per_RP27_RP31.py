# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_II_common import *

class codice_inserito_campo_411_modello_unico(Variable):
    value_type = Enum
    possible_values = TipiCodiciCampo411ModelloUnico
    definition_period = YEAR
    default_value = TipiCodiciCampo411ModelloUnico.nessun_codice
    entity = Persona
    label = u"Codice inserito nel campo 411 del modello unico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Normativa+e+Prassi/Provvedimenti/2018/Gennaio+2018+Provvedimenti/Provvedimento+15012018+CU+2018/CU_modOrd_2018.pdf#page=5"


class importo_punto_421_certificazione_unica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Punto 421 della Certificazione Unica 2017 "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source


class importo_punto_422_certificazione_unica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Punto 421 della Certificazione Unica 2017 "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source


class importo_punto_423_certificazione_unica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Punto 423 della Certificazione Unica 2017 "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source


class importo_punto_414_certificazione_unica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Punto 414 della Certificazione Unica 2017 "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

class importo_punto_413_certificazione_unica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Punto 413 della Certificazione Unica 2017 "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source


class importo_punto_412_certificazione_unica(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Punto 412 della Certificazione Unica"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source


class importo_punto_417_certificazione_unica(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Punto 417 della Certificazione Unica"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source


class importo_punto_440_certificazione_unica(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Punto 440 della Certificazione Unica"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source
