# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


# Rigo RP14
class spese_per_canoni_di_leasing(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese per canoni di leasing(Rigo RP14)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

class data_stipula_leasing_relativa_a_spese_per_canoni_di_leasing(Variable):
    value_type = date
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Data stipula leasing(Rigo RP14 col.1)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

# TODO: vedere se c'è un limite di anni per cui si possa usufruire della detrazione
class numero_anno_per_cui_il_soggetto_usufruisce_della_detrazione_per_spese_canoni_di_leasing(Variable):
    value_type = date
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Numero anno in cui si usufruisce della detrazione (Rigo RP14 col.2), se il contratto e' stato stipulato nel 2017 allora questa variabile assume valore 1"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class eta_persona_stipula_del_contratto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Eta' del soggetto quando ha stipulato il contratto di leasing"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

# TODO:  L’importo dei canoni di leasing non può superare: il limite di 8.000 euro annui se alla data di stipula del contratto di leasing il contribuente aveva meno di 35 anni; il limite di 4.000 euro annui se a tale data il contribuente aveva un età uguale o superiore a 35 anni.
class importo_canone_leasing_relativo_a_spese_per_canoni_di_leasing(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Importo canone di leasing(Rigo RP14 col.3)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


# TODO: Il prezzo di riscatto non può superare: il limite di 20.000 euro se alla data di stipula del contratto di leasing il contribuente aveva meno di 35 anni; il limite di 10.000 euro se a tale data il contribuente aveva un età uguale o superiore a 35 anni.
class prezzo_di_riscatto_relativo_a_spese_per_canoni_di_leasing(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Eta' del soggetto quando ha stipulato il contratto di leasing"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
