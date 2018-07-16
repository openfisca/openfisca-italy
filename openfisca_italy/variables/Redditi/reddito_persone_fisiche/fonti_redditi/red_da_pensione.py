# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np
# to avoid python runtime warning
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


# This variable is a pure input: it doesn't have a formula
class reddito_pensioni_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da pensioni annuale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        reddito_totale_da_pensioni = person('reddito_totale_da_pensioni',period)
        giorni_in_cui_si_e_percepita_la_pensione = person('giorni_in_cui_si_e_percepita_la_pensione',period)
        non_ci_sono_giorni_in_cui_si_e_percepita_la_pensione = where(giorni_in_cui_si_e_percepita_la_pensione == 0, True, False)
        return where (non_ci_sono_giorni_in_cui_si_e_percepita_la_pensione, np.array(0), np.array(round_(reddito_totale_da_pensioni * (giorni_in_cui_si_e_percepita_la_pensione/365.00),2)) )


# This variable is a pure input: it doesn't have a formula
class reddito_totale_da_pensioni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da pensioni percepite in un anno (questa variabile indica il totale del reddito percepito da pensioni ma non quello annuale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        return person('reddito_pensione_normale',period) + person('reddito_pensione_residente_campione_italia',period) + person('reddito_pensione_favore_dei_superstiti_corrisposte_agli_orfani',period)

# This variable is a pure input: it doesn't have a formula
class giorni_in_cui_si_e_percepita_la_pensione(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Giorni in cui la persona ha percepito reddito da pensioni (da 0 a 365)"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source
