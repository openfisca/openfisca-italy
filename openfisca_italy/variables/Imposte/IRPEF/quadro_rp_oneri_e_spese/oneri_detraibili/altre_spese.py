# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np

# Altre spese rigo rp8

# possibili codici esistente (dal 9 al 42)
class CodiciAltreSpeseDetraibili(Enum):
    nessun_codice = u"Non c'e' stata nessuna altra spesa per questo rigo relativamente alle altre spese per detrazioni negli oneri deducibili"
    codice_9 = u"Interessi per mutui contratti nel 1997 per recupero edilizio"
    codice_10 = u"Interessi per mutui ipotecari per costruzione abitazione principale"
    codice_11 = u"Interessi per prestiti o mutui agrari"
    codice_12 = u"Spese per istruzione diverse da quelle universitarie"
    codice_13 = u"Spese per istruzione universitaria"
    codice_14 = u"Spese funebri"
    codice_15 = u"Spese per addetti all'assistenza personale"
    codice_16 = u"Spese per attivita' sportive per ragazzi"
    codice_17 = u"Spese per intermediazione immobiliare"
    codice_18 = u"Spese per canoni di locazione sostenute da studenti universitari fuori sede"
    codice_20 = u"Erogazioni liberali a favore delle popolazioni colpite da calamita' pubbliche o eventi straordinari"
    codice_21 = u"Erogazioni liberali alle societa' ed associazioni sportive dilettantistiche"
    codice_22 = u"Contributi associativi alle societa' di mutuo soccorso"
    codice_23 = u"Erogazioni liberali a favore delle associazioni di promozione sociale"
    codice_24 = u"Erogazioni liberali a favore della societa' di cultura Biennale di Venezia"
    codice_25 = u"Spese relative a beni soggetti a regime vincolistico"
    codice_26 = u"Erogazioni liberali per attivita' culturali ed artistiche"
    codice_27 = u"Erogazioni liberali a favore di enti operanti nello spettacolo"
    codice_28 = u"Erogazioni liberali a favore di fondazioni operanti nel settore musicale"
    codice_29 = u"Spese veterinarie"
    codice_30 = u"Spese sostenute per servizi di interpretariato dai soggetti ricosciuti sordi"
    codice_31 = u"Erogazioni liberali a favore degli istituti scolastici di ogni ordine e grado"
    codice_32 = u"Spese relative ai contributi versati per il riscatto degli anni di laurea dei familiari a carico"
    codice_33 = u"Spese per asili nido"
    codice_35 = u"Erogazioni liberali al fondo per l'ammortamento di titoli di Stato"
    codice_36 = u"Premi per assicurazioni sulla vita e contro gli infortuni"
    codice_38 = u"Premi per assicurazioni per tutela delle persone con disaibilita grave"
    codice_39 = u"Premi per assicurazioni per rischio di non autosufficienza"
    codice_41 = u"Erogazioni liberali a favore delle Onlus" # 26%
    codice_42 = u"Erogazioni liberali a favore dei partiti politici" # 26%
    codice_99= u"Altre spese detraibili"

# COLONNE 1 RIGHI RP8-RP13
class codice_altra_spesa_rigo_RP8(Variable):
    value_type = Enum
    possible_values = CodiciAltreSpeseDetraibili
    default_value = CodiciAltreSpeseDetraibili.nessun_codice  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Codice di altra spesa indicato nel Rigo RP8 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class codice_altra_spesa_rigo_RP9(Variable):
    value_type = Enum
    possible_values = CodiciAltreSpeseDetraibili
    default_value = CodiciAltreSpeseDetraibili.nessun_codice  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Codice di altra spesa indicato nel Rigo RP9 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class codice_altra_spesa_rigo_RP10(Variable):
    value_type = Enum
    possible_values = CodiciAltreSpeseDetraibili
    default_value = CodiciAltreSpeseDetraibili.nessun_codice  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Codice di altra spesa indicato nel Rigo RP10 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class codice_altra_spesa_rigo_RP11(Variable):
    value_type = Enum
    possible_values = CodiciAltreSpeseDetraibili
    default_value = CodiciAltreSpeseDetraibili.nessun_codice  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Codice di altra spesa indicato nel Rigo RP11 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class codice_altra_spesa_rigo_RP12(Variable):
    value_type = Enum
    possible_values = CodiciAltreSpeseDetraibili
    default_value = CodiciAltreSpeseDetraibili.nessun_codice  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Codice di altra spesa indicato nel Rigo RP12 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class codice_altra_spesa_rigo_RP13(Variable):
    value_type = Enum
    possible_values = CodiciAltreSpeseDetraibili
    default_value = CodiciAltreSpeseDetraibili.nessun_codice  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = "Codice di altra spesa indicato nel Rigo RP13 col.1"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

