# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class TipologiaDetrazioneInquiliniAlloggiAdibitiAdAbitazionePrincipaleRigoRP71(Enum):
    nessun_codice = u"Il rigo non è stato compilato"
    codice_uno = u"Detrazione per gli inquilini di alloggi adibiti ad abitazione principale"
    codice_due = u"Detrazione per gli inquilini di alloggi adibiti ad abitazione principale con contratti a regime convenzionale"
    codice_tre = u"Detrazione per canoni di locazione relativi a contratti di locazione per abitazione principale per i giovani di età compresa tra i 20 ed i 30 anni, con reddito complessivo non superiore ad euro 15.493,71"

class tipologia_di_detrazione_inquilini_alloggi_adibiti_abitazione_principale_rigo_rp71(Variable):
    value_type = Enum
    possible_values = TipologiaDetrazioneInquiliniAlloggiAdibitiAdAbitazionePrincipaleRigoRP71
    default_value = TipologiaDetrazioneInquiliniAlloggiAdibitiAdAbitazionePrincipaleRigoRP71.nessun_codice
    entity = Persona
    definition_period = YEAR
    label = "Tipologia di detrazione inserita Rigo RP71 col.1"

class numero_giorni_in_cui_immobile_e_stato_adibito_ad_abitazione_principale(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = "Giorni dell’anno in cui l’immobile è stato adibito ad abitazione principale"

class percentuale_di_spettanza_relativa_a_inquilini_alloggi_adibiti_abitazione_principale(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = "Percentuale di spettanza relativa a inquilini di alloggi adibiti ad abitazione principale che va dallo 0 al 100%"
