# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


class soglia_reddito_non_tassabile_per_reddito_da_pensione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito non tassabile per reddito da sola pensione"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        eta = person('age',period.last_month) <= 70
        return where(eta,7500,8000)

class irpef_non_dovuta_pensionati_e_terreni (Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "Condizione vera se il pensionato ha un reddito da sola pensione minore della soglia ed eventualmente reddito da terreni minore della soglia e non ha compilato rigo RN1 col. 2"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"

    def formula(person,period,parameters):
        # check if the person has only retirement income under the threshold and fields income under the threshold
        reddito_da_pensione_sotto_la_soglia = (person('reddito_pensioni_annuale',period) < person('soglia_reddito_non_tassabile_per_reddito_da_pensione',period)) * (person('reddito_pensioni_annuale',period) > 0)
        reddito_da_terreni_sotto_la_soglia = (person('reddito_terreni_annuale',period) < parameters(period).imposte.IRPEF.redditi_non_tassabili.reddito_terreni) * (person('reddito_terreni_annuale',period) > 0)
        # check that user has compiled the section credito_per_fondi_comuni_compilato in the income declaration
        credito_per_fondi_comuni_compilato = person('credito_per_fondi_comuni_compilato',period)
        # person have only income from fields and retirement
        # check that all other incomes are 0
        print 'in irpef non dovuta ai pensionati: reddio pensionati sotto la soglia', reddito_da_pensione_sotto_la_soglia
        print 'in irpef non dovuta ai pensionati: reddito_da_terreni_sotto_la_soglia', reddito_da_terreni_sotto_la_soglia
        print 'in irpef non dovuta ai pensionati: credito per fondi comuni compilato', credito_per_fondi_comuni_compilato
        tutti_altri_redditi_sono_zero = person('solo_redditi_da_pensione_e_terreni',period)
        return where((reddito_da_pensione_sotto_la_soglia and reddito_da_terreni_sotto_la_soglia and tutti_altri_redditi_sono_zero and not_(credito_per_fondi_comuni_compilato)),True,False)

# TODO: aggiornare il parametro del credito per fondi comuni compilato quando verrà definito il rigo RN1
class credito_per_fondi_comuni_compilato (Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "Condizione vera se persona ha compilato rigo RN1 col. 2 nella dichiarazione dei redditi"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"


class solo_redditi_da_pensione_e_terreni(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "Condizione vera se la persona ha solo reddito da pensione e da terreni"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"

    def formula(person,period,parameters):
        # check that all other incomes are 0
        altri_redditi = ['reddito_lavoro_dipendente_annuale','reddito_assimilato_a_lavoro_dipendente_ed_altri_redditi_annuale','reddito_di_capitali_annuale','reddito_fabbricati_annuale','reddito_diversi_annuale','redditi_da_attivita_sportive_dilettantistiche']
        tutti_altri_redditi_sono_zero = [person(reddito, period)==0 for reddito in altri_redditi]
        # check that all values in tutti_altri_redditi_sono_zero are true and set in the same variables
        tutti_altri_redditi_sono_zero = all(tutti_altri_redditi_sono_zero)
        return where(tutti_altri_redditi_sono_zero,True,False)
