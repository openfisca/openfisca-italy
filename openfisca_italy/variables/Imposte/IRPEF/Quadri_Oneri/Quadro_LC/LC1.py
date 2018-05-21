# -*- coding: utf-8 -*-
# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
import numpy as np

class LC1_imposta_cedolare_secca(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.1 -  indicare l’ammontare dell’imposta sostitutiva dovuta indicato nella colonna 3 del rigo RB11 " # TODO: mettere importo col 3 RB11 quando RB sarà fatto
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_imposta_su_redditi_diversi(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.2 - indicare l’ammontare dell’imposta sostitutiva dovuta con aliquota pari al 21 per cento dell’importo indicato nella colonna 4 del rigo RL10 (Fascicolo 2) per tutti i moduli nel caso in cui sia barrata la casella 3 “cedolare secca” del medesimo rigo. " # TODO: mettere importo col 4 RL10 quando RL sarà fatto
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_totale_imposta_complessiva(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.3 - indicare la somma degli importi esposti nelle colonne 1 e 2 del presente rigo "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        return person('LC1_imposta_cedolare_secca',period) + person('LC1_imposta_su_redditi_diversi',period)


class LC1_ritenute_CU_locazioni_brevi(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.4 - indicare l’importo delle ritenute riportato nel quadro Certificazione Redditi – Locazioni brevi della Certificazione Unica 2018 al punto 15 e relative ai corrispondenti redditi di locazione indicati nel quadro RB e RL per il quale non è barrata la relativa casella “2018” del punto 4. Se in possesso di più quadri della Certificazione Redditi – Locazioni brevi della Certificazione Unica 2018 o se sono compilati più righi dello stesso quadro (punti 15, 115, 215, 315 e 415 per i quali non è barrata la relativa casella “2018”) indicare la somma delle ritenute" # TODO: mettere importi dei vari punti dei quadri RB ed RL quando saranno fatti
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_differenza(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.5 - indicare la differenza degli importi esposti nelle colonne 3 e 4 del presente rigo. Se la differenza LC1 colonna 3 – LC1 colonna 4 è negativo, il risultato in valore assoluto deve essere riportato nel rigo RN33 colonna 4"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        return person('LC1_totale_imposta_complessiva',period)- person('LC1_ritenute_CU_locazioni_brevi',period)


class LC1_eccedenza_dichiarata_precedentemente(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.6 - riportare l’eventuale credito di cedolare secca che risulta dalla dichiarazione relativa ai redditi 2016, indicato nella colonna 5 del rigo RX4 del Mod. Redditi PF 2017."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_eccedenza_compensata_modello_F24(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.7 - indicare l’importo dell’eccedenza di cedolare secca eventualmente compensata utilizzando il modello F24."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class input_acconti_versati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Parte di LC1 col.8 - indicare l’ammontare degli acconti della cedolare secca versati per l’anno 2017"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_acconti_versati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.8 - indicare l’ammontare degli acconti della cedolare secca versati per l’anno 2017 comprendendo anche l'importo di colonna 9"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        return person('input_acconti_versati',period) + person('LC1_acconti_sospesi',period)


class LC1_acconti_sospesi(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.9 - indicare l’importo degli acconti dovuti ma non ancora versati alla data di presentazione della dichiarazione in quanto si è goduto della sospensione dei termini sulla base di specifici provvedimenti emanati per eventi eccezionali."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_cedolare_secca_trattenuta_dal_sostituto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.10 - riportare l’importo trattenuto dal sostituto d’imposta, indicato nella colonna 7 del rigo 99 del modello 730-3/2018."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_cedolare_Secca_rimbosata_dal_sostituto_o_REDDITI_2018(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.11 - riportare l’importo rimborsato dal sostituto d’imposta, indicato nella colonna 5 del rigo 99 del modello 730-3/2018."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_credito_compensato_modello_F24(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.12 - a presente colonna deve essere compilata solo se nel quadro I del mod. 730/2018 avete chiesto di utilizzare il credito originato dalla liquidazione della dichiarazione 730 per il pagamento dell’IMU e di altre imposte e se nel mod. 730-3/2018 (prospetto di liquidazione), risulta compilata la colonna 4 del rigo 99 (ovvero col. 4 del rigo 119 per il coniuge). In tal caso riportare l’ammontare del credito utilizzato in compensazione con il mod. F24, entro la data di presentazione della presente dichiarazione, per il pagamento dell’IMU e di altre imposte."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_imposta_a_debito(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.13 - Tale importo va riportato nella colonna 1 del rigo RX4,vedere documentazione per calcolo."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source


class LC1_imposta_a_debito(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.13 - Tale importo va riportato nella colonna 1 del rigo RX4,vedere documentazione per calcolo."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        importo_colonna_5 = where(person('LC1_differenza',period)>0,person('LC1_differenza',period),0) #inclusa se positiva
        importo_colonna_6 = person('LC1_eccedenza_dichiarata_precedentemente',period)
        importo_colonna_7 = person('LC1_eccedenza_compensata_modello_F24',period)
        importo_colonna_8 = person('LC1_acconti_versati',period)
        importo_colonna_10 = person('LC1_cedolare_secca_trattenuta_dal_sostituto',period)
        importo_colonna_11 = person('LC1_cedolare_Secca_rimbosata_dal_sostituto_o_REDDITI_2018',period)
        importo_colonna_12 = person('LC1_credito_compensato_modello_F24',period)
        importo = importo_colonna_5 - importo_colonna_6 + importo_colonna_7 - importo_colonna_8 - importo_colonna_10 + importo_colonna_11 + importo_colonna_12
        return where(importo>0,importo, np.array(0))


class LC1_imposta_a_credito(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.14 - Tale importo va riportato anche nella colonna 2 del rigo RX4,vedere documentazione per calcolo."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        importo_colonna_5 = where(person('LC1_differenza',period)>0,person('LC1_differenza',period),0) #inclusa se positiva
        importo_colonna_6 = person('LC1_eccedenza_dichiarata_precedentemente',period)
        importo_colonna_7 = person('LC1_eccedenza_compensata_modello_F24',period)
        importo_colonna_8 = person('LC1_acconti_versati',period)
        importo_colonna_10 = person('LC1_cedolare_secca_trattenuta_dal_sostituto',period)
        importo_colonna_11 = person('LC1_cedolare_Secca_rimbosata_dal_sostituto_o_REDDITI_2018',period)
        importo_colonna_12 = person('LC1_credito_compensato_modello_F24',period)
        importo = importo_colonna_5 - importo_colonna_6 + importo_colonna_7 - importo_colonna_8 - importo_colonna_10 + importo_colonna_11 + importo_colonna_12
        print 'LC1_differenza',importo_colonna_5
        print 'LC1_eccedenza_dichiarata_precedentemente',importo_colonna_6
        print 'LC1_eccedenza_compensata_modello_F24',importo_colonna_7
        print 'LC1_acconti_versati',importo_colonna_8
        print 'LC1_cedolare_secca_trattenuta_dal_sostituto',importo_colonna_10
        print 'LC1_cedolare_Secca_rimbosata_dal_sostituto_o_REDDITI_2018',importo_colonna_11
        print 'LC1_credito_compensato_modello_F24',importo_colonna_12
        return where(importo<0,abs(importo), np.array(0))
