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
class reddito_lavoro_dipendente_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period 
    label = "Reddito da lavoro dipendente al netto delle detrazioni del datore di lavoro"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        return person('reddito_comune_campione_italia',period) + person('reddito_lavoro_frontaliere',period) + person('reddito_lavoro_dipendente_normale',period) + person('reddito_lavori_socialmente_utili',period)


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
        return where (non_ci_sono_giorni_in_cui_si_e_percepita_la_pensione, np.array(0), np.array(reddito_totale_da_pensioni * (365.00/giorni_in_cui_si_e_percepita_la_pensione)))


# This variable is a pure input: it doesn't have a formula
class reddito_totale_da_pensioni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period 
    label = "Reddito da pensioni percepite in un anno (questa variabile indica il totale del reddito percepito da pensioni ma non quello annuale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


# This variable is a pure input: it doesn't have a formula
class giorni_in_cui_si_e_percepita_la_pensione(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period 
    label = "Giorni in cui la persona ha percepito reddito da pensioni (da 0 a 365)"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


# This variable is a pure input: it doesn't have a formula
class reddito_lavoro_dipendente_e_assimilati_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period 
    label = "Reddito da lavoro dipendente e assimilati"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        reddito_lavoro_dipendente = person('reddito_lavoro_dipendente_annuale',period)
        reddito_pensioni = person('reddito_pensioni_annuale',period)
        return reddito_lavoro_dipendente + reddito_pensioni


# This variable is a pure input: it doesn't have a formula
class reddito_lavoro_autonomo_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito da lavoro autonomo al netto delle perdite"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source


# This variable is a pure input: it doesn't have a formula
class reddito_catastale_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito catastale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


# This variable is a pure input: it doesn't have a formula
class reddito_affitto_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito da affitti"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source    


# The sum of reddito_terreni_annuali and reddito_fabbricati_annuale
class reddito_fabbricati_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito da fabbricati"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        reddito_catastale_annuale = person ('reddito_catastale_annuale',period)
        reddito_affitto_annuale = person('reddito_affitto_annuale',period)
        return reddito_catastale_annuale + reddito_affitto_annuale

# This variable is a pure input: it doesn't have a formula
class reddito_agrario_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito catastale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class reddito_dominicale_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito dominicale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


# The sum of reddito_catastale_annuali and reddito_dominicale_annuale
class reddito_terreni_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da terreni"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        reddito_agrario_annuale = person ('reddito_agrario_annuale',period)
        reddito_dominicale_annuale = person('reddito_dominicale_annuale',period)
        return reddito_agrario_annuale + reddito_dominicale_annuale

# The sum of reddito_terreni_annuali and reddito_fabbricati_annuale
class reddito_fondiari_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito fondiari"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"
    def formula(person,period,parameters):
        reddito_terreni_annuale = person('reddito_terreni_annuale',period)
        reddito_fabbricati_annuale = person('reddito_fabbricati_annuale',period)
        return reddito_terreni_annuale + reddito_fabbricati_annuale


# This variable is a pure input: it doesn't have a formula
class reddito_di_impresa_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito d'imprese"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source


# This variable is a pure input: it doesn't have a formula
class reddito_di_capitali_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito di capitali"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source


# This variable is a pure input: it doesn't have a formula
class reddito_diversi_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Reddito diversi"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source    

# This variable is a pure input: it doesn't have a formula
class redditi_da_attivita_sportive_dilettantistiche(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Redditi da attività sportive dilettantistiche"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source    
