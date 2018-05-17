# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


#Sezione spese


class iva_per_acquisto_abitazione_classe_energetica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "IVA per acquisto abitazione classe energetica A o B (Rigo RP59 col.2)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

#Sezione rate

class importo_rata_iva_per_acquisto_abitazione_classe_energetica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Importo rata IVA per acquisto abitazione classe energetica A o B (Rigo RP59 col.3)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('iva_per_acquisto_abitazione_classe_energetica',period) / 10.0


class numero_rata_iva_per_acquisto_abitazione_classe_energetica(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = "Numero rata importo iva per acquisto abitazione classe energetica (Rigo RP59 col.1)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source
