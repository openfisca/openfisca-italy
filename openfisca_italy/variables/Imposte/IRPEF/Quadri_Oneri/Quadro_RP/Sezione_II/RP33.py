# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
import numpy as np


class RP33_e_stato_chiesto_al_sostituto_di_effettuare_la_deduzione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label="Serve per conoscere l'importo da indicare in colonna 1 del rigo RP33"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source


class RP33_somme_restituite_anno(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label="Rigo RP33 col.1 - Importo delle somme restituite nel 2017 al soggetto erogatore o, nel caso in cui sia stato chiesto al sostituto di effettuare la deduzione, l’importo delle somme non dedotte indicate nel punto 440 della Certificazione Unica 2018."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source
    def formula(person,period,parameters):
        return where (person('RP33_e_stato_chiesto_al_sostituto_di_effettuare_la_deduzione',period),person('importo_punto_440_certificazione_unica',period),np.array(0))


class RP33_residuo_precedente_dichiarazione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label="Rigo RP33 col.2 -  indicare l’ammontare non dedotto nel periodo d’imposta precedente, riportato nel rigo RN47, colonna 36, del modello REDDITI 2017 oppure nel rigo 149 del prospetto di liquidazione Mod. 730-3/2017 (colonna 1 per il dichiarante, colonna 2 per il coniuge)."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source


class RP33_totale_restituzione_somme_al_soggetto_erogatore(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label="Rigo RP33 col.3 - Totale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source

    def formula(person,period,parameters):
        return person('RP33_somme_restituite_anno',period) + person('RP33_residuo_precedente_dichiarazione',period)
