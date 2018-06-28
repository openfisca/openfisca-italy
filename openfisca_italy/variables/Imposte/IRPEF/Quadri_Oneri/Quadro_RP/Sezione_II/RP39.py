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
        righi_RP_21_26 = ['RP21_contributi_previdenziali_assistenziali','RP22_assegno_periodico_al_coniuge','RP23_contributi_addetti_servizi_domestici_e_familiari',
                                'RP24_erogazioni_liberali_a_istituzioni_religiose','RP25_spese_mediche_e_assistenza_disabili','RP26_altri_oneri_e_spese_deducibili']
        righi_RP_27_31 = ['RP_28_limite_importo_deducibile_contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto','RP29_contributi_per_fondi_in_squilibrio_finanziario_non_dedotti_dal_sostituto','RP27_30_31_limite_importo_deducibile']
        righi_RP_32_34 = ['RP32_totale_importo_deducibile_abitazione_data_in_locazione',
                                'RP33_totale_restituzione_somme_al_soggetto_erogatore','RP34_totale_importo_RPF_2018','RP34_importo_residuo_RPF_2017',
                                'RP34_importo_residuo_RPF_2016','RP34_importo_residuo_RPF_2015']
        elementi_da_sommare = []
        elementi_da_sommare.append(righi_RP_21_26)
        elementi_da_sommare.append(righi_RP_27_31)
        elementi_da_sommare.append(righi_RP_32_34)
        importo_oneri_deducibili = 0
        for lista in elementi_da_sommare:
                importo_oneri_deducibili = importo_oneri_deducibili + round_(sum(person(elemento, period) for elemento in lista),2)
        return importo_oneri_deducibili

class RP27_30_31_limite_importo_deducibile(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Massimo importo deducibile da indicare dei righi RP 27 - 30 - 31"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source
    def formula(person,period,parameters):
        # calcolo capienza_RP28
        limite_deducibilita = parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_importo_deducibile_contributi_versati_lavoratori_prima_occupazione #limite di deducibilità normale
        # eventuale maggiorazione del limite di deduciblità
        eventuale_aumento_limite_deducibilita_maggiorato = (25822.85 - person('RP28_contributi_versati_nei_primi_5_anni_per_maggior_limite_deducibilita',period))
        eventuale_aumento_limite_deducibilita_maggiorato = where(eventuale_aumento_limite_deducibilita_maggiorato<2582,eventuale_aumento_limite_deducibilita_maggiorato,2582)
        limite_deducibilita = round((where(person('RP28_hanno_diritto_a_maggior_limite_di_deducibilita',period),(eventuale_aumento_limite_deducibilita_maggiorato + limite_deducibilita) ,limite_deducibilita)),2)
        capienza_RP28 = limite_deducibilita - person('RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto',period) - person('RP28_contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto',period) - person('RP29_contributi_per_fondi_in_squilibrio_finanziario_dedotti_dal_sostituto',period) - person('RP30_contributi_versati_per_familiari_a_carico_dedotti_dal_sostituto',period) - person('RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_dedotti_dal_sostituto',period)
        capienza_RP28 = where(capienza_RP28<0, 0, capienza_RP28)
        #calcolo limite di deduciblità per Rp 27-30-31
        limite_di_deduciblita_RP27_30_31 = capienza_RP28 - 2582 - person('RP28_contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto',period)
        limite_di_deduciblita_RP27_30_31 = round_((where(limite_di_deduciblita_RP27_30_31<0,0,limite_di_deduciblita_RP27_30_31)),2)
        #deduzione richiesta
        deduzione_richiesta = round_((person('RP27_contributi_deducibilita_ordinaria_non_dedotti_dal_sostituto',period) + person('RP30_contributi_versati_per_familiari_a_carico_non_dedotti_dal_sostituto',period) + person('RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_non_dedotti_dal_sostituto',period)),2)
        return where(deduzione_richiesta<limite_di_deduciblita_RP27_30_31,deduzione_richiesta,limite_di_deduciblita_RP27_30_31)


class RP_28_limite_importo_deducibile_contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Rigo RP28 Col.2 sottoposto al limite di deducibilità da utilizzare per il calcolo degli oneri deducibili"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source
        def formula(person,period,parameters):
            limite_deducibilita = parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_importo_deducibile_contributi_versati_lavoratori_prima_occupazione #limite di deducibilità normale
            # eventuale maggiorazione del limite di deduciblità
            eventuale_aumento_limite_deducibilita_maggiorato = (25822.85 - person('RP28_contributi_versati_nei_primi_5_anni_per_maggior_limite_deducibilita',period))
            eventuale_aumento_limite_deducibilita_maggiorato = where(eventuale_aumento_limite_deducibilita_maggiorato<2582,eventuale_aumento_limite_deducibilita_maggiorato,2582)
            limite_deducibilita = round((where(person('RP28_hanno_diritto_a_maggior_limite_di_deducibilita',period),(eventuale_aumento_limite_deducibilita_maggiorato + limite_deducibilita) ,limite_deducibilita)),2)
            capienza_RP28 = limite_deducibilita - person('RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto',period) - person('RP28_contributi_per_lavoratori_prima_occupazione_dedotti_dal_sostituto',period) - person('RP29_contributi_per_fondi_in_squilibrio_finanziario_dedotti_dal_sostituto',period) - person('RP30_contributi_versati_per_familiari_a_carico_dedotti_dal_sostituto',period) - person('RP31_contributi_fondo_pensione_negoziale_dipendenti_pubblici_dedotti_dal_sostituto',period)
            capienza_RP28 = where(capienza_RP28<0, 0, capienza_RP28)
            RP28_col2 = person('RP28_contributi_per_lavoratori_prima_occupazione_non_dedotti_dal_sostituto',period)
            return where(RP28_col2<=capienza_RP28,RP28_col2,capienza_RP28)
