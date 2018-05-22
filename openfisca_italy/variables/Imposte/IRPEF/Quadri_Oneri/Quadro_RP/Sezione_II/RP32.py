# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

import numpy as np

class TipoSpesaPerAcquistoCostruzioneAbitazioniDateInLocazione(Enum):
    tipo_uno = u"acquisto unità immobiliari a destinazione residenziale di nuova costruzione, invendute al 12 novembre 2014"
    tipo_due = u"acquisto di unità immobiliari a destinazione residenziale oggetto di interventi di ristrutturazione edilizia, o di restauro e di risanamento conservativo"
    tipo_tre = u" costruzione di unità immobiliari a destinazione residenziale su aree edificabili già possedute dal contribuente prima dell’inizio dei lavori o sulle quali sono già riconosciuti diritti edificatori e per le quali, prima del 12 novembre 2014, sia stato rilasciato il titolo abilitativo edilizio, comunque denominato"


class data_stipula_locazione_Rigo_RP32(Variable):
    value_type = date
    default_value = date(1970, 1, 1)
    entity = Persona
    definition_period = YEAR
    label="Data stipula locazione relativa al Rigo RP32 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source


class spesa_acquisto_costruzione_abitazione_data_in_locazione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label="Spesa sostenuta per l’acquisto o la costruzione dell’immobile dato in locazione RP32 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source


class interessi_passivi_sui_mutui_abitazione_data_in_locazione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label="Importo degli interessi passivi pagati nell’anno e dipendenti dai mutui contratti per l’acquisto dell’unità immobiliare oggetto dell’agevolazione RP32 col.3 "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source


class totale_importo_deducibile_abitazione_data_in_locazione(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label="Totale importo deducibile RP32 col.4 "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=67"  # Always use the most official source
    def formula(person,period,parameters):
        vero_valore_colonna_2 = where(person('spesa_acquisto_costruzione_abitazione_data_in_locazione',period)< parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_spesa_acquisto_costruzione_immobile_dato_locazione,person('spesa_acquisto_costruzione_abitazione_data_in_locazione',period),parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_spesa_acquisto_costruzione_immobile_dato_locazione)
        return round_(((0.2 * vero_valore_colonna_2) / (8 + (0.2* person('interessi_passivi_sui_mutui_abitazione_data_in_locazione',period)))),2)
