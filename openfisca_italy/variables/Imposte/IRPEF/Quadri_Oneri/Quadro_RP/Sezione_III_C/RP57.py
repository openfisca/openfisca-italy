# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class spesa_arredo_immobili_ristrutturati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spesa arredo immobili ristrutturati (Rigo RP57 col.2-5)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class importo_rata_spesa_arredo_immobili_ristrutturati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Importo rata arredo immobili ristrutturati (Rigo RP57 col.3-6)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('spesa_arredo_immobili_ristrutturati',period) / 10.0

class numero_rata_spesa_arredo_immobili_ristrutturati(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = "Numero rata arredo immobili ristrutturati (Rigo RP57 col.1-4)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source
