# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# ONERI DETRAIBILI

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


# Condizioni possibili
# condizione per raterizzare : RP1+RP2+RP3 devono essere maggiori di 15.493,71 al lordo della franchigia


# Spese sanitarie rigo rp1

class spese_sanitarie_comprensive_di_franchigia(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie (Rigo RP1 col.2)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class spese_patologie_esenti_sostenute_da_familiare(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie (Rigo RP1 col.1)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class spese_sanitarie_annue(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie (Rigo RP1 totale)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return person('spese_sanitarie_comprensive_di_franchigia',period) + person('spese_patologie_esenti_sostenute_da_familiare',period)


# Spese sanitarie rigo rp2


class spese_sanitarie_per_familiari_non_a_carico_affetti_da_patologie_esistenti_annue(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie per familiari non a carico affetti da patologie esenti (Rigo RP2)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

# Spese sanitarie rigo rp3

class spese_sanitarie_per_persone_con_disabilita(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie per persone con disabilita (Rigo RP3)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

# Spese sanitarie rigo rp4

class spese_veicoli_per_persone_con_disabilita(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese veicoli per persone con disabilita (Rigo RP4 col 2), può essere l'importo totale o una rata"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class NumeroRataDellaDetrazioneSpesePerVeicoliPersoneDisabili(Enum):
    nessun_numero = u"Indica che non si vuola rateizzare la detrazione sull'importo per la spesa sui veicoli per persone con disabilità"
    primo_anno_rata = u"Si è deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilità e questo è il primo anno"
    secondo_anno_rata = u"Si è deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilità e questo è il secondo anno"
    terzo_anno_rata = u"Si è deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilità e questo è il terzo anno"
    quarto_anno_rata = u"Si è deciso di rateizzare la detrazione per la spesa sui veicoli per persone con disabilità e questo è il quarto anno"


class anno_rata_sulla_detrazione_per_spese_veicoli_per_persone_con_disabilita(Variable):
    value_type = Enum
    possible_values = NumeroRataDellaDetrazioneSpesePerVeicoliPersoneDisabili
    default_value = NumeroRataDellaDetrazioneSpesePerVeicoliPersoneDisabili.nessun_numero  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Anno della rata da indicare nel rigo RP4 se si è deciso quest'anno di rateizzare o se l'importo è stato rateizzato fino a tre anni fa e l'anno corrente è il quarto"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


# Spese sanitarie rigo rp5


class spese_acquisto_cani_guida(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese per acquisto di cani guida (Rigo RP5 col.2). Anche in questo caso la detrazione spetta una volta ogni 4 anni salvo perdita dell'animale. Questo valore può essere il totale della spesa o una rata."
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class NumeroRataDellaDetrazioneSpesePerAcquistoCaniGuida(Enum):
    nessun_numero = u"Indica che non si vuola rateizzare la detrazione sull'importo per la spesa per acquisto cani guida"
    primo_anno_rata = u"Si è deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo è il primo anno"
    secondo_anno_rata = u"Si è deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo è il secondo anno"
    terzo_anno_rata = u"Si è deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo è il terzo anno"
    quarto_anno_rata = u"Si è deciso di rateizzare la detrazione per la spesa per acquisto cani guida e questo è il quarto anno"


class anno_rata_sulla_detrazione_per_spese_veicoli_per_acquisto_cani_guida(Variable):
    value_type = Enum
    possible_values = NumeroRataDellaDetrazioneSpesePerAcquistoCaniGuida
    default_value = NumeroRataDellaDetrazioneSpesePerAcquistoCaniGuida.nessun_numero  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Anno della rata da indicare nel rigo RP4 se si è deciso quest'anno di rateizzare o se l'importo è stato rateizzato fino a tre anni fa e l'anno corrente è il quarto"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


# Spese sanitarie rigo rp6


class spese_sanitarie_raetizzate_in_precedenza(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese sanitarie rateizzate in precedenza (Rigo RP6)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

# Spese interessi rigo rp7


class interessi_mutui_ipotecari_acquisto_abitazione_principale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Interessi mutui ipotecari acquisto abitazione principale (Rigo RP7)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


# Altre spese rigo rp8


class altre_spese_che_sono_soggette_a_detrazioni_al_19(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Altre spese soggette a detrazione per il 19% (Rigo RP8-Rigo RP13)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

class altre_spese_che_sono_soggette_a_detrazioni_al_26(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Altre spese soggette a detrazione per il 19% (Rigo RP8-Rigo RP13)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


# Altre spese rigo rp8

class spese_per_canoni_di_leasing(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Spese per canoni di leasing(Rigo RP14)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
