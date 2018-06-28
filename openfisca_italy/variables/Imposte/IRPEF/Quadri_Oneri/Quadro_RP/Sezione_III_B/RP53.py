# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpt
import numpy as np
#Se i lavori sono effettuati dal conduttore (o comodatario), devono essere indicati, oltre ai dati catastali identificativi dell’immobile (righi
#RP51 e RP52) anche gli estremi di registrazione del contratto di locazione o di comodato (colonne da 3 a 6 del rigo RP53) ovvero
#colonna 7 se in possesso del codice identificativo del contratto).

class RP53_numero_ordine_immobile(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP53 Col.1 -Nella presente colonna 1 va indicato un numero progressivo per identificare l’immobile oggetto degli interventi di ristrutturazione. "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP53_condominio(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = u"RP53 Col.2 - la casella deve essere barrata nel caso di interventi effettuati su parti comuni condominiali. I singoli condomini, barrando questa casella, dichiarano che la spesa riportata nella sezione III-A del quadro RP si riferisce ad interventi effettuati su parti comuni condominiali, pertanto non devono essere compilate le successive colonne dei righi RP51 e RP52, relative ai dati catastali dell’immobile, in quanto tali dati saranno indicati dall’amministratore di condominio nel quadro AC della propria dichiarazione dei redditi."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


# Conduttore - Estremi di registrazione del contratto di locazione o comodato
class RP53_data_registrazione_contratto(Variable):
    value_type = date
    default_value = date(1970,1,1)
    entity = Persona
    definition_period = YEAR
    label = u"RP53 col.3 - Indicare la data di registrazione del contratto."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP53CodiceRelativoModalitaRegistrazione(Enum):
    nessun_codice = "Non è stato inserito alcun codice, quindi il rigo non dovrebbe essere compilato"
    codice_1T = "Registrazione telematica tramite pubblico ufficiale"
    codice_3 = "Registrazione del contratto presso un ufficio dell’Agenzia delle Entrate"
    codice_3P = "Registrazione telematica tramite Siria e Iris"
    codice_3T = "Registrazione telematica tramite altre applicazioni "
    codice_3A = "Codice di serie in uso in passato presso gli uffici"
    codice_3B = "Codice di serie in uso in passato presso gli uffici"


class RP53_serie(Variable):
    value_type = Enum
    possible_values = RP53CodiceRelativoModalitaRegistrazione
    default_value = RP53CodiceRelativoModalitaRegistrazione.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = "RP53 col.4 - Indicare il codice relativo alla modalità di registrazione"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP53_numero_sottonumero(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP53 Col.5 -Nella presente colonna 5 indicare il numero e l’eventuale sottonumero di registrazione del contratto"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP53_codice_ufficio_agenzia_entrate(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP53 Col.6 - Nella presente colonna 6 indicare il codice identificativo dell’Ufficio dell’Agenzia delle Entrate presso il quale è stato registrato il contratto."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP53_codice_identificativo_contratto(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP53 Col.7 - Nella presente colonna 7 indicare il codice identificativo del contratto composto da 17 caratteri e reperibile nella copia del modello di richiesta di registrazione del contratto restituito dall’ufficio o, per i contratti registrati per via telematica, nella ricevuta di registrazione. Se sono state compilate le colonne da 3 a 6 questa colonna non va compilata."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


# Domanda di accatastamento

class RP53_data_domanda_accastamento(Variable):
    value_type = date
    default_value = date(1970,1,1)
    entity = Persona
    definition_period = YEAR
    label = u"RP53 Col.8 - Nella presente colonna 8 indicare la data di presentazione della domanda di accatastamento"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP53_numero_domanda_accatastamento(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP53 Col.9 - Nella presente colonna 8 indicare il numero della domanda di accatastamento"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP53_sigla_provincia_domanda_accatastamento(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP53 Col.10 - Nella presente colonna 10  indicare la sigla della Provincia in cui è situato l’Ufficio dell’Agenzia delle Entrate presso il quale è stata presentata la domanda."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"
