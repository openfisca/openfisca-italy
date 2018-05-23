# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class TipiSpesaSostenutaPerRecuperoPatrimonioEdilizioInterventiAntisismici(Enum):
    nessun_codice = u"Non è stata sostenuta nessuna spesa per interventi di recupero del patrimonio edilizio e misure antisismiche "
    codice_due = u"Spese sostenute dal 1° gennaio al 25 giugno 2012 (detrazione del 36%)"
    codice_tre = u"Spese sostenute dal 26 giugno al 31 dicembre 2012 (detrazione del 50%)"
    codice_quattro = u"Spese sostenute dal 4 agosto 2013 al 31 dicembre 2016 per interventi relativi all’adozione di misure antisismiche su edifici ricadenti nelle zone sismiche ad alta pericolosità, riferite a costruzioni adibite ad abitazione principale o ad attività produttive"
    codice_cinque = u"Spese sostenute nel 2017 per interventi relativi all’adozione di misure antisismiche su edifici ricadenti nelle zone sismiche ad alta pericolosità (detrazione del 50%) e nella zona sismica 3"
    codice_sei = u"Spese sostenute nel 2017 per interventi relativi all’adozione di misure antisismiche su edifici ricadenti nelle zone sismiche ad alta pericolosità e nella zona sismica 3, dalla cui adozione derivi una riduzione del rischio sismico che determini il passaggio ad una classe di rischio inferiore (detrazione del 70%)"
    codice_sette = u"Spese sostenute nel 2017 per interventi relativi all’adozione di misure antisismiche su edifici ricadenti nelle zone sismiche ad alta pericolosità e nella zona sismica 3, dalla cui adozione derivi una riduzione del rischio sismico che determini il passaggio a due classi di rischio inferiore (detrazione dell’80%)"
    codice_otto = u" Spese sostenute nel 2017 per interventi relativi all’adozione di misure antisismiche sulle parti comuni di edifici condominiali ricadenti nelle zone sismiche ad alta pericolosità e nella zona sismica 3, dalla cui adozione derivi una riduzione del rischio sismico che determini il passaggio ad una classe di rischio inferiore (detrazione del 75%)"
    codice_nove = u"Spese sostenute nel 2017 per interventi relativi all’adozione di misure antisismiche sulle parti comuni di edifici condominiali ricadenti nelle zone sismiche ad alta pericolosità e nella zona sismica 3, riferite a costruzioni adibite ad abitazione o ad attività produttive, dalla cui adozione derivi una riduzione del rischio sismico che determini il passaggio a due classi di rischio inferiore (detrazione dell’85%)"
    codice_dieci = u"Spese sostenute nel 2017 per l’acquisto di unità immobiliari facenti parte di edifici ricostruitiricadenti nelle zone classificate a rischio sismico 1 ai sensi dell’ordinanza del Presidente del Consiglio dei ministri n. 3519 del 28 aprile 2006, pubblicata nella Gazzetta Ufficiale n. 108 dell’11 maggio 2006, la cui ricostruzione ha comportato il passaggio ad una classe di rischio inferiore (detrazione del 75%)"
    codice_undici =  u"Spese sostenute dal 1° gennaio 2017 al 31 dicembre 2017 per l’acquisto di unità immobiliari facenti parte di edifici ricostruiti ricadenti nelle zone classificate a rischio sismico 1 ai sensi dell’ordinanza del Presidente del Consiglio dei ministri n. 3519 del 28 aprile 2006, pubblicata nella Gazzetta Ufficiale n. 108 dell’11 maggio 2006, la cui ricostruzione ha comportato il passaggio a due classi di rischio inferiore (detrazione dell’85%)"


class TipiInterventiParticolariPerRecuperoPatrimonioEdilizioInterventiAntisismici(Enum):
    nessun_codice = u"Non è stata sostenuta nessuna spesa per interventi particolari di recupero del patrimonio edilizio e misure antisismiche "
    codice_uno = u"Nel caso in cui le spese relative ad un singolo intervento siano state sostenute in più anni. Per calcolare il limite massimo di spesa detraibile occorre tenere conto delle spese sostenute negli anni precedenti"
    codice_quattro = u"-nel caso di spese sostenute per l’acquisto o assegnazione di immobili che fanno parte di edifici ristrutturati. La detrazione spetta su un importo pari al 25 per cento del prezzo di vendita o di assegnazione dell’immobile"


class TipiCodiceEreditarietaInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici(Enum):
    nessun_codice = u"Non è stato indicato come il soggetto abbia ricevuto l'immobile "
    codice_quattro = u"Nel caso in cui il contribuente, nell’anno 2017 ha ereditato, acquistato o ricevuto in donazione l’immobile da un soggetto che aveva ripartito la spesa, sostenuta in anni precedenti, in 10 rate."


class NumeriRateInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici(Enum):
        nessun_codice = u"Non è stato inserito il numero della rata"
        codice_uno = u"Primo anno che il contribuente utilizza della rata"
        codice_due = u"Secondo anno che il contribuente utilizza della rata"
        codice_tre = u"Terzo anno che il contribuente utilizza della rata"
        codice_quattro = u"Quarto anno che il contribuente utilizza della rata"
        codice_cinque = u"Quinto anno che il contribuente utilizza della rata"
        codice_sei = u"Sesto anno che il contribuente utilizza della rata"
        codice_sette = u"Settimo anno che il contribuente utilizza della rata"
        codice_otto = u"Ottavo anno che il contribuente utilizza della rata"
        codice_nove = u"Nono anno che il contribuente utilizza della rata"
        codice_dieci = u"Decimo anno che il contribuente utilizza della rata"
