# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imu.imu_common import *

class imposta_imu(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Imposta IMU, risultato della moltiplicazione tra la base imponibile e l'aliquota imu"

    def formula(person, period, parameters):
        is_esenti = where(  person('is_destinazione_ad_uso_di_culto',period)+
                            person('is_destinazione_ad_usi_culturali',period)+
                            person('is_proprieta_santa_sede',period)+
                            person('is_svolgimento_attivita_non_commerciali_di_un_determinato_tipo',period)+
                            person('is_immobile_rurale_ad_uso_strumentale_in_comune_montano',period)+
                            person('is_immobile_posseduto_da_CD',period)+
                            person('is_immobile_posseduto_da_IAP',period)+
                            person('is_immobile_merce',period)
                        ,True,False)

        cat = person('immobile_categoria_catastale',period)
        condition = (
                        (cat == CategoriaCatastale.A2) +
                        (cat == CategoriaCatastale.A3) +
                        (cat == CategoriaCatastale.A4) +
                        (cat == CategoriaCatastale.A5) +
                        (cat == CategoriaCatastale.A6) +
                        (cat == CategoriaCatastale.A7) ) * person('is_immobile_prima_casa',period)
        is_esenti = is_esenti + condition
        is_area_fabbricabile = person('is_area_fabbricabile',period)
        other_case = not_(is_esenti+is_area_fabbricabile)

        risultato_imposta = select(  [
                                is_esenti == True,
                                other_case == True,
                                is_area_fabbricabile == True
                            ],
                            [
                                0,
                                person('base_imponibile',period) * (person('aliquota_imu',period)/1000.00),
                                #Le aree fabbricabili si calcolano RenditaCatastaleNonRivalutata*aliquota_imu
                                person('valore_immobile_non_rivalutato',period)*(person('aliquota_imu',period)/1000.00)
                            ]) + person('importo_pertinenze',period)

        risultato_imposta_divisa_per_possesso = risultato_imposta * (person('percentuale_possesso',period)/100.00) * (person('mesi_di_possesso',period)/12.00)
        return round_(risultato_imposta_divisa_per_possesso,2)

class importo_imu(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Importo IMU, la differenza tra l'imposta imu e le detrazioni"

    def formula(person, period, parameters):
        is_esenti = where(  person('is_destinazione_ad_uso_di_culto',period)+
                            person('is_destinazione_ad_usi_culturali',period)+
                            person('is_proprieta_santa_sede',period)+
                            person('is_svolgimento_attivita_non_commerciali_di_un_determinato_tipo',period)+
                            person('is_immobile_rurale_ad_uso_strumentale_in_comune_montano',period)+
                            person('is_immobile_merce',period)
                        ,True,False)
        #se è esente ritorna 0 altrimenti calcola il risultato
        return where(is_esenti,0,person('imposta_imu',period) - person('detrazioni_imu',period))


class detrazioni_imu(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Detrazioni applicate all'imposta imu"

    def formula(person, period, parameters):
        immobile_categoria_catastale_temp = person('immobile_categoria_catastale',period)

        is_esenti = where(  person('is_destinazione_ad_uso_di_culto',period)+
                            person('is_destinazione_ad_usi_culturali',period)+
                            person('is_proprieta_santa_sede',period)+
                            person('is_svolgimento_attivita_non_commerciali_di_un_determinato_tipo',period)+
                            person('is_immobile_rurale_ad_uso_strumentale_in_comune_montano',period)+
                            person('is_immobile_merce',period)
                        ,True,False)
        a1_a8_a9_case = (((immobile_categoria_catastale_temp == CategoriaCatastale.A1)+
                        (immobile_categoria_catastale_temp == CategoriaCatastale.A8)+
                        (immobile_categoria_catastale_temp == CategoriaCatastale.A9))*
                        (person('is_immobile_prima_casa',period)==True))
        other_case = not_(a1_a8_a9_case) + not_(is_esenti)
        return select( [
                            is_esenti,
                            a1_a8_a9_case,
                            other_case
                        ],
                        [
                            0,
                            200,    #A1,A8,A9 hanno una detrazione fissa di 200 euro
                            0
                        ])
