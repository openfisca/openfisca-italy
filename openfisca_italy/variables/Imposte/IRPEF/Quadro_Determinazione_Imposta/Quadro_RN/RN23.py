# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class RN23_detrazioni_spese_sanitarie_per_determinate_patologie(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RN23  quadro RN"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        franchigia = parameters(period).imposte.IRPEF.QuadroRP.sezione_I_Oneri_spese.franch_spese_med
        # caso 1
        RP15_casella_1_totale_spese_su_cui_determinare_la_detrazione_barrata = person('RP15_casella_1_totale_spese_su_cui_determinare_la_detrazione_barrata',period)
        #caso 2
        col_2_rigo_RP1_e_rigo_RP2_non_compilati = (person('RP1_spese_sanitarie_comprensive_di_franchigia_rigo_RP1',period) == 0) * (person('RP2_spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti',period) == 0)
        spesa_da_restituire_se_caso_2_True = 0.19 * (person('RP1_spese_patologie_esenti_sostenute_da_familiare',period)-franchigia)
        spesa_da_restituire_se_caso_2_True = where(spesa_da_restituire_se_caso_2_True>0,spesa_da_restituire_se_caso_2_True,0) # se questo valore è minore di 0 allora ritorna 0
        # caso 3
        col_2_rigo_RP1_o_rigo_RP2_compilata = not_(person('RP1_spese_sanitarie_comprensive_di_franchigia_rigo_RP1',period) == 0) + not_(person('RP2_spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti',period) == 0)
        spese_RP1_RP2_caso_3 = person('RP1_spese_sanitarie_comprensive_di_franchigia_rigo_RP1',period) + person('RP2_spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti',period)
        spesa_da_restituire_se_caso_3_True =  select([spese_RP1_RP2_caso_3>=franchigia, spese_RP1_RP2_caso_3 < franchigia],
                                                    [0.19 * person('RP1_spese_patologie_esenti_sostenute_da_familiare',period),
                                                     (0.19 * (person('RP1_spese_patologie_esenti_sostenute_da_familiare',period) - (franchigia - spese_RP1_RP2_caso_3)))])
        return select([RP15_casella_1_totale_spese_su_cui_determinare_la_detrazione_barrata,
                        col_2_rigo_RP1_e_rigo_RP2_non_compilati,
                        col_2_rigo_RP1_o_rigo_RP2_compilata],
                        [0,
                        round(spesa_da_restituire_se_caso_2_True,2),
                        round(spesa_da_restituire_se_caso_3_True,2)])
