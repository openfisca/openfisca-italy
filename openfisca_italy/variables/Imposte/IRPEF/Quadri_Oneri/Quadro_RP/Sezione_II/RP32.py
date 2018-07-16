# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

import numpy as np

class RP32TipoSpesaPerAcquistoCostruzioneAbitazioniDateInLocazione(Enum):
    tipo_uno = u"acquisto unità immobiliari a destinazione residenziale di nuova costruzione, invendute al 12 novembre 2014"
    tipo_due = u"acquisto di unità immobiliari a destinazione residenziale oggetto di interventi di ristrutturazione edilizia, o di restauro e di risanamento conservativo"
    tipo_tre = u" costruzione di unità immobiliari a destinazione residenziale su aree edificabili già possedute dal contribuente prima dell’inizio dei lavori o sulle quali sono già riconosciuti diritti edificatori e per le quali, prima del 12 novembre 2014, sia stato rilasciato il titolo abilitativo edilizio, comunque denominato"


class RP32_data_stipula_locazione_Rigo_RP32(Variable):
    value_type = date
    default_value = date(1970, 1, 1)
    entity = Persona
    definition_period = YEAR
    label="Rigo RP32 col.1 - Data stipula locazione relativa"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source


class RP32_spesa_acquisto_costruzione_abitazione_data_in_locazione(Variable):
    value_type = float #must be limit to 300000
    entity = Persona
    definition_period = YEAR
    label="Rigo RP32 col.2 - Spesa sostenuta per l’acquisto o la costruzione dell’immobile dato in locazione."
    reference = "http://www.agenziaentra.ps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source


class RP32_interessi_passivi_sui_mutui_abitazione_data_in_locazione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label="RP32 col.3 - Importo degli interessi passivi pagati nell’anno e dipendenti dai mutui contratti per l’acquisto dell’unità immobiliare oggetto dell’agevolazione."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source


class RP32_totale_importo_deducibile_abitazione_data_in_locazione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label="RP32 col.4 - Totale importo deducibile."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source
    def formula(person,period,parameters):
        # limit RP31 col.2
        vero_valore_colonna_2 = where(person('RP32_spesa_acquisto_costruzione_abitazione_data_in_locazione',period)< parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.lim_spesa_acq_costr_imm_dato_loc,person('RP32_spesa_acquisto_costruzione_abitazione_data_in_locazione',period),parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.lim_spesa_acq_costr_imm_dato_loc)
        return round_(((0.2 * vero_valore_colonna_2) / (8 + (0.2* person('RP32_interessi_passivi_sui_mutui_abitazione_data_in_locazione',period)))),2)
