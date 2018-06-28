# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


class RP14_data_stipula_leasing_relativa_a_spese_per_canoni_di_leasing(Variable):
    value_type = date
    default_value = date(1966, 1, 1)
    entity = Persona
    definition_period = ETERNITY
    label = "Rigo RP14 col.1 - Data stipula leasing"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source


# TODO: vedere se c'e' un limite di anni per cui si possa usufruire della detrazione
class RP14_numero_anno_per_cui_il_soggetto_usufruisce_della_detrazione_per_spese_canoni_di_leasing(Variable):
    value_type = date
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP14 col.2 - Numero anno in cui si usufruisce della detrazione, se il contratto e' stato stipulato nel 2017 allora questa variabile assume valore 1"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source

# Questo non fa parte del rigo, ma serve per capire se la detrazione spetta
class RN1_reddito_complessivo_alla_data_atto_stipula_contratto_leasing(Variable):
    value_type = float
    entity = Persona
    definition_period = ETERNITY
    label = "Reddito complessivo alla data di stipula del contratto"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source


# Prendi eta' persona attuale, prendi la data della stipula e fai la differenza
class RP14_eta_persona_stipula_del_contratto_leasing(Variable):
    value_type = float
    entity = Persona
    definition_period = ETERNITY
    label = "Eta' del soggetto quando ha stipulato il contratto di leasing"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source

    def formula(person,period,parameters):
        data_di_nascita = person('data_di_nascita',period)
        data_di_nascita_year = data_di_nascita.astype('datetime64[Y]').astype(int) + 1970
        RP14_data_stipula_leasing_relativa_a_spese_per_canoni_di_leasing = person('RP14_data_stipula_leasing_relativa_a_spese_per_canoni_di_leasing',period)
        data_stipula_leasing_relativa_a_spese_per_canoni_di_leasing_year = RP14_data_stipula_leasing_relativa_a_spese_per_canoni_di_leasing.astype('datetime64[Y]').astype(int) + 1970
        return data_stipula_leasing_relativa_a_spese_per_canoni_di_leasing_year - data_di_nascita_year


class RP14_limite_importo_canone_leasing(Variable):
    value_type = float
    entity = Persona
    definition_period = ETERNITY
    label = "Limite da indicare in RP14 col.3"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source

    def formula(person,period,parameters):
        eta = person('RP14_eta_persona_stipula_del_contratto_leasing',period)
        return where(eta<=35,
                parameters(period).imposte.IRPEF.QuadroRP.sezione_I_Oneri_spese.RP14.RP14_importo_massimo_canone_leasing_meno_35,
                    parameters(period).imposte.IRPEF.QuadroRP.sezione_I_Oneri_spese.RP14.RP14_importo_massimo_canone_leasing_sopra_35)


class RP14_limite_importo_prezzo_riscatto(Variable):
    value_type = float
    entity = Persona
    definition_period = ETERNITY
    label = "Limite da indicare in RP14 col.3"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source

    def formula(person,period,parameters):
        eta = person('RP14_eta_persona_stipula_del_contratto_leasing',period)
        return where(eta<=35,
                parameters(period).imposte.IRPEF.QuadroRP.sezione_I_Oneri_spese.RP14.RP14_importo_prezzo_riscatto_meno_35,
                    parameters(period).imposte.IRPEF.QuadroRP.sezione_I_Oneri_spese.RP14.RP14_importo_prezzo_riscatto_sopra_35)



# TODO:  Quando sarà possibile utilizzare limite calcolato sopra
class RP14_importo_canone_leasing_relativo_a_spese_per_canoni_di_leasing(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP14 col.3 - Importo canone di leasing"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source


# TODO:  Quando sarà possibile utilizzare limite calcolato sopra
class RP14_prezzo_di_riscatto_relativo_a_spese_per_canoni_di_leasing(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Rigo RP14 col.4 - Importo del prezzo di riscatto"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=62"  # Always use the most official source
