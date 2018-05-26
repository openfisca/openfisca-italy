# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from numpy import datetime64


class comune_di_nascita(Variable):
    value_type = str
    entity = Persona
    label = u"Comune di nascita della Persona"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Istanze/Richiesta+TS_CF/Verifica+codice+fiscale/?page=schedeistanze"


class provincia_del_comune_di_nascita(Variable):
    value_type = str
    entity = Persona
    label = u"Provincia del comune di nascita della Persona"
    definition_period = ETERNITY  # This variable cannot change over time.
    reference = u"http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Istanze/Richiesta+TS_CF/Verifica+codice+fiscale/?page=schedeistanze"
