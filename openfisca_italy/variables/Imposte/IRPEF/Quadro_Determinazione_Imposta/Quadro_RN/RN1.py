# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

class RN1_reddito_di_riferimento_per_agevolazioni_fiscali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN1 col.1 - Reddito di riferimento per agevolazioni fiscali"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class RN1_credito_per_fondi_comuni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RN1 col.2 - Credito per fondi comuni Rigo"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class RN1_perdite_compensabili_con_crediti_per_fondi_comuni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN1 col.3 - Perdite compensabili con crediti per fondi comuni."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class RN1_reddito_minimo_da_partecipazione_in_societa_non_operative(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = " Rigo RN1 col.4 - Reddito minimo da partecipazione in società non operative."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=83"  # Always use the most official source

class RN1_reddito_complessivo(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN1 col.5 - Reddito complessivo"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=83"  # Always use the most official source

    def formula(person, period, parameters):
        tipi_reddito = ['reddito_lavoro_dipendente_e_assimilati_annuale','reddito_di_capitali_annuale',
        'reddito_fondiari_annuale','reddito_diversi_annuale','redditi_da_attivita_sportive_dilettantistiche']
        totale_RN1_reddito_complessivo = round_(sum(person(reddito, period) for reddito in tipi_reddito),2)
        totale_RN1_reddito_complessivo = where(person('compilato_RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore_utilizzato',period),totale_RN1_reddito_complessivo - person('RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore_utilizzato',period),totale_RN1_reddito_complessivo)  # eventuale diminuzione se compilato RS37 col.16
        RN1_col_4_compilato = not_(person('RN1_reddito_minimo_da_partecipazione_in_societa_non_operative',period) <= 0)
        return where(RN1_col_4_compilato, min_(totale_RN1_reddito_complessivo,RN1_col_4_compilato),totale_RN1_reddito_complessivo)

# il campo relativo al quadro RS 37 serve per sapere se devo effettuare una sottrazione nel calcolo del reddito complessivo

class compilato_RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore_utilizzato(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La persona ha compilato il rigo RS37 colonna 16 riguardo importo del rendimento nozionale di spettanza dell imprenditore utilizzato"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
    def formula(person,period,parameters):
        return not_(person('RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore_utilizzato',period) == 0)


# Il reddito per detrazione non fa parte del Rigo RN1: reddito complessivo ma viene utilizzato per il calcolo delle detrazioni, per cui lo inserisco in questo file
class reddito_per_detrazioni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito per detrazioni"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=86"  # Always use the most official source

    def formula(person,period,parameters):
        # if RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore negative consider 0
        RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore = where (person('RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period)<0,0, person('RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period))
        return person('RN1_reddito_complessivo',period) - person('RN2_deduzione_abitazione_principale',period) + RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore
