# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import common
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_III_A_common import *


class RP47_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR # tra il 2008 e il 2017
    label = u"RP47 Col.1 - Indicare l’anno in cui sono state sostenute le spese per interventi di recupero del patrimonio edilizio e misure antisismiche"


class RP47_codice_2012_2013_2017_antisismico(Variable):
    value_type = Enum
    possible_values = TipiSpesaSostenutaPerRecuperoPatrimonioEdilizioInterventiAntisismici
    default_value = TipiSpesaSostenutaPerRecuperoPatrimonioEdilizioInterventiAntisismici.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = u"RP47 Col.2 - Indicare codice della spesa"


class RP47_codice_fiscale(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP47 Col.3 - Indicare il codice fiscale relativo a spese per interventi di recupero del patrimonio edilizio e misure antisismiche nel caso di lavori a condomini."


class RP47_interventi_particolari(Variable):
    value_type = Enum
    possible_values = TipiInterventiParticolariPerRecuperoPatrimonioEdilizioInterventiAntisismici
    default_value = TipiInterventiParticolariPerRecuperoPatrimonioEdilizioInterventiAntisismici.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = u"RP47 Col.4 - Indicare codice intervento particolare"


class RP47_acquisto_ereditarieta_donazione(Variable):
    value_type = Enum
    possible_values = TipiCodiceEreditarietaInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici
    default_value = TipiCodiceEreditarietaInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = u"RP47 Col.5 - Indicare codice acquisto eraditarietà donazione"


class RP47_Anno_rata(Variable):
    value_type = Enum
    possible_values = NumeriRateInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici
    default_value = NumeriRateInterventiDonazioniPerRecuperoPatrimonioEdilizioInterventiAntisismici.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = u"RP47 Col.8 - indicare il numero della rata che il contribuente utilizza per il 2017. Per le spese sostenute nel 2017 va obbligatoriamente indicato il numero ‘1’"


class RP47_importo_spesa(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP47 Col.9 -indicare l’intero importo delle spese sostenute nell’anno riportato in colonna 1"


class RP47_importo_rata(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP47 Col.10 -indicare l’importo di ciascuna rata delle spese sostenute. Tale importo si ottiene dividendo l’ammontare di colonna 9 (spesa sostenuta nei limiti sopra indicati), per dieci"

    def formula(person,period,parameters):
         return person('RP47_importo_spesa',period)/10.0


class RP47_numero_ordine(Variable):
    value_type = str
    entity = Persona
    definition_period = YEAR
    label = u"RP47 Col.11 -Nella presente colonna 11 va indicato un numero progressivo per identificare l’immobile oggetto degli interventi di ristrutturazione. Riportare lo stesso numero anche nella colonna 1 della seguente sezione III-B."
