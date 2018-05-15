# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
#import numpy
import numpy as np


class TipiInvestimentiStartup(Enum):
    nessun_codice_inserito=u'Non sono stati fatti investimenti in startup'
    codice_uno = u'Investimento diretto'
    codice_due = u'Investimento indiretto mediante un organismo di investimento collettivo del risparmio'
    codice_tre = u'Investimento indiretto è stato effettuato mediante una società di capitali che investe prevalentemente in start-up innovative'
    codice_quattro = u'I contribuenti che partecipano a società in nome collettivo o in accomandita semplice '
    codice_cinque= u'I contribuenti che partecipano a società di persone per il tramite di società che abbiano optato per la trasparenza fiscale ai sensi dell art. 116'


class tipi_investimenti_startup(Variable):
    value_type = Enum
    possible_values = TipiInvestimentiStartup
    default_value = TipiInvestimentiStartup.nessun_codice_inserito  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni e crediti d'imposta e deduzioni per startup del 2017 (Rigo RN47 col. 2 del modello REDDITI 2017)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class diritto_a_compilare_colonna_codice_e_ammontare_detrazione_investimenti_startup(Variable):
     value_type = bool
     entity = Persona
     definition_period = YEAR
     label = "La persona ha diritto a compilare la colonna 4 e 5 del Rigo RP80 se non ha indicato codice quattro o codice cinque nei tipi di investimenti in startup "
     reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

     def formula(person,period,parameter):
        tipo_investimento = person('tipi_investimenti_startup',period)
        non_deve_compilare_colonna_4_5 = (tipo_investimento == TipiInvestimentiStartup.nessun_codice_inserito) + (tipo_investimento == TipiInvestimentiStartup.codice_quattro) + (tipo_investimento == TipiInvestimentiStartup.codice_cinque)
        return where (non_deve_compilare_colonna_4_5, False, True)


class ammontare_investimento_detraibile_investimenti_startup(Variable):
     value_type = float
     entity = Persona
     definition_period = YEAR
     label = "Ammontare dell'importo detraibile di investimenti in startup (Rigo RP80 col.4 ) che non può essere comunque superiore a 1000000 di euro (regolato nel calcolo delle detrazioni)"
     reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class TipiInvestimentiStartupPerPercentualeDetrazioni(Enum):
    nessun_codice_inserito = u'Non sono stati fatti investimenti in startup'
    codice_uno = u'Investimento è stato effettuato in start-up innovativa'
    codice_due = u'Investimento è stato effettuato in PMI innovativa di cui all’art. 4, comma 9, del decreto-legge 24 gennaio 2015, n. 3'


class tipi_investimenti_startup_per_percentuale_detrazioni(Variable):
    value_type = Enum
    possible_values = TipiInvestimentiStartupPerPercentualeDetrazioni
    default_value = TipiInvestimentiStartupPerPercentualeDetrazioni.nessun_codice_inserito  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = u"Residui detrazioni e crediti d'imposta e deduzioni per startup del 2017 (Rigo RN47 col. 2 del modello REDDITI 2017)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source
