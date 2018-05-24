# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
#import numpy
import numpy as np


class RN22_totale_detrazioni_imposta(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni d'imposta annuali"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        tipi_detrazione = ['RN8_totale_detrazioni_per_carichi_di_famiglia_e_lavoro',
        'RN12_detrazione_canoni_di_locazione_e_affitto_terreni_annuo',
        'RN13_detrazioni_per_oneri_detraibili_annuali',
        'RN14_detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue',
        'RN15_detrazioni_per_spese_arredo_immobili_giovani_coppie_iva_acquisto_abitazione_annue',
        'RN16_detrazioni_per_spese_per_interventi_finalizzati_al_risparmio_energetico_annue',
        'RN17_totale_detrazione_oneri_Sez_VI_quadro_RP',
        'RN18_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2014',
        'RN19_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2015',
        'RN20_detrazione_utilizzata_relativa_a_residuo_detrazione_startup_2016',
        'RN21_detrazioni_per_investimenti_startup_utilizzata']
        totale_detrazioni_imposta_annuale = round_(sum(person(detrazione, period) for detrazione in tipi_detrazione),2)
        return np.array(totale_detrazioni_imposta_annuale)
