# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class RP60_totale_rate_spesa_arredo_immobili_ristrutturati_gc_iva_acquisto_abitazione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP60 -  riportare la somma degli importi indicati nelle colonne 3 e 6 dei righi RP57, nella colonna 3 del rigo RP58, e nella colonna 3 del rigo RP59 di tutti i moduli compilati. Su questo importo si determina la detrazione del 50 per cento che va riportata nel rigo RN15."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=75"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_rate_spese_arredo_immobili = ['RP57_importo_rata_spesa_arredo_immobili_ristrutturati',
                                            'RP58_importo_rata_spesa_arredo_immobili_giovani_coppie',
                                            'RP59_importo_rata_iva_per_acquisto_abitazione_classe_energetica',]
        return round_(sum(person(tipo_rata, period) for tipo_rata in tipi_rate_spese_arredo_immobili),2)
