# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


class irpef_non_dovuta_per_soli_terreni_e_fabbricati (Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "Condizione vera se il pensionato ha un reddito da sola pensione minore della soglia ed eventualmente reddito da terreni minore della soglia e non ha compilato rigo RN1 col. 2"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"
    def formula(person,period,parameters):
        # check if lands and buildings income is under the threshold
        reddito_fondiario_sotto_la_soglia = person('reddito_fondiari_annuale',period) < parameters(period).imposte.IRPEF.redditi_non_tassabili.reddito_solo_terreni_e_fabbricati and person('reddito_fondiari_annuale',period)>0
        # check if the person has only field and lands and buildings income
        solo_redditi_da_terreni_e_fabbricati = person('solo_redditi_da_terreni_e_fabbricati',period)
        # check that user hasn't compiled the section credito_per_fondi_comuni_compilato in the income declaration
        credito_per_fondi_comuni_compilato_non_compilato = not person('credito_per_fondi_comuni_compilato',period)
        # check that all other incomes are 0
        tutti_altri_redditi_sono_zero = person('solo_redditi_da_terreni_e_fabbricati',period)
        return where((reddito_fondiario_sotto_la_soglia and solo_redditi_da_terreni_e_fabbricati and credito_per_fondi_comuni_compilato_non_compilato),True,False)


class solo_redditi_da_terreni_e_fabbricati(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "Condizione vera se persona ha compilato rigo RN1 col. 2 nella dichiarazione dei redditi"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"

    def formula(person,period,parameters):
        # check that all other incomes are 0
        altri_redditi = ['reddito_lavoro_dipendente_annuale','reddito_assimilato_a_lavoro_dipendente_ed_altri_redditi_annuale','reddito_di_capitali_annuale',
       'reddito_diversi_annuale','redditi_da_attivita_sportive_dilettantistiche']
        tutti_altri_redditi_sono_zero = [person(reddito, period)==0 for reddito in altri_redditi]
        # check that all values in tutti_altri_redditi_sono_zero are true and set in the same variables
        tutti_altri_redditi_sono_zero = all(tutti_altri_redditi_sono_zero)
        return where(tutti_altri_redditi_sono_zero,True,False)
