# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# TODO: definire il calcolo del vari crediti d'imposta in base ai valori del quadro CR ed LM una volta che questi saranno definiti


class RN24_totale_crediti_imposta_generano_requisiti(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Somma colonne Rigo RN24 quadro RN"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_credito_imposta = ['RN24_credito_imposta_riacquisto_della_prima_casa','RN24_credito_imposta_incremento_occupazione',
                    'RN24_credito_imposta_reintegro_anticipazioni_fondi_pensione','RN24_credito_imposta_mediazioni_per_la_conciliazione_di_controversie_civili_commerciali',
                    'RN24_credito_imposta_negoziazione_e_arbitrato']

        return round_(sum(person(tipo_credito,period)for tipo_credito in tipi_credito_imposta),2)


class RN24_credito_imposta_riacquisto_della_prima_casa(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN24 col.1 quadro RN: Credito d’imposta per il riacquisto della prima casa"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class RN24_credito_imposta_incremento_occupazione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN24 col.2 quadro RN: Credito d’imposta per l’incremento dell’occupazione"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class RN24_credito_imposta_reintegro_anticipazioni_fondi_pensione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN24 col.3 quadro RN: Credito d’imposta reintegro anticipazioni fondi pensione"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class RN24_credito_imposta_mediazioni_per_la_conciliazione_di_controversie_civili_commerciali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN24 col.4 quadro RN: Credito d’imposta mediazioni per la conciliazione di controversie civili e commerciali"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class RN24_credito_imposta_negoziazione_e_arbitrato(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN24 col.5 quadro RN: Credito d’imposta negoziazione e arbitrato"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source
