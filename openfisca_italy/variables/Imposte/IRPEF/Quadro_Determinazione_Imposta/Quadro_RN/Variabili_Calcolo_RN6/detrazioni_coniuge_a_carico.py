# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class detrazioni_per_conigue_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni dovute per coniuge a carico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        #reddito per detrazioni è uguale alla somma del RN1_reddito_complessivo - deduzione_abitazione_principale + RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        # if this person doesn't have a spouse this value must be 0
        la_persona_non_ha_un_coniuge_a_carico = person('la_persona_non_ha_un_coniuge_a_carico',period)
        # calcuation basing on income
        return select([la_persona_non_ha_un_coniuge_a_carico,reddito_per_detrazioni<=15000,reddito_per_detrazioni<=40000,
                        reddito_per_detrazioni<=80000,reddito_per_detrazioni>=80000],
                    [0, person('detrazioni_per_conigue_a_carico_reddito_inferiore_15000',period),
                    person('detrazioni_per_conigue_a_carico_reddito_inferiore_40000',period),
                    person('detrazioni_per_conigue_a_carico_reddito_inferiore_80000',period),0])


class detrazioni_per_conigue_a_carico_reddito_inferiore_15000(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Formula per detrazioni dovute per coniuge a carico basata sul reddito per detrazioni"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        quoziente = round_((person('reddito_per_detrazioni',period) / 15000),4)
        mesi_coniuge_a_carico = person('mesi_coniuge_a_carico',period)
        detrazione_spettante = round_(((800-(110*quoziente)) * (mesi_coniuge_a_carico/12)),2)
        # if quoziente is 0 this deduction can not be calculated
        return where(quoziente==0,0,detrazione_spettante)


class detrazioni_per_conigue_a_carico_reddito_inferiore_40000(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Formula per detrazioni dovute per coniuge a carico basata sul reddito per detrazioni"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        mesi_coniuge_a_carico = person('mesi_coniuge_a_carico',period)
        maggiorazione_in_base_al_reddito = person('maggiorazione_detrazioni_coniuge_in_base_al_reddito',period)
        detrazione_spettante = round_(((690*mesi_coniuge_a_carico/12)+maggiorazione_in_base_al_reddito),2)
        # if quoziente is 0 this deduction can not be calculated
        return detrazione_spettante


class maggiorazione_detrazioni_coniuge_in_base_al_reddito(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Maggiorazione per redditi complessivi tra 15000 euro e 40000"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source
    def formula(person,period,parameters):
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        return select([reddito_per_detrazioni<=29000,reddito_per_detrazioni<=29200,
                        reddito_per_detrazioni<=34700,reddito_per_detrazioni<=35000,
                        reddito_per_detrazioni<=35100,
                        reddito_per_detrazioni<=35200,reddito_per_detrazioni<=40000],
                        [0,10,20,30,20,10,0])


class detrazioni_per_conigue_a_carico_reddito_inferiore_80000(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Formula per detrazioni dovute per coniuge a carico basata sul reddito per detrazioni"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        quoziente = round_(((80000-person('reddito_per_detrazioni',period)) / 40000),4)
        mesi_coniuge_a_carico = person('mesi_coniuge_a_carico',period)
        detrazione_spettante = round_(((690*quoziente) * (mesi_coniuge_a_carico/12)),2)
        # if quoziente is 0 this deduction can not be calculated
        return detrazione_spettante


class mesi_coniuge_a_carico(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    label = "Mesi dell'anno in cui il coniuge è stato a carico della persona"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source


class la_persona_non_ha_un_coniuge_a_carico(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha un coniuge a carico?"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameters):
        reddito_coniuge_per_calcolo_detrazioni_coniuge_a_carico = person('reddito_coniuge_per_calcolo_detrazioni_coniuge_a_carico',period)
        il_coniuge_ha_reddito_maggiore_di_soglia = reddito_coniuge_per_calcolo_detrazioni_coniuge_a_carico >= parameters(period).imposte.IRPEF.QuadroRN.detrazioni_carichi_famigliari.soglia_familiare_a_carico
        return il_coniuge_ha_reddito_maggiore_di_soglia


# TO DO, understand how family works and erase this variable
class reddito_coniuge_per_calcolo_detrazioni_coniuge_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito coniuge"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source
