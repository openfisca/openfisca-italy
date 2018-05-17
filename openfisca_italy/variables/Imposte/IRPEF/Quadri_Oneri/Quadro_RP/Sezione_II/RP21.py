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
