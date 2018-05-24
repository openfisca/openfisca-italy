# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class moltiplicatore_catastale(Variable):
    value_type = int
    entity = Persona
    default_value = 160
    definition_period = ETERNITY
    label = u"Moltiplicatore catastale dell'immobile"
    reference = u""

    #Not implemented for E and F because they are real estate of State.
    def formula(person, period, parameters):
        immobile_categoria_catastale_temp = person('immobile_categoria_catastale',period)
        c1               =  (immobile_categoria_catastale_temp == CategoriaCatastale.C1)
        d1_10_tranne_d5  =  ((immobile_categoria_catastale_temp == CategoriaCatastale.D1) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.D2) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.D3) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.D4) +

                            (immobile_categoria_catastale_temp == CategoriaCatastale.D6) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.D7) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.D8) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.D9) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.D10))

        a10_d5           =  ((immobile_categoria_catastale_temp == CategoriaCatastale.A10) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.D5))

        c3_c4_c5_b       =  ((immobile_categoria_catastale_temp == CategoriaCatastale.C3) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.C4) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.C5) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.B1) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.B2) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.B3) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.B4) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.B5) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.B6) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.B7) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.B8))

        c2_c6_c7_a1_9    =  ((immobile_categoria_catastale_temp == CategoriaCatastale.C2) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.C6) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.C7) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.A1) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.A2) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.A3) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.A4) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.A5) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.A6) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.A7) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.A8) +
                            (immobile_categoria_catastale_temp == CategoriaCatastale.A9))

        terreno_cd_iap    = (person('is_immobile_posseduto_da_CD',period) + person('is_immobile_posseduto_da_IAP',period)) * immobile_categoria_catastale_temp == CategoriaCatastale.T
        terreno_normale   = not_(person('is_immobile_posseduto_da_CD',period) + person('is_immobile_posseduto_da_IAP',period)) * immobile_categoria_catastale_temp == CategoriaCatastale.T
        return select(  [   c1,
                            d1_10_tranne_d5,
                            a10_d5,
                            c3_c4_c5_b,
                            c2_c6_c7_a1_9,
                            terreno_normale

                        ],
                        [
                            55,
                            65,
                            80,
                            140,
                            160,
                            135
                        ])


class valore_immobile_non_rivalutato(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Valore dell'immobile non rivalutato"


class valore_immobile_rivalutato(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Valore dell'immobile rivalutato"
    def formula(person, period, parameters):
        coefficiente = 0
        immobile_categoria_catastale_temp = person('immobile_categoria_catastale',period)
        coefficiente = where(immobile_categoria_catastale_temp == CategoriaCatastale.T,1.25,1.05)
        #valore del mobile non rivalutato
        return person('valore_immobile_non_rivalutato',period) * coefficiente


class base_imponibile(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Base imponibile dell'immobile"

    def formula(person, period, parameters):
        is_scontato_50_percento = where(    person('is_interesse_storico_artistico',period)+
                                            person('is_inagibile_accertato',period),
                                            True,False)
        is_scontato_25_percento = where(    person('is_canone_concordato',period)*
                                            not_(
                                                (person('immobile_categoria_catastale',period) == CategoriaCatastale.A1)+
                                                (person('immobile_categoria_catastale',period) == CategoriaCatastale.A8)+
                                                (person('immobile_categoria_catastale',period) == CategoriaCatastale.A9)
                                                ),True,False)
        is_scontato_75_percento = where(    is_scontato_25_percento*is_scontato_50_percento,
                                            True,False)
        other_case = not_(is_scontato_25_percento)+not_(is_scontato_50_percento)+not_(is_scontato_75_percento)

        base_imponibile = person('valore_immobile_rivalutato',period) * person('moltiplicatore_catastale',period)
        return select(  [
                            is_scontato_25_percento,
                            is_scontato_50_percento,
                            is_scontato_75_percento,
                            other_case
                        ],[
                            base_imponibile-(base_imponibile*25/100.00),
                            base_imponibile-(base_imponibile*50/100.00),
                            base_imponibile-(base_imponibile*75/100.00),
                            base_imponibile
                        ])


class immobile_categoria_catastale(Variable):
    value_type = Enum
    possible_values = CategoriaCatastale
    default_value = CategoriaCatastale.A4  #default: Abitazione popolare
    entity = Persona
    definition_period = MONTH
    label = u"E' l'indice ufficiale utilizzato in Italia per classificare i beni immobili, e determinarne le rendite"



#I can't control the range of this variable if it's an input.
class aliquota_imu(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Aliquota IMU che cambia a seconda della categoria"

    def formula(person, period, parameters):
        immobile_categoria_catastale_temp = person('immobile_categoria_catastale',period)

        a1_a8_a9 = ((immobile_categoria_catastale_temp == CategoriaCatastale.A1) +
                   (immobile_categoria_catastale_temp == CategoriaCatastale.A8) +
                   (immobile_categoria_catastale_temp == CategoriaCatastale.A9))
        other_case = not_(a1_a8_a9)
        #A1,A8,A9 hanno l'aliquota del 4 per mille
        return select(
                            [a1_a8_a9,  other_case  ]
                            ,
                            [(4),  (7.6)  ]
                    )

class percentuale_possesso(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    default_value = 100
    set_input = set_input_divide_by_period
    label = u"Percentuale di possesso di un immobile"


class mesi_di_possesso(Variable):
    value_type = int
    entity = Persona
    definition_period = MONTH
    default_value = 12
    set_input = set_input_divide_by_period
    label = u"Mesi di possesso di un immobile"


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
                            ])
        risultato_imposta_divisa_per_possesso = risultato_imposta * (person('percentuale_possesso',period)/100.00) * (person('mesi_di_possesso',period)/12.00)
        return risultato_imposta_divisa_per_possesso

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
