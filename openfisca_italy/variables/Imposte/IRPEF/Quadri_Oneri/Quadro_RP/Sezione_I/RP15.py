# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# Rigo RP15

class RP15_si_vogliono_rateizzare_le_spese_relative_a_righi_RP1_RP2_RP3(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP15 col 1 - Si vogliono reatizzare le spese relativi ai righi RP1 RP2 RP3"


class RP15_si_possono_rateizzare_importo_spese_relative_a_righi_RP1_RP2_RP3(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Si possono rateizzare le spese se il costo dei righi RP1-RP2-RP3 supera la soglia"

    def formula(person,period,parameters):
        spese_RP1_RP2_RP3 = person('RP1_totale_spese_sanitarie',period) + person('RP2_spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti',period) + person('RP3_spese_sanitarie_per_persone_con_disabilita',period)
        print 'uscito fuori', person('RP2_spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti',period)
        return where (spese_RP1_RP2_RP3> parameters(period).imposte.IRPEF.QuadroRP.sezione_I_Oneri_spese.importo_minimo_per_rateatizzazione_RP1_RP2_RP2, np.array(True), np.array(False))


class RP15_casella_1_totale_spese_su_cui_determinare_la_detrazione_barrata(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La casella 1 e' stata baratta se si vogliono rateizzare le spese e il costo supera la soglia"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source

    def formula(person,period,parameters):
        return person('RP15_si_vogliono_rateizzare_le_spese_relative_a_righi_RP1_RP2_RP3',period) *  person('RP15_si_possono_rateizzare_importo_spese_relative_a_righi_RP1_RP2_RP3',period)


class RP15_casella_2_importo_rata_o_somma_RP1_RP2_RP3(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Rigo RP15 col.2 - Con casella 1 barrata indicare importo rata, o somma RP1 col. 2, RP2 e RP3"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source

        def formula(person,period,parameters):
            casella_1_barrata = person('RP15_casella_1_totale_spese_su_cui_determinare_la_detrazione_barrata',period)
            # situazione in cui la casella della rateizzazione non e' stata barrata
            spese_senza_franchigia_casella_1_non_barrata = person('RP1_spese_sanitarie_comprensive_di_franchigia_rigo_RP1',period) + person('RP2_spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti',period) - parameters(period).imposte.IRPEF.QuadroRP.sezione_I_Oneri_spese.franchigia_spese_mediche
            spese_senza_franchigia_casella_1_non_barrata = where (spese_senza_franchigia_casella_1_non_barrata > 0, spese_senza_franchigia_casella_1_non_barrata, np.array(0))
            ammontare_da_indicare_in_colonna_2_se_casella_1_non_barrata = spese_senza_franchigia_casella_1_non_barrata + person('RP3_spese_sanitarie_per_persone_con_disabilita',period)
            # situazione in cui la casella della rateizzazione e' stata barrata
            spese_senza_franchigia_casella_1_barrata = person('RP1_totale_spese_sanitarie',period) + person('RP2_spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti',period) - parameters(period).imposte.IRPEF.QuadroRP.sezione_I_Oneri_spese.franchigia_spese_mediche
            spese_senza_franchigia_casella_1_barrata = where (spese_senza_franchigia_casella_1_barrata > 0, spese_senza_franchigia_casella_1_barrata, np.array(0))
            ammontare_da_indicare_in_colonna_2_se_casella_1_barrata = (spese_senza_franchigia_casella_1_barrata + person('RP3_spese_sanitarie_per_persone_con_disabilita',period))/4 # diviso 4 perche' si puo' rateizzare in 4 volte
            return where(casella_1_barrata,round_(ammontare_da_indicare_in_colonna_2_se_casella_1_barrata,2), round_(ammontare_da_indicare_in_colonna_2_se_casella_1_non_barrata,2))


class RP15_altre_spese_al_19_colonna_3(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "RP15 col.3: sommare gli importi dei righi da RP4 a RP7, gli importi dei righi da RP8 a RP13 (con codici da 8 a 39 e codice 99), gli importi delle col 3-4 del rigo RP14 e riportare il totale nella colonna 3. L'importo del codice 29 va diminuito della franchigia di euro 129"
        reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source

        def formula(person,period,parameters):
            altre_spese_che_sono_soggette_a_detrazioni_al_19 = person('altre_spese_che_sono_soggette_a_detrazioni_al_19',period)
            spese_per_canoni_leasing_col3_col4 = person('RP14_importo_canone_leasing_relativo_a_spese_per_canoni_di_leasing',period) + person('RP14_prezzo_di_riscatto_relativo_a_spese_per_canoni_di_leasing',period)
            totale_altre_spese_al_19_colonna_3_rigo_RP15 = altre_spese_che_sono_soggette_a_detrazioni_al_19 + spese_per_canoni_leasing_col3_col4
            # particulare case: se tra le altre spese, e' presente una con codice 29, va sottratto al totale la franchigia
            codice_29_trovato_nelle_altre_spese_da_RP8_a_RP13 = person('codice_29_trovato_nelle_altre_spese_da_RP8_a_RP13',period)
            totale_altre_spese_al_19_colonna_3_rigo_RP15 = where(codice_29_trovato_nelle_altre_spese_da_RP8_a_RP13,totale_altre_spese_al_19_colonna_3_rigo_RP15-parameters(period).imposte.IRPEF.QuadroRP.sezione_I_Oneri_spese.franchigia_spese_mediche,totale_altre_spese_al_19_colonna_3_rigo_RP15)
            return np.array(round(totale_altre_spese_al_19_colonna_3_rigo_RP15,2))


class RP15_oneri_detraibili_al_19(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP15 col 4 -Totale spese per detrazione al 19 %"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source

    def formula(person,period,parameters):
        return person('RP15_casella_2_importo_rata_o_somma_RP1_RP2_RP3',period) + person('RP15_altre_spese_al_19_colonna_3',period)


class RP15_oneri_detraibili_al_26(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP15 col 5 - Totale spese per detrazione al 26"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source

    def formula(person,period,parameters):
        return person('altre_spese_che_sono_soggette_a_detrazioni_al_26',period)
