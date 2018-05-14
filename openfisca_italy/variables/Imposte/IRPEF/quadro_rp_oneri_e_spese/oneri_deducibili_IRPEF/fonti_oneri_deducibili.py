# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class contributi_previdenziali_assistenziali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Contributi previdenziali e assistenziali"
    reference = "http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Comunicazioni/Dati+relativi+ai+contributi+previdenziali+%28dal+2015%29/InfoGen+DatiContributiPrevidenzialidal2015/?page=schedecomunicazioni"  # Always use the most official source

class assegni_periodo_coniuge(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Assegni periodici corrisposti al coniuge"
    reference = "https://www.ecnews.it/le-deducibilita-dellassegno-periodico-corrisposto-al-coniuge/"  # Always use the most official source

class contributi_addetti_servizi_domestici_e_familiari(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Contributi per addetti ai servizi domestici e familiari"
    reference = "https://www.fiscoetasse.com/rassegna-stampa/23384-deducibilit-dei-contributi-per-gli-addetti-ai-servizi-domestici-e-familiari-730.html"  # Always use the most official source

class erogazioni_istituzioni_religiose(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Erogazioni liberali a favore di istituzioni religiose"
    reference = "http://www.fiscooggi.it/normativa-e-prassi/articolo/erogazioni-istituzioni-religiosededucibili-se-quietanzate-dallente"  # Always use the most official source

class spese_mediche_e_assistenza_disabili(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese mediche e di assistenza per disabili"
    reference = "http://www.fiscooggi.it/normativa-e-prassi/articolo/erogazioni-istituzioni-religiosededucibili-se-quietanzate-dallente"  # Always use the most official source

class contributi_previdenza_complementare(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Contributi per la previdenza complementare"
    reference = "http://www.fiscooggi.it/normativa-e-prassi/articolo/erogazioni-istituzioni-religiosededucibili-se-quietanzate-dallente"  # Always use the most official source
