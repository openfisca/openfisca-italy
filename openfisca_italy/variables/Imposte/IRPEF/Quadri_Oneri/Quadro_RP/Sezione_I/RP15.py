# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# Rigo RP15

class si_vogliono_rateizzare_le_spese_relative_a_righi_RP1_RP2_RP3(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Si vogliono reatizzare le spese relativi ai righi RP1 RP2 RP3(Rigo RP15 col 1)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class si_possono_rateizzare_importo_spese_relative_a_righi_RP1_RP2_RP3(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Si possono rateizzare le spese se il costo dei righi RP1-RP2-RP3 supera la soglia"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        spese_RP1_RP2_RP3 = person('spese_sanitarie_annue',period) + person('spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti_annue',period) + person('spese_sanitarie_per_persone_con_disabilita',period)
        return where (spese_RP1_RP2_RP3> parameters(period).imposte.IRPEF.parametri_spese_quadro_rp.sezione_I_Oneri_spese.importo_minimo_per_rateatizzazione_RP1_RP2_RP2, np.array(True), np.array(False))


class casella_1_totale_spese_su_cui_determinare_la_detrazione_barrata(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "La casella 1 e' stata baratta se si vogliono rateizzare le spese e il costo supera la soglia"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return person('si_vogliono_rateizzare_le_spese_relative_a_righi_RP1_RP2_RP3',period) *  person('si_possono_rateizzare_importo_spese_relative_a_righi_RP1_RP2_RP3',period)


class casella_2_importo_rata_o_somma_RP1_RP2_RP3(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Colonna 2 rigo RP15 : Con casella 1 barrata indicare importo rata, o somma RP1 col. 2, RP2 e RP3"
        reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

        def formula(person,period,parameters):
            casella_1_barrata = person('casella_1_totale_spese_su_cui_determinare_la_detrazione_barrata',period)
            # situazione in cui la casella della rateizzazione non e' stata barrata
            spese_senza_franchigia_casella_1_non_barrata = person('spese_sanitarie_comprensive_di_franchigia_rigo_RP1',period) + person('spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti_annue',period) - parameters(period).imposte.IRPEF.parametri_spese_quadro_rp.sezione_I_Oneri_spese.franchigia_spese_mediche
            spese_senza_franchigia_casella_1_non_barrata = where (spese_senza_franchigia_casella_1_non_barrata > 0, spese_senza_franchigia_casella_1_non_barrata, np.array(0))
            ammontare_da_indicare_in_colonna_2_se_casella_1_non_barrata = spese_senza_franchigia_casella_1_non_barrata + person('spese_sanitarie_per_persone_con_disabilita',period)
            # situazione in cui la casella della rateizzazione e' stata barrata
            spese_senza_franchigia_casella_1_barrata = person('spese_sanitarie_annue',period) + person('spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti_annue',period) - parameters(period).imposte.IRPEF.parametri_spese_quadro_rp.sezione_I_Oneri_spese.franchigia_spese_mediche
            spese_senza_franchigia_casella_1_barrata = where (spese_senza_franchigia_casella_1_barrata > 0, spese_senza_franchigia_casella_1_barrata, np.array(0))
            ammontare_da_indicare_in_colonna_2_se_casella_1_barrata = (spese_senza_franchigia_casella_1_barrata + person('spese_sanitarie_per_persone_con_disabilita',period))/4 # diviso 4 perche' si puo' rateizzare in 4 volte
            return where(casella_1_barrata,round_(ammontare_da_indicare_in_colonna_2_se_casella_1_barrata,2), round_(ammontare_da_indicare_in_colonna_2_se_casella_1_non_barrata,2))


class altre_spese_al_19_colonna_3_rigo_RP15(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        set_input = set_input_divide_by_period
        label = "Colonna 3 rigo RP15 : sommare gli importi dei righi da RP4 a RP7, gli importi dei righi da RP8 a RP13 (con codici da 8 a 39 e codice 99), gli importi delle col 3-4 del rigo RP14 e riportare il totale nella colonna 3. L'importo del codice 29 va diminuito della franchigia di euro 129"
        reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

        def formula(person,period,parameters):
            altre_spese_che_sono_soggette_a_detrazioni_al_19 = person('altre_spese_che_sono_soggette_a_detrazioni_al_19',period)
            spese_per_canoni_leasing_col3_col4 = person('importo_canone_leasing_relativo_a_spese_per_canoni_di_leasing',period) + person('prezzo_di_riscatto_relativo_a_spese_per_canoni_di_leasing',period)
            totale_altre_spese_al_19_colonna_3_rigo_RP15 = altre_spese_che_sono_soggette_a_detrazioni_al_19 + spese_per_canoni_leasing_col3_col4
            # particulare case: se tra le altre spese, e' presente una con codice 29, va sottratto al totale la franchigia
            codice_29_trovato_nelle_altre_spese_da_RP8_a_RP13 = person('codice_29_trovato_nelle_altre_spese_da_RP8_a_RP13',period)
            totale_altre_spese_al_19_colonna_3_rigo_RP15 = where(codice_29_trovato_nelle_altre_spese_da_RP8_a_RP13,totale_altre_spese_al_19_colonna_3_rigo_RP15-parameters(period).imposte.IRPEF.parametri_spese_quadro_rp.sezione_I_Oneri_spese.franchigia_spese_mediche,totale_altre_spese_al_19_colonna_3_rigo_RP15)
            return np.array(round(totale_altre_spese_al_19_colonna_3_rigo_RP15,2))


class oneri_detraibili_al_19(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Totale spese per detrazione al 19 % (Rigo RP15 col 4)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
    def formula(person,period,parameters):
        return person('casella_2_importo_rata_o_somma_RP1_RP2_RP3',period) + person('altre_spese_al_19_colonna_3_rigo_RP15',period)


class oneri_detraibili_al_26(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Totale spese per detrazione al 26 (Rigo RP15 col 5)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return person('altre_spese_che_sono_soggette_a_detrazioni_al_26',period)
