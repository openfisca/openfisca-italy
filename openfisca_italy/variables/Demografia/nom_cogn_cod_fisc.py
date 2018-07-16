# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from numpy import datetime64

class codice_fiscale(Variable):
    value_type = str
    entity = Persona
    label = u"Codice Fiscale Persona"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Istanze/Richiesta+TS_CF/Verifica+codice+fiscale/?page=schedeistanze"


class nome(Variable):
    value_type = str
    entity = Persona
    label = u"Nome della Persona"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Istanze/Richiesta+TS_CF/Verifica+codice+fiscale/?page=schedeistanze"


class cognome(Variable):
    value_type = str
    entity = Persona
    label = u"Cognome della Persona"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Istanze/Richiesta+TS_CF/Verifica+codice+fiscale/?page=schedeistanze"