# COLONNE 2 RIGHI RP8-RP13

class importo_altra_spesa_rigo_RP8(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Importo indicato nel Rigo RP8 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class importo_altra_spesa_rigo_RP9(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Importo indicato nel Rigo RP9 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class importo_altra_spesa_rigo_RP10(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Importo indicato nel Rigo RP10 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class importo_altra_spesa_rigo_RP11(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Importo indicato nel Rigo RP11 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class importo_altra_spesa_rigo_RP12(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Importo indicato nel Rigo RP12 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class importo_altra_spesa_rigo_RP13(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Importo indicato nel Rigo RP13 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


# Esistono al massimo 6 spese RP13-RP8 ognuna delle quali puo' essere assoggettata al 19% o al 26% di detrazioni a seconda del codice
# Elenco quindi i valori presenti nei vari righi nelle colonne n_2 e poi metto insieme i valori e i codici per capire se debbano essere detratti al 19% o al 26%
# TODO: definire per ogni codice il massimo della spesa detraibile
# Totale altre spese
class altre_spese_che_sono_soggette_a_detrazioni_al_19(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Altre spese soggette a detrazione per il 19% (Rigo RP8-Rigo RP13)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        importo_totale_da_detrarre_altre_spese_al_19 = 0
        # per ogni rigo l'importo potrebbe aumentare oppure no a seconda se il codice presente nel rigo e' quello giusto
        codici_righi = ['codice_altra_spesa_rigo_RP8','codice_altra_spesa_rigo_RP9','codice_altra_spesa_rigo_RP10',
        'codice_altra_spesa_rigo_RP11','codice_altra_spesa_rigo_RP12','codice_altra_spesa_rigo_RP13']
        importi_righi = ['importo_altra_spesa_rigo_RP8','importo_altra_spesa_rigo_RP9','importo_altra_spesa_rigo_RP10',
        'importo_altra_spesa_rigo_RP11','importo_altra_spesa_rigo_RP12','importo_altra_spesa_rigo_RP13']
        print codici_righi
        # cicliamo tutti i righi
        for codice_rigo,importo_rigo in zip(codici_righi,importi_righi):
            rigo_ha_codice_per_il_19 =  not_(person(codice_rigo,period) == CodiciAltreSpeseDetraibili.codice_42) * not_(person(codice_rigo,period) == CodiciAltreSpeseDetraibili.codice_41) * not_(person(codice_rigo,period) == CodiciAltreSpeseDetraibili.nessun_codice)
            importo_totale_da_detrarre_altre_spese_al_19 = importo_totale_da_detrarre_altre_spese_al_19 + where(rigo_ha_codice_per_il_19,person(importo_rigo,period),0)
        return round_(importo_totale_da_detrarre_altre_spese_al_19,2)

class altre_spese_che_sono_soggette_a_detrazioni_al_26(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Altre spese soggette a detrazione per il 26% (Rigo RP8-Rigo RP13)"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        importo_totale_da_detrarre_altre_spese_al_26 = 0
        # per ogni rigo l'importo potrebbe aumentare oppure no a seconda se il codice presente nel rigo e' quello giusto
        codici_righi = ['codice_altra_spesa_rigo_RP8','codice_altra_spesa_rigo_RP9','codice_altra_spesa_rigo_RP10',
        'codice_altra_spesa_rigo_RP11','codice_altra_spesa_rigo_RP12','codice_altra_spesa_rigo_RP13']
        importi_righi = ['importo_altra_spesa_rigo_RP8','importo_altra_spesa_rigo_RP9','importo_altra_spesa_rigo_RP10',
        'importo_altra_spesa_rigo_RP11','importo_altra_spesa_rigo_RP12','importo_altra_spesa_rigo_RP13']
        print codici_righi
        # cicliamo tutti i righi
        for codice_rigo,importo_rigo in zip(codici_righi,importi_righi):
            rigo_ha_codice_per_il_26 =  (person(codice_rigo,period) == CodiciAltreSpeseDetraibili.codice_42) + (person(codice_rigo,period) == CodiciAltreSpeseDetraibili.codice_41)
            importo_totale_da_detrarre_altre_spese_al_26 = importo_totale_da_detrarre_altre_spese_al_26 + where(rigo_ha_codice_per_il_26,person(importo_rigo,period),0)
        return round_(importo_totale_da_detrarre_altre_spese_al_26,2)
