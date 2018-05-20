# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpt
import numpy as np

#Dovrei prendere un codice relativo alla Sezione III A nelle colonne 11. Il problema e' che nella sezione III a ci sono 7 righi e qui solo due. Quindi c'è un problema.
class RP51_numero_ordine_immobile(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP51 Col.1 -Nella presente colonna 1 va indicato un numero progressivo per identificare l’immobile oggetto degli interventi di ristrutturazione. "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"

class RP51_condominio(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = u"RP51 Col.2 - la casella deve essere barrata nel caso di interventi effettuati su parti comuni condominiali. I singoli condomini, barrando questa casella, dichiarano che la spesa riportata nella sezione III-A del quadro RP si riferisce ad interventi effettuati su parti comuni condominiali, pertanto non devono essere compilate le successive colonne dei righi RP51 e RP52, relative ai dati catastali dell’immobile, in quanto tali dati saranno indicati dall’amministratore di condominio nel quadro AC della propria dichiarazione dei redditi."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"

class RP51_codice_comune(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP51 Col.3 -Nella presente colonna 3 indicare il codice catastale del comune dove è situata l’unità immobiliare."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP51TipiTerreniUrbani(Enum):
    nessun_codice = "Nessun codice inserito"
    codice_T = "Immobile è censito nel catasto terreni"
    codice_U = "Immobile è censito nel catasto edilizio urbano"


class RP51_terreni_Urbani(Variable):
    value_type = Enum
    entity = Persona
    possible_values = RP51TipiTerreniUrbani
    default_value = RP51TipiTerreniUrbani.nessun_codice
    definition_period = YEAR
    label = u"RP51 Col.4 -Nella presente colonna 4 indicare: ‘T’ se l’immobile è censito nel catasto terreni; ‘U’ se l’immobile è censito nel catasto edilizio urbano."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP51_sezione_urbana_comune_catastale(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP51 Col.5 -Nella presente colonna 5 riportare le lettere o i numeri indicati nel documento catastale, se presenti. Per gli immobili siti nelle zone in cui vige il sistema tavolare indicare il codice “Comune catastale"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP51_foglio(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP51 Col.6 -Nella presente colonna 6 riportare il numero di foglio indicato nel documento catastale."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP51_particella(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP51 Col.7 -Nella presente colonna 7 riportare il numero di particella, indicato nel documento catastale, che può essere composto da due parti, rispettivamente di cinque e quattro cifre, separato da una barra spaziatrice. Se la particella è composta da una sola serie di cifre, quest’ultima va riportata nella parte a sinistra della barra spaziatrice."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"


class RP51_subalterno(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP51 Col.8 -Nella presente colonna 8 riportare, se presente, il numero di subalterno indicato nel documento catastale."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=74"
