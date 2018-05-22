# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_I_common import *
# import numpy
import numpy as np

# TODO: definire per ogni codice il massimo della spesa detraibile

class altre_spese_che_sono_soggette_a_detrazioni_al_19(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Altre spese soggette a detrazione per il 19% (Rigo RP8-Rigo RP13)"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=56"  # Always use the most official source

    def formula(person,period,parameters):
        importo_totale_da_detrarre_altre_spese_al_19 = 0
        # per ogni rigo l'importo potrebbe aumentare oppure no a seconda se il codice presente nel rigo e' quello giusto
        codici_righi = ['codice_altra_spesa_rigo_RP8','codice_altra_spesa_rigo_RP9','codice_altra_spesa_rigo_RP10',
        'codice_altra_spesa_rigo_RP11','codice_altra_spesa_rigo_RP12','codice_altra_spesa_rigo_RP13']
        importi_righi = ['importo_altra_spesa_rigo_RP8','importo_altra_spesa_rigo_RP9','importo_altra_spesa_rigo_RP10',
        'importo_altra_spesa_rigo_RP11','importo_altra_spesa_rigo_RP12','importo_altra_spesa_rigo_RP13']
        # cicliamo tutti i righi
        for codice_rigo,importo_rigo in zip(codici_righi,importi_righi):
            rigo_ha_codice_per_il_19 =  not_(person(codice_rigo,period) == CodiciAltreSpeseDetraibili.codice_42) * not_(person(codice_rigo,period) == CodiciAltreSpeseDetraibili.codice_41) * not_(person(codice_rigo,period) == CodiciAltreSpeseDetraibili.nessun_codice)
            importo_totale_da_detrarre_altre_spese_al_19 = importo_totale_da_detrarre_altre_spese_al_19 + where(rigo_ha_codice_per_il_19,person(importo_rigo,period),0)
        return round_(importo_totale_da_detrarre_altre_spese_al_19,2)

class altre_spese_che_sono_soggette_a_detrazioni_al_26(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Altre spese soggette a detrazione per il 26% (Rigo RP8-Rigo RP13)"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=56"  # Always use the most official source

    def formula(person,period,parameters):
        importo_totale_da_detrarre_altre_spese_al_26 = 0
        # per ogni rigo l'importo potrebbe aumentare oppure no a seconda se il codice presente nel rigo e' quello giusto
        codici_righi = ['codice_altra_spesa_rigo_RP8','codice_altra_spesa_rigo_RP9','codice_altra_spesa_rigo_RP10',
        'codice_altra_spesa_rigo_RP11','codice_altra_spesa_rigo_RP12','codice_altra_spesa_rigo_RP13']
        importi_righi = ['importo_altra_spesa_rigo_RP8','importo_altra_spesa_rigo_RP9','importo_altra_spesa_rigo_RP10',
        'importo_altra_spesa_rigo_RP11','importo_altra_spesa_rigo_RP12','importo_altra_spesa_rigo_RP13']
        # cicliamo tutti i righi
        for codice_rigo,importo_rigo in zip(codici_righi,importi_righi):
            rigo_ha_codice_per_il_26 =  (person(codice_rigo,period) == CodiciAltreSpeseDetraibili.codice_42) + (person(codice_rigo,period) == CodiciAltreSpeseDetraibili.codice_41)
            importo_totale_da_detrarre_altre_spese_al_26 = importo_totale_da_detrarre_altre_spese_al_26 + where(rigo_ha_codice_per_il_26,person(importo_rigo,period),0)
        return round_(importo_totale_da_detrarre_altre_spese_al_26,2)

# variabile particolare utilizzata solo nel calcolo del totale delle spese
class codice_29_trovato_nelle_altre_spese_da_RP8_a_RP13(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "Tra le altre spese nei Righi da RP8 a RP13 c'e' anche il codice 29"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=56"  # Always use the most official source

    def formula(person,period,parameters):
        altra_spesa_codice_29_trovata = np.array(False)
        codici_righi = ['codice_altra_spesa_rigo_RP8','codice_altra_spesa_rigo_RP9','codice_altra_spesa_rigo_RP10',
        'codice_altra_spesa_rigo_RP11','codice_altra_spesa_rigo_RP12','codice_altra_spesa_rigo_RP13']
        for codice in codici_righi:
            altra_spesa_codice_29_trovata = where(altra_spesa_codice_29_trovata,altra_spesa_codice_29_trovata,person(codice,period) == CodiciAltreSpeseDetraibili.codice_29)
        return altra_spesa_codice_29_trovata
