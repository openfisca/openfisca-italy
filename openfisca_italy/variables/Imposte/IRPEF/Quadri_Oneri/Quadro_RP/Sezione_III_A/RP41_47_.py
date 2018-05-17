# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = u"Indicare l’anno in cui sono state sostenute le spese per interventi di recupero del patrimonio edilizio e misure antisismiche"


class TipiSpesaSostenutaPerRecuperoPatrimonioEdilizioInterventiAntisismici(Enum):
    nessun_codice = u"Non è stata sostenuta nessuna spesa per interventi di recupero del patrimonio edilizio e misure antisismiche "
    #...

class codice_fiscale_relativo_a_Rigo_RP41_RP47(Variable):
        value_type = str
        entity = Persona
        definition_period = YEAR
        label = u"Col.3 Indicare il codice fiscale relativo a spese per interventi di recupero del patrimonio edilizio e misure antisismiche"

# TODO: definire tutte le colonne della sezione III A, non definite al momento per ragioni di utilità
