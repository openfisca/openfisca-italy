# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class totale_rate_spesa_arredo_immobili_ristrutturati_gc_iva_acquisto_abitazione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "TOTALE RATE per Spese arredo immobili ristrutturati, giovani coppie, IVA per acquisto abitazione classe energetica A o B (Rigo RP60)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_rate_spese_arredo_immobili = ['importo_rata_spesa_arredo_immobili_ristrutturati',
                                            'importo_rata_spesa_arredo_immobili_giovani_coppie',
                                            'importo_rata_iva_per_acquisto_abitazione_classe_energetica',]
        return round_(sum(person(tipo_rata, period) for tipo_rata in tipi_rate_spese_arredo_immobili),2)

#Sezione spese

class spesa_arredo_immobili_ristrutturati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spesa arredo immobili ristrutturati (Rigo RP57 col.2-5)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class spesa_arredo_immobili_giovani_coppie(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spesa arredo immobili giovani coppie  (Rigo RP58 col.2)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class iva_per_acquisto_abitazione_classe_energetica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "IVA per acquisto abitazione classe energetica A o B (Rigo RP59 col.2)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

#Sezione rate

class importo_rata_spesa_arredo_immobili_ristrutturati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Importo rata arredo immobili ristrutturati (Rigo RP57 col.3-6)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('spesa_arredo_immobili_ristrutturati',period) / 10.0

class importo_rata_spesa_arredo_immobili_giovani_coppie(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Importo rata arredo immobili giovani coppie (Rigo RP58 col.3)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('spesa_arredo_immobili_giovani_coppie',period) / 10.0

class importo_rata_iva_per_acquisto_abitazione_classe_energetica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Importo rata IVA per acquisto abitazione classe energetica A o B (Rigo RP59 col.3)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('iva_per_acquisto_abitazione_classe_energetica',period) / 10.0
