# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


class RP82_sostenute_spese_mantenimento_cane_guida(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RP82 Col.1 - Se il soggetto ha un cane guida da mantenere ha diritto a una detrazione fissa"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class RP82_detrazioni_per_mantenimento_cane_guida(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RP82 - Detrazioni speciali per mantenimento cane guida"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return where (person('RP82_sostenute_spese_mantenimento_cane_guida',period),parameters(period).imposte.IRPEF.QuadroRP.Sezione_VI.detrazione_forfettaria_spese_mantenimento_cani_guida,np.array(0))
