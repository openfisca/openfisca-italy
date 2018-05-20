# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class RP44TipiSpesaSostenutaPerRecuperoPatrimonioEdilizioInterventiAntisismici(Enum):
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


class RP44TipiInterventiParticolariPerRecuperoPatrimonioEdilizioInterventiAntisismici(Enum):
    nessun_codice = u"Non è stata sostenuta nessuna spesa per interventi particolari di recupero del patrimonio edilizio e misure antisismiche "
    codice_uno = u"Nel caso in cui le spese relative ad un singolo intervento siano state sostenute in più anni. Per calcolare il limite massimo di spesa detraibile occorre tenere conto delle spese sostenute negli anni precedenti"
    codice_quattro = u"-nel caso di spese sostenute per l’acquisto o assegnazione di immobili che fanno parte di edifici ristrutturati. La detrazione spetta su un importo pari al 25 per cento del prezzo di vendita o di assegnazione dell’immobile"


class RP44TipiCodiceEreditarietaInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici(Enum):
    nessun_codice = u"Non è stato indicato come il soggetto abbia ricevuto l'immobile "
    codice_quattro = u"Nel caso in cui il contribuente, nell’anno 2017 ha ereditato, acquistato o ricevuto in donazione l’immobile da un soggetto che aveva ripartito la spesa, sostenuta in anni precedenti, in 10 rate."


class RP44NumeriRateInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici(Enum):
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


class RP44_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR # tra il 2008 e il 2017
    label = u"RP44 Col.1 - Indicare l’anno in cui sono state sostenute le spese per interventi di recupero del patrimonio edilizio e misure antisismiche"


class RP44_codice_2012_2013_2017_antisismico(Variable):
    value_type = Enum
    possible_values = RP44TipiSpesaSostenutaPerRecuperoPatrimonioEdilizioInterventiAntisismici
    default_value = RP44TipiSpesaSostenutaPerRecuperoPatrimonioEdilizioInterventiAntisismici.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = u"RP44 Col.2 - Indicare codice della spesa"


class RP44_codice_fiscale(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP44 Col.3 - Indicare il codice fiscale relativo a spese per interventi di recupero del patrimonio edilizio e misure antisismiche nel caso di lavori a condomini."


class RP44_interventi_particolari(Variable):
    value_type = Enum
    possible_values = RP44TipiInterventiParticolariPerRecuperoPatrimonioEdilizioInterventiAntisismici
    default_value = RP44TipiInterventiParticolariPerRecuperoPatrimonioEdilizioInterventiAntisismici.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = u"RP44 Col.4 - Indicare codice intervento particolare"


class RP44_acquisto_ereditarieta_donazione(Variable):
    value_type = Enum
    possible_values = RP44TipiCodiceEreditarietaInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici
    default_value = RP44TipiCodiceEreditarietaInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = u"RP44 Col.5 - Indicare codice acquisto eraditarietà donazione"


class RP44_Anno_rata(Variable):
    value_type = Enum
    possible_values = RP44NumeriRateInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici
    default_value = RP44NumeriRateInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = u"RP44 Col.8 - indicare il numero della rata che il contribuente utilizza per il 2017. Per le spese sostenute nel 2017 va obbligatoriamente indicato il numero ‘1’"


class RP44_importo_spesa(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP44 Col.9 -indicare l’intero importo delle spese sostenute nell’anno riportato in colonna 1"


class RP44_importo_rata(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP44 Col.10 -indicare l’importo di ciascuna rata delle spese sostenute. Tale importo si ottiene dividendo l’ammontare di colonna 9 (spesa sostenuta nei limiti sopra indicati), per dieci"

    def formula(person,period,parameters):
         return person('RP44_importo_spesa',period)/10.0


class RP44_numero_ordine(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP44 Col.11 -Nella presente colonna 11 va indicato un numero progressivo per identificare l’immobile oggetto degli interventi di ristrutturazione. Riportare lo stesso numero anche nella colonna 1 della seguente sezione III-B."
