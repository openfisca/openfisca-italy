# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
import numpy as np

class RP64TipiInterventiFinalizzatiRisparmioEnergetico(Enum):
    nessun_codice = "Non è stato compilato nessun codice per il RIGO RP64 col.1"
    codice_uno = "Interventi di riqualificazione energetica di edifici esistenti"
    codice_due = "Interventi sull’involucro degli edifici esistenti"
    codice_tre = "Installazione di pannelli solari"
    codice_quattro = "Sostituzione di impianti di climatizzazione invernale"
    codice_cinque = "Acquisto e posa in opera di schermature solari"
    codice_sei = "Acquisto e posa in opera di impianti di climatizzazione invernale a biomasse"
    codice_sette = "Acquisto, installazione e messa in opera di dispositivi multimediali per controllo da remoto"
    codice_otto = "Interventi sull’involucro di parti comuni degli edifici condominiali esistenti"
    codice_nove = " Interventi di riqualificazione energetica di parti comuni degli edifici condominiali esistenti"

class RP64_tipo_intervento(Variable):
    value_type = Enum
    possible_values = RP64TipiInterventiFinalizzatiRisparmioEnergetico
    default_value = RP64TipiInterventiFinalizzatiRisparmioEnergetico.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = "RP64 Col.1 - Indicare il codice del tipo di intervento finalizzato al risparmio energetico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source

