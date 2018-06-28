# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np
# to avoid python runtime warning
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Tipi di redditi percepibili

class reddito_comune_campione_italia(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito nel comune di Campione d'Italia"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class reddito_lavoro_frontaliere(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito frontaliero"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class reddito_lavori_socialmente_utili(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito lavori socialmente utile"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class reddito_lavoro_dipendente_normale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito lavoro dipendente"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


# Numero giorni di lavoro
class numero_giorni_lavoro_dipendente(Variable):
    value_type =  int
    entity = Persona
    definition_period = YEAR
    label = "Numero giorni in cui persona ha percepito reddito da lavoro dipendente"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class reddito_lavoro_dipendente_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da lavoro dipendente al netto delle detrazioni del datore di lavoro"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        return person('reddito_comune_campione_italia',period) + person('reddito_lavoro_frontaliere',period) + person('reddito_lavoro_dipendente_normale',period) + person('reddito_lavori_socialmente_utili',period)

class reddito_da_assegni_ex_coniuge(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da assegni ex coniuge"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source


# This variable is a pure input: it doesn't have a formula
class reddito_assimilato_a_lavoro_dipendente_ed_altri_redditi_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da lavoro dipendente e assimilati"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        reddito_lavoro_autonomo_annuale = person('reddito_lavoro_autonomo_annuale',period)
        reddito_da_attivita_commerciali_non_esercitate_abitualmente = person('reddito_da_attivita_commerciali_non_esercitate_abitualmente',period)
        reddito_da_attivita_lavoro_autonomo_non_esercitate_abitualmente = person('reddito_da_attivita_lavoro_autonomo_non_esercitate_abitualmente',period)
        reddito_da_attivita_assunzioni_fare_nonfare_permettere = person('reddito_da_attivita_assunzioni_fare_nonfare_permettere',period)
        reddito_di_impresa_annuale = person('reddito_di_impresa_annuale',period)
        reddito_da_assegni_ex_coniuge  = person('reddito_da_assegni_ex_coniuge',period)
        return reddito_lavoro_autonomo_annuale + reddito_da_attivita_commerciali_non_esercitate_abitualmente + reddito_da_attivita_lavoro_autonomo_non_esercitate_abitualmente + reddito_da_attivita_assunzioni_fare_nonfare_permettere + reddito_di_impresa_annuale


class reddito_lavoro_dipendente_e_assimilati_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da lavoro dipendente e assimilati"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        return person('reddito_assimilato_a_lavoro_dipendente_ed_altri_redditi_annuale',period) + person('reddito_lavoro_dipendente_annuale',period) + person('reddito_pensioni_annuale',period)


# This variable is a pure input: it doesn't have a formula
class reddito_lavoro_autonomo_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Reddito da lavoro autonomo al netto delle perdite"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class reddito_da_attivita_commerciali_non_esercitate_abitualmente(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Redditi derivanti da attività commerciali non esercitate abitualmente"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class reddito_da_attivita_lavoro_autonomo_non_esercitate_abitualmente(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Redditi derivanti da attività di lavoro autonomo non esercitate abitualmente"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source

# This variable is a pure input: it doesn't have a formula
class reddito_da_attivita_assunzioni_fare_nonfare_permettere(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Redditi derivanti da attività di assunzione di obblighi di fare,non fare, permettere"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Always use the most official source
