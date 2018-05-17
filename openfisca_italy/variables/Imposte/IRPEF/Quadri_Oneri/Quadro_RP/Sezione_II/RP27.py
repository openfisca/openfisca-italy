# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class contributi_deducibilita_ordinaria_dedotti_dal_sostituto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Indicare l’importo dei contributi che il sostituto d’imposta ha dedotto dall’imponibile, di cui al punto 412 della Certificazione Unica. Rigo RP27 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

class contributi_deducibilita_ordinaria_non_dedotti_dal_sostituto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Indicare l’importo dei contributi che il sostituto d’imposta non ha dedotto dall’imponibile, di cui al punto 412 della Certificazione Unica. Rigo RP27 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

    def formula(person,period,parameters):
        # se è stato compilato uno solo dei righi da RP27 a RP31, indicare il minore importo tra i risultati delle seguenti operazioni:
        # 1) calcolare il totale degli oneri di previdenza complementare per i quali si chiede la deduzione in dichiarazione: nto 413 della Certificazione Unica 2017 + somme versate alle forme pensionistiche individuali 2) calcolare la differenza per verificare il limite di deducibilità ordinaria: 5.164,57 – l’importo di colonna 1
        pass
