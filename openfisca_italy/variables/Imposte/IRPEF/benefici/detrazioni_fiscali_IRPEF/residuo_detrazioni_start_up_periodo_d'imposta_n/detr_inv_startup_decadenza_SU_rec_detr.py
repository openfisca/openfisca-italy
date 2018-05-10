# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class ammontare_importo_detraibile_ricevuto_per_trasparenza(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo che esiste solamente se persona ha effettuato un tipo di investimento con codice 4 o 5 (Se esiste va scritto nel Rigo RP80 col. 6)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class ammontare_detrazioni(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = u"Importo che esiste solamente se persona non ha effettuato un tipo di investimento con codice 4 o 5 (Rigo RP80 col. 5)"
        reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

        def formula(person,period,parameters):
            diritto_a_compilare_colonna_codice_e_ammontare_detrazione = person('diritto_a_compilare_colonna_codice_e_ammontare_detrazione',period)
            ammontare_detrazioni = round_((person('ammontare_investimento_detraibile',period) * 0.30),2)
            return where(diritto_a_compilare_colonna_codice_e_ammontare_detrazione,ammontare_detrazioni,0)
