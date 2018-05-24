# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
import numpy as np


class RP34_codice_fiscale_societa_startup_in_cui_si_e_investito(Variable):
    value_type = str
    entity = Persona
    label = u"Rigo RP34 col.1 - Codice Fiscale Startup in cui si è investito"
    definition_period = YEAR
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=68"  # Always use the most official source


class RP34_quota_di_conferimento_in_start_up_eccedente_il_RN1_reddito_complessivo(Variable):
    value_type = float
    entity = Persona
    label = u"Rigo RP34 col.2 - Quota di conferimento in start up eccedente il reddito complessivo"
    definition_period = YEAR
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=68"  # Always use the most official source


class RP34_totale_importo_RPF_2018(Variable):
    value_type = float
    entity = Persona
    label = u"Rigo RP34 col.3 -  Indicare la somma degli importi indicati nelle colonne 2 di tutti i moduli compilati se è stato compilato più di un modulo"
    definition_period = YEAR
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=68"  # Always use the most official source


class RP34_importo_residuo_RPF_2017(Variable):
    value_type = float
    entity = Persona
    label = u"Rigo RP34 col.4 -  Indicare l’importo della deduzione non fruita relativa all’anno 2016, rilevabile dal modello REDDITI 2017 al rigo RN47 col.33 al netto delle eventuali eccedenze riportate al rigo RL32, col. 3 del modello REDDITI 2018"
    definition_period = YEAR
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=68"  # Always use the most official source


class RP34_importo_residuo_RPF_2016(Variable):
    value_type = float
    entity = Persona
    label = u"Rigo RP34 col.5 - Indicare l’importo della deduzione non fruita relativa all’anno 2015, rilevabile dal modello REDDITI 2017 al rigo , RN47 col.32"
    definition_period = YEAR
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=68"  # Always use the most official source


class RP34_importo_residuo_RPF_2015(Variable):
    value_type = float
    entity = Persona
    label = u"Rigo RP34 col.6 -  Indicare l’importo della deduzione non fruita relativa all’anno 2014, rilevabile dal modello REDDITI 2017 al rigo RN47 col.31"
    definition_period = YEAR
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=68"  # Always use the most official source
