# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpt
import numpy as np
# TODO: Inserire reddito complessivo da quello già creato

class reddito_di_riferimento_per_agevolazioni_fiscali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito di riferimento per agevolazioni fiscali Rigo RN1 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class credito_per_fondi_comuni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Credito per fondi comuni Rigo RN1 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class perdite_compensabili_con_crediti_per_fondi_comuni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Perdite compensabili con crediti per fondi comuni Rigo RN1 col.3"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class reddito_minimo_da_partecipazione_in_societa_non_operative(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito minimo da partecipazione in società non operative Rigo RN1 col.4"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

class reddito_complessivo(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito complessivo  Rigo RN1 col.5"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person, period, parameters):
        tipi_reddito = ['reddito_lavoro_dipendente_e_assimilati_annuale','reddito_di_capitali_annuale',
        'reddito_fondiari_annuale','reddito_diversi_annuale','redditi_da_attivita_sportive_dilettantistiche']
        # TO DO Check if incomes are taxable or not
        totale_reddito_complessivo = round_(sum(person(reddito, period) for reddito in tipi_reddito),2) # get first two decimale
        return np.array(totale_reddito_complessivo) #return converting in np.array becaues tests accept only this type


# Il reddito per detrazione non fa parte del Rigo RN1: reddito complessivo ma viene utilizzato per il calcolo delle detrazioni, per cui lo inserisco in questo file
class reddito_per_detrazioni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito per detrazioni"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        # if importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore negative consider 0
        importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore = where (person('importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period)<0,0, person('importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period))
        return person('reddito_complessivo',period) - person('deduzione_abitazione_principale_annuale',period) + importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore
