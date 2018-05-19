# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class RP_39_totale_oneri_deducibili(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Rp39 - Totale degli oneri deducibili"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=68"  # Always use the most official source

    def formula(person,period,parameters):
        elementi_da_sommare = ['contributi_previdenziali_assistenziali','assegno_periodico_al_coniuge','contributi_addetti_servizi_domestici_e_familiari',
                                'erogazioni_liberali_a_istituzioni_religiose','spese_mediche_e_assistenza_disabili','altri_oneri_e_spese_deducibili',
                                'contributi_deducibilita_ordinaria_non_dedotti_dal_sostituto','contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto','contributi_per_fondi_in_squilibrio_finanziario_non_dedotti_dal_sostituto',
                                'contributi_versati_per_familiari_a_carico_non_dedotti_dal_sostituto','contributi_fondo_pensione_negoziale_dipendenti_pubblici_non_dedotti_dal_sostituto','totale_importo_deducibile_abitazione_data_in_locazione',
                                'totale_restuzione_somme_al_soggetto_erogatore_rigo_RP33','totale_importo_RPF_2018_Rigo_RP34','importo_residuo_RPF_2017_Rigo_RP34',
                                'importo_residuo_RPF_2016_Rigo_RP34','importo_residuo_RPF_2015_Rigo_RP34']
        return round_(sum(person(elemento, period) for elemento in elementi_da_sommare),2)
