# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_VI.RP83 import RP83_TipiAltreDetrazioni
# Import numpy
import numpy as np

class RN17_totale_detrazione_oneri_Sez_VI_quadro_RP(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RN17 - Detrazione per oneri indicati nella Sezione VI del Quadro RP"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        tipo_altra_detrazione = person('RP83_tipo_altre_detrazioni',period)
        vero_valore_RP83_altre_detrazioni = where(tipo_altra_detrazione == 1, #RP83_TipiAltreDetrazioni.codice_due
                                                    where(person('RP83_altre_detrazioni',period) < (0.30 * person('RN5_irpef_lorda',period)) ,
                                                    person('RP83_altre_detrazioni',period), (0.30 * person('RN5_irpef_lorda',period)))
                                            ,person('RP83_altre_detrazioni',period))
        print round_((person('RP82_detrazioni_per_mantenimento_cane_guida',period) + vero_valore_RP83_altre_detrazioni),2)
        return round_((person('RP82_detrazioni_per_mantenimento_cane_guida',period) + vero_valore_RP83_altre_detrazioni),2)
