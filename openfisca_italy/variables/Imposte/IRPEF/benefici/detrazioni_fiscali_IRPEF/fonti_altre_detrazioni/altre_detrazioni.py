# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


class altre_detrazioni_annue_totali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni speciali per mantenimento cane guida"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_altre_detrazioni=['detrazioni_per_mantenimento_cane_guida',
                                'altre_detrazioni']
        return round_(sum(person(detrazione, period) for detrazione in tipi_altre_detrazioni),2)


class detrazioni_per_mantenimento_cane_guida(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni speciali per mantenimento cane guida"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return where (person('spese_mantenimento_cane_guida',period),np.array(516.46),np.array(0))


# Detrazioni investimenti startup


class ammontare_importo_detraibile_ricevuto_per_trasparenza_investimenti_startup(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo che esiste solamente se persona ha effettuato un tipo di investimento con codice 4 o 5 (Se esiste va scritto direttamentenel Rigo RP80 col. 6)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class ammontare_detrazioni_investimenti_startup(Variable):
        value_type = float
        entity = Persona
        definition_period = YEAR
        label = u"Importo che esiste solamente se persona non ha effettuato un tipo di investimento con codice 4 o 5 (Rigo RP80 col. 5)"
        reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

        def formula(person,period,parameters):
            diritto_a_compilare_colonna_codice_e_ammontare_detrazione = person('diritto_a_compilare_colonna_codice_e_ammontare_detrazione_investimenti_startup',period)
            ammontare_detrazioni = round_((person('ammontare_investimento_detraibile_investimenti_startup',period) * 0.30),2)
            return where(diritto_a_compilare_colonna_codice_e_ammontare_detrazione,ammontare_detrazioni,0)


class totale_detrazioni_per_investimenti_startup(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Detrazione per investimenti in startup indicati nel quadro VI del Quadro RP (Detrazioni investimenti startup) (Rigo RP80 col.6)"
    def formula(person,period,parameters):
        diritto_a_compilare_colonna_codice_e_ammontare_detrazione = person('diritto_a_compilare_colonna_codice_e_ammontare_detrazione_investimenti_startup',period)
        return where(diritto_a_compilare_colonna_codice_e_ammontare_detrazione,person('ammontare_detrazioni_investimenti_startup',period),round_(person('ammontare_importo_detraibile_ricevuto_per_trasparenza_investimenti_startup',period),2))
