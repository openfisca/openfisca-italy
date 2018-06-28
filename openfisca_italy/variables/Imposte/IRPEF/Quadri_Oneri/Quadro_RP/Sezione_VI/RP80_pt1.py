# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
#import numpy
import numpy as np


class RP80_codice_fiscale_relativo_a_investimenti_startup(Variable):
        value_type = str
        entity = Persona
        definition_period = YEAR
        label = u"RP80 Col.1 Indicare il codice fiscale della startup in cui si è deciso di investire"


class RP80_TipiInvestimentiStartup(Enum):
    nessun_codice_inserito=u'Non sono stati fatti investimenti in startup'
    codice_uno = u'Investimento diretto'
    codice_due = u'Investimento indiretto mediante un organismo di investimento collettivo del risparmio'
    codice_tre = u'Investimento indiretto è stato effettuato mediante una società di capitali che investe prevalentemente in start-up innovative'
    codice_quattro = u'I contribuenti che partecipano a società in nome collettivo o in accomandita semplice '
    codice_cinque= u'I contribuenti che partecipano a società di persone per il tramite di società che abbiano optato per la trasparenza fiscale ai sensi dell art. 116'


class RP80_tipi_investimenti_startup(Variable):
    value_type = Enum
    possible_values = RP80_TipiInvestimentiStartup
    default_value = RP80_TipiInvestimentiStartup.nessun_codice_inserito  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = u"RP80 col.2 Residui detrazioni e crediti d'imposta e deduzioni per startup del 2017 (Rigo RN47 col. 2 del modello REDDITI 2017)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class RP80_diritto_a_compilare_colonna_codice_e_ammontare_detrazione_investimenti_startup(Variable):
     value_type = bool
     entity = Persona
     definition_period = YEAR
     label = "La persona ha diritto a compilare la colonna 4 e 5 del Rigo RP80 se non ha indicato codice quattro o codice cinque nei tipi di investimenti in startup "
     reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

     def formula(person,period,parameter):
        tipo_investimento = person('RP80_tipi_investimenti_startup',period)
        non_deve_compilare_colonna_4_5 = (tipo_investimento == RP80_TipiInvestimentiStartup.nessun_codice_inserito) + (tipo_investimento == RP80_TipiInvestimentiStartup.codice_quattro) + (tipo_investimento == RP80_TipiInvestimentiStartup.codice_cinque)
        return where (non_deve_compilare_colonna_4_5, False, True)


class RP80_ammontare_investimento_startup(Variable):
     value_type = float
     entity = Persona
     definition_period = YEAR
     label = "Rigo RP80 col.3 Ammontare dell'importo detraibile di investimenti in startup che non può essere comunque superiore a 1000000 di euro (regolato nel calcolo delle detrazioni)"
     reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class RP80_TipiInvestimentiStartupPerPercentualeDetrazioni(Enum):
    nessun_codice_inserito = u'Non sono stati fatti investimenti in startup'
    codice_uno = u'Investimento è stato effettuato in start-up innovativa'
    codice_due = u'Investimento è stato effettuato in PMI innovativa di cui all’art. 4, comma 9, del decreto-legge 24 gennaio 2015, n. 3'


class RP80_tipi_investimenti_startup_per_percentuale_detrazioni(Variable):
    value_type = Enum
    possible_values = RP80_TipiInvestimentiStartupPerPercentualeDetrazioni
    default_value = RP80_TipiInvestimentiStartupPerPercentualeDetrazioni.nessun_codice_inserito  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = u"RP80 col.4 -  Indicare il codice che identifica il tipo di investimento per determinare la percentuale di detrazione"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


# Detrazioni investimenti startup


class RP80_ammontare_importo_detraibile_ricevuto_per_trasparenza_investimenti_startup(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP80 possibile colonna 6 - Importo che esiste solamente se persona ha effettuato un tipo di investimento con codice 4 o 5"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class RP80_ammontare_detrazioni_investimenti_startup(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = u"RP80 Col. 5 - Importo che esiste solamente se persona non ha effettuato un tipo di investimento con codice 4 o 5"
        reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

        def formula(person,period,parameters):
            diritto_a_compilare_colonna_codice_e_ammontare_detrazione = person('RP80_diritto_a_compilare_colonna_codice_e_ammontare_detrazione_investimenti_startup',period)
            ammontare_detrazioni = round_((person('RP80_ammontare_investimento_startup',period) * 0.30),2)
            return where(diritto_a_compilare_colonna_codice_e_ammontare_detrazione,ammontare_detrazioni,round_(person('RP80_ammontare_importo_detraibile_ricevuto_per_trasparenza_investimenti_startup',period),2))


class RP80_totale_detrazioni_per_investimenti_startup(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP80 Col.6 - Detrazione per investimenti in startup indicati nel quadro VI del Quadro RP (Detrazioni investimenti startup)"
    def formula(person,period,parameters):
        return person('RP80_ammontare_detrazioni_investimenti_startup',period)
