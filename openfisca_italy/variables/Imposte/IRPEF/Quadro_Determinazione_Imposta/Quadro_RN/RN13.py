# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np

class RN13_detrazioni_per_oneri_detraibili_annuali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN13 totale - Detrazioni per oneri detraibili totali."
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return round_((person('RN13_detrazioni_per_oneri_detraibili_19_annuali',period) + person('RN13_detrazioni_per_oneri_detraibili_26_annuali',period)),2)


class RN13_detrazioni_per_oneri_detraibili_19_annuali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN13 col.1 - Detrazioni per oneri detraibili al 19%"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return round_((0.19*person('oneri_detraibili_al_19',period)),2)

class RN13_detrazioni_per_oneri_detraibili_26_annuali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN13 col.2 - Detrazioni per oneri detraibili al 26%"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return round_((0.26*person('oneri_detraibili_al_26',period)),2)
