# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from numpy import datetime64

class numero_di_telefono_fisso(Variable):
    value_type = float
    entity = Persona
    label = u"Numero di telefono fisso della Persona"
    definition_period = YEAR  # This variable cannot change over time.
    reference = u"http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Istanze/Richiesta+TS_CF/Verifica+codice+fiscale/?page=schedeistanze"


class numero_di_telefono_cellulare(Variable):
    value_type = float
    entity = Persona
    label = u"Numero di telefono cellulare della Persona"
    definition_period = YEAR  # This variable cannot change over time.
    reference = u"http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Istanze/Richiesta+TS_CF/Verifica+codice+fiscale/?page=schedeistanze"


class indirizzo_di_posta_elettronica(Variable):
    value_type = float
    entity = Persona
    label = u"Indirizzo di posta elettronica della Persona"
    definition_period = YEAR  # This variable cannot change over time.
    reference = u"http://www.agenziaentrate.gov.it/wps/content/Nsilib/Nsi/Schede/Istanze/Richiesta+TS_CF/Verifica+codice+fiscale/?page=schedeistanze"