class RP64_anno_sostenimento_spese_risparmio_energetico(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    entity = Persona
    label = "RP64 Col.2 - Indicare il anno sostenimento spesa intervento finalizzaot al risparmio energetico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source


class RP64TipiPeriodo2013FinalizzatiRisparmioEnergetico(Enum):
    nessun_codice = "Non è stato compilato nessun codice per il RIGO RP64 col.3"
    codice_uno = "Spese sostenute dal 1° gennaio al 5 giugno 2013 (detrazione del 55%)"
    codice_due = "Spese sostenute dal 6 giugno al 31 dicembre 2013 (detrazione del 65%)"

class RP64_periodo_2013(Variable):
    value_type = Enum
    possible_values = RP64TipiPeriodo2013FinalizzatiRisparmioEnergetico
    default_value = RP64TipiPeriodo2013FinalizzatiRisparmioEnergetico.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = "RP64 Col.3 - Compilare questa colonna solo se le spese sono state sostenute nel 2013"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source


class RP64TipiCasiParticolariFinalizzatiRisparmioEnergetico(Enum):
    nessun_codice = "Non è stato compilato nessun codice per il RIGO RP64 col.3"
    codice_uno = "Nel caso di spese sostenute per lavori iniziati in anni precedenti e ancora in corso nel 2017"
    codice_due = "Nel caso in cui le spese sostenute in anni precedenti al 2017 riguardino un immobile ereditato, acquistato o ricevuto in donazione nell’anno 2017"
    codice_tre = "Se ricorrono contemporaneamente le condizioni di cui ai codici 1 e 2 (lavori che proseguono in più anni ed immobile ereditato, acquistato o ricevuto in donazione)"


class RP64_casi_particolari(Variable):
    value_type = Enum
    possible_values = RP64TipiCasiParticolariFinalizzatiRisparmioEnergetico
    default_value = RP64TipiCasiParticolariFinalizzatiRisparmioEnergetico.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = "RP64 Col.4 - Compilare questa colonna solo se ci si trova in una situazione riservata ai contribuenti che si trovano in una delle situazioni descritte."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source


class RP64_periodo_2008_rideterminazione_rate(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = "RP64 Col.5 -i contribuenti che dal 2009 al 2017 hanno acquistato o ereditato un immobile, oggetto di lavori nel corso dell’anno 2008, se hanno rideterminato o intendono rideterminare il numero di rate scelte da chi ha sostenuto la spesa indicano in questa colonna il numero delle rate in cui è stata inizialmente ripartita la detrazione."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source


class RP64_numero_rata(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = "RP64 Col.7 - indicare il numero della rata che il contribuente utilizza per il 2017. Ad esempio, indicare 3 per le spese sostenute nel 2015, 2 per le spese del 2016 e 1 per le spese del 2017."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source

class RP64RangeSpesaDate(Enum):
    nessun_codice = "Non e' stata inserita alcuna spesa"
    codice_uno = "spese sostenute fino al 5 giugno 2013 (55%)"
    codice_due = "spese sostenute dal 6 giugno 2013 al 31 dicembre 2017 (65%)"
    codice_tre = "Spese sostenute dal 1 gennaio al 31 dicembre 2017"

class RP64_Range_Spesa_Date(Variable):
    value_type = Enum
    possible_values = RP64RangeSpesaDate
    default_value = RP64RangeSpesaDate.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = "Campo che serve a capire il limite di spesa inseribile nei righi a seconda del tipo di spesa."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source

class RP64_limite_spesa_in_base_a_codice_da_1_a_4(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label= "Limite di spesa inseribile nel rigo RP64"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source
    def formula(person,period,parameters):
        codice_tipo_intervento = person('RP64_tipo_intervento',period)
        range_date_spesa = person('RP64_Range_Spesa_Date',period)
        # dove i codici sono diversi da 5 e 6
        P = parameters(period).imposte.IRPEF.QuadroRP.Sezione_IV.limite_spesa_codici_diversi_da_5_6_RP61_64[codice_tipo_intervento]
        return select([range_date_spesa == RP64RangeSpesaDate.nessun_codice,
        range_date_spesa == RP64RangeSpesaDate.codice_uno,
        range_date_spesa == RP64RangeSpesaDate.codice_due],
        [0, P.importo_spese_sostenute_fino_5_giugno_2013, P.importo_spese_sostenute_dal_6_giugno_2013_al_21_dicembre_2017,])


class RP64_limite_spesa_in_base_a_codice_5_6(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label= "Limite di spesa inseribile nel rigo RP64"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source
    def formula(person,period,parameters):
        codice_tipo_intervento = person('RP64_tipo_intervento',period)
        range_date_spesa = person('RP64_Range_Spesa_Date',period)
        # dove i codici sono diversi da 5 e 6
        P = parameters(period).imposte.IRPEF.QuadroRP.Sezione_IV.limite_spesa_codici_5_6_RP61_64[codice_tipo_intervento]
        return select([range_date_spesa == RP64RangeSpesaDate.nessun_codice,
        range_date_spesa == RP64RangeSpesaDate.codice_tre],
        [0, P.importo_spese_sostenute_dal_1_gennaio_al_31_dicembre_2017])


class RP64_spesa_totale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "RP64 Col.8 - indicare l’ammontare della spesa sostenuta entro i limiti sottodescritti in relazione alla tipologia dell’intervento che, ad eccezione delle spese indicate con il codice 7 "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source
    #TODO: Quando la funzionalità sara' implementata, mettere come limite massimo indicabile quello calcolato nelle variabili di questo file

class RP64_importo_rata(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "RP64 Col.9 - indicare l’importo di ciascuna rata delle spese sostenute. Tale importo si ottiene dividendo l’ammontare della spesa sostenuta (colonna 8), per 10"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=78"  # Always use the most official source
    def formula(person,period,parameters):
        rideterminazione_rata_compilato = not_(person('RP64_periodo_2008_rideterminazione_rate',period) == 0)
        rate_utilizzate = (8 - person('RP64_numero_rata',period)) * (person('RP64_spesa_totale',period)/person('RP64_periodo_2008_rideterminazione_rate',period))
        importo_rata_calcolato_con_rideterminazione =  (person('RP64_spesa_totale',period) - rate_utilizzate) / 10.0
        return where(rideterminazione_rata_compilato,importo_rata_calcolato_con_rideterminazione,person('RP64_spesa_totale',period) / 10.0)
