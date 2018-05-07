# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class detrazioni_per_figli_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni dovute per figli a carico teorica"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameter):
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        incremento = (person('numero_figli_a_carico',period)-1) * 15000
        quoziente = round_((((95000 + incremento) - reddito_per_detrazioni)/(95000 + incremento)),4)
        # deduction formula used if quoziente is valid
        detrazione_spettante = round_((person('detrazioni_per_figli_a_carico_teorica',period) * quoziente),2)
        detrazione_fissa_per_numero_figli_dopo_il_terzo = where (person('numero_figli_a_carico',period),parameter(period).imposte.IRPEF.detrazioni.detrazioni_carichi_famigliari.detrazioni_tipi_figli.ulteriore_detrazione_figli_a_carico,0)
        detrazione_spettante = detrazione_spettante + detrazione_fissa_per_numero_figli_dopo_il_terzo
        # check if quoziente is valid or not
        quoziente_valido = quoziente > 0 * quoziente < 1
        # if quoziente is less than 0 the deduction is 0 instead there is a formula to calculate it use the theoretical deduction
        return select( [not_(quoziente_valido),quoziente_valido],[0,detrazione_spettante])


# TO DO: in italian legislation, every tipology of child has a durance in month in a year. This is not defined because of tools fault. 
# It takes for granted that a child maintains a condition for a whole year, which is not true at all.
# For example a child who is 3 years old during the year will be 4 so the condition will change.
# These notes are valid only for the theoretical detraction, the formula of detrazioni_per_figli_a_carico is correct (the result is non correct at all because
# of the value of the theoretical deduction).
# I can't evaluate the percentage of responsibility too. 


class detrazioni_per_figli_a_carico_teorica(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni dovute per figli a carico teorica"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person,period,parameter):
        # to avoid user set number of child less than 0
        numero_figli_inferiore_tre_anni_a_carico = where( person('numero_figli_inferiore_tre_anni_a_carico',period) >=0, person('numero_figli_inferiore_tre_anni_a_carico',period),0)
        numero_figli_maggiore_tre_anni_a_carico = where( person('numero_figli_maggiore_tre_anni_a_carico',period) >=0, person('numero_figli_maggiore_tre_anni_a_carico',period),0)
        numero_totale_figli = person('numero_figli_a_carico',period)
        numero_figli_dopo_il_terzo = numero_totale_figli - 3
        # if user set that child with disability are more than the total number of child, result that it have a number of son with disabilities like the number of sons
        numero_figli_maggiore_disabili_a_carico =  where ( person('numero_figli_maggiore_disabili_a_carico',period)<=numero_totale_figli, person('numero_figli_maggiore_disabili_a_carico',period),numero_totale_figli )
        # evaluation
        detrazione_per_numero_figli_inferiore_tre_anni_a_carico = numero_figli_inferiore_tre_anni_a_carico * parameter(period).imposte.IRPEF.detrazioni.detrazioni_carichi_famigliari.detrazioni_tipi_figli.detrazione_figli_eta_minore_tre
        detrazione_per_numero_figli_maggiore_tre_anni_a_carico = numero_figli_maggiore_tre_anni_a_carico * parameter(period).imposte.IRPEF.detrazioni.detrazioni_carichi_famigliari.detrazioni_tipi_figli.detrazione_figli_eta_maggiore_tre
        detrazione_per_numero_figli_se_possiede_piu_di_3_figli = numero_totale_figli * parameter(period).imposte.IRPEF.detrazioni.detrazioni_carichi_famigliari.detrazioni_tipi_figli.detrazione_aggiuntiva_per_figlio_dopo_terzo
        detrazione_per_numero_figli_maggiore_disabili_a_carico = numero_figli_maggiore_disabili_a_carico * parameter(period).imposte.IRPEF.detrazioni.detrazioni_carichi_famigliari.detrazioni_tipi_figli.detrazione_figli_handicap
        
        return detrazione_per_numero_figli_inferiore_tre_anni_a_carico + detrazione_per_numero_figli_maggiore_tre_anni_a_carico + detrazione_per_numero_figli_se_possiede_piu_di_3_figli + detrazione_per_numero_figli_maggiore_disabili_a_carico


class numero_figli_inferiore_tre_anni_a_carico(Variable):
    value_type = int 
    entity = Persona
    definition_period = YEAR
    label = "Numero di figli con età inferiore a 3 anni a carico"


class numero_figli_maggiore_tre_anni_a_carico(Variable):
    value_type = int 
    entity = Persona
    definition_period = YEAR
    label = "Numero di figli con età maggiore di 3 anni a carico"    


class numero_figli_maggiore_disabili_a_carico(Variable):
    value_type = int 
    entity = Persona
    definition_period = YEAR
    label = "Numero di figli disabili"     

class numero_figli_a_carico(Variable):
    value_type = int 
    entity = Persona
    definition_period = YEAR
    label = "Numero di figli a carico"

    def formula(person,period,parameter):
        numero_figli_inferiore_tre_anni_a_carico = where( person('numero_figli_inferiore_tre_anni_a_carico',period) >=0, person('numero_figli_inferiore_tre_anni_a_carico',period),0)
        numero_figli_maggiore_tre_anni_a_carico = where( person('numero_figli_maggiore_tre_anni_a_carico',period) >=0, person('numero_figli_maggiore_tre_anni_a_carico',period),0)
        return numero_figli_inferiore_tre_anni_a_carico + numero_figli_maggiore_tre_anni_a_carico