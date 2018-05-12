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
    label = "Si vogliono reatizzare le spese relativi ai righi RP1(Rigo RP15 col 4)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

class si_possono_rateizzare_importo_spese_relative_a_righi_RP1_RP2_RP3(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Se si vogliono rateizzare le spese e l'importo di queste tre supera la soglia allora si può effettuare la rateatizzazione"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        si_vogliono_rateizzare_le_spese_relative_a_righi_RP1_RP2_RP3 = person('si_vogliono_rateizzare_le_spese_relative_a_righi_RP1_RP2_RP3',period)
        spese = person('spese_sanitarie_annue',period) + person('spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti_annue',period) + person('spese_sanitarie_per_persone_con_disabilita',period)
        return where (si_vogliono_rateizzare_le_spese_relative_a_righi_RP1_RP2_RP3 * spese> )


class oneri_detraibili_al_19(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Totale spese per detrazione al 19 % (Rigo RP15 col 4)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        franchigia = parameters(period).imposte.IRPEF.parametri_spese_quadro_rp.spese_mediche.franchigia_spese_mediche
        # RIGO rp2
        rigo_RP2 = person('spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti_annue',period)
        somma_rigo_RP2_per_somma_detraibile_al_19 = where(rigo_RP2<=6197.48,  (rigo_RP2 - franchigia), 6197.48)
        tipi_spesa = ['spese_sanitarie_annue','spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti_annue',
                        'spese_sanitarie_per_persone_con_disabilita',
                        'spese_veicoli_per_persone_con_disabilita',
                        'spese_acquisto_cani_guida',
                        'spese_sanitarie_raetizzate_in_precedenza',
                        'spese_per_canoni_di_leasing',
                        'interessi_mutui_ipotecari_acquisto_abitazione_principale','altre_spese_che_sono_soggette_a_detrazioni_al_19']
        return round_(sum(person(spesa, period) for spesa in tipi_spesa),2) - np.array(129.11)


class oneri_detraibili_al_26(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Totale spese per detrazione al 26 (Rigo RP15 col 5)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return person('altre_spese_che_sono_soggette_a_detrazioni_al_26',period)
