# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class RP26_altri_oneri_e_spese_deducibili(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Altri oneri e spese deducibili Rigo Rp26 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=64"  # Always use the most official source

class RP26_TipiAltriOneriESpeseDeducibili(Enum):
    nessun_codice = u"Nessun codice è stato inserito, il campo non compilato"
    codice_sei = u"Contributi versati ai fondi integrativi al Servizio sanitario nazionale"
    codice_sette = u" i contributi, le donazioni e le oblazioni erogate alle organizzazioni non governative (ONG) riconosciute idonee, che operano nel campo della cooperazione con i Paesi in via di sviluppo"
    codice_otto = u" le erogazioni liberali in denaro o in natura a favore di organizzazioni non lucrative di utilità sociale, di associazioni di promozione sociale e di alcune fondazioni e associazioni riconosciute."
    codice_nove = u"Le erogazioni liberali in denaro a favore di enti universitari, di ricerca pubblica e di quelli vigilati nonché degli enti parco regionali e nazionali"
    codice_dodici = u"Per le erogazioni liberali, le donazioni e gli altri atti a titolo gratuito a favore di trust o fondi speciali."
    codice_tredici = u"per i contributi versati direttamente dai pensionati, anche per i familiari non a carico, a casse di assistenza sanitaria aventi esclusivamente fini assistenziali"
    codice_ventuno = u"gli altri oneri deducibili diversi da quelli contraddistinti dai precedenti codici"
