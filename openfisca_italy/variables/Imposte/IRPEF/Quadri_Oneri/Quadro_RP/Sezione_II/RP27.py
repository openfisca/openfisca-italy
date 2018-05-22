# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_II_common import *
import numpy as np


class RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = " Rigo RP27 col.1 - Indicare l’importo dei contributi che il sostituto d’imposta ha dedotto dall’imponibile, di cui al punto 412 della Certificazione Unica."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

    def formula(person,period,parameters):
        importo_punto_412_certificazione_unica = person('importo_punto_412_certificazione_unica',period)
        punto_421_certificazione_unica_compilato = not_(person('importo_punto_421_certificazione_unica',period)==0)
        importo_punto_422_certificazione_unica = person('importo_punto_422_certificazione_unica',period)
        importo = where (punto_421_certificazione_unica_compilato,importo_punto_412_certificazione_unica - importo_punto_422_certificazione_unica , importo_punto_412_certificazione_unica)
        codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_uno
        return where (codice_campo_411_valido, importo ,0)

class RP27_contributi_deducibilita_ordinaria_non_dedotti_dal_sostituto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = " Rigo RP27 col.2 - Indicare l’importo minore tra due operazioni definire nel documento di riferimento."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source

    def formula(person,period,parameters):
        # restituire il minor importo tra
        oneri_di_previdenza_complementare_per_i_quali_si_chiede_la_deduzione = person('importo_punto_413_certificazione_unica',period) + person('somme_versate_forme_pensionistiche_per_calcolo_RigoRP27_col_2',period)
        limite_deducibilita_per_RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto = parameters(period).imposte.IRPEF.QuadroRP.Sezione_II.limite_importo_deducibile_contributi_deducibilita_ordinaria - person('RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto',period)
        limite_deducibilita_per_RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto = where(limite_deducibilita_per_RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto>0,limite_deducibilita_per_RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto,np.array(0))
        importo =  round_(min_(oneri_di_previdenza_complementare_per_i_quali_si_chiede_la_deduzione,limite_deducibilita_per_RP27_contributi_deducibilita_ordinaria_dedotti_dal_sostituto),2)
        codice_campo_411_valido = person('codice_inserito_campo_411_modello_unico',period) == TipiCodiciCampo411ModelloUnico.codice_uno
        return where (codice_campo_411_valido, importo ,0)

class somme_versate_forme_pensionistiche_per_calcolo_RigoRP27_col_2(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Somme versate fondi pensionistici "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=66"  # Always use the most official source
