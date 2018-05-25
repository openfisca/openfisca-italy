# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
from openfisca_italy.variables.Imu.imu_common import *
import numpy as np

class rendita_catastale_non_rivalutata_C2(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Rendita catastale non rivalutata C2"

class rendita_catastale_non_rivalutata_C6(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Rendita catastale non rivalutata C6"

class rendita_catastale_non_rivalutata_C7(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Rendita catastale non rivalutata C7"

class percentuale_possesso_C2(Variable):
    value_type = float
    entity = Persona
    default_value = 100
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Percentuale di possesso C2"

class percentuale_possesso_C6(Variable):
    value_type = float
    entity = Persona
    default_value = 100
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Percentuale di possesso C6"

class percentuale_possesso_C7(Variable):
    value_type = float
    entity = Persona
    default_value = 100
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Percentuale di possesso C7"

class mesi_possesso_C2(Variable):
    value_type = float
    entity = Persona
    default_value = 12
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"mesi di possesso C2"

class mesi_possesso_C6(Variable):
    value_type = float
    entity = Persona
    default_value = 12
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"mesi di possesso C6"

class mesi_possesso_C7(Variable):
    value_type = float
    entity = Persona
    default_value = 12
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"mesi di possesso C7"

class is_inagibile_o_storico_C2(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Pertinenza C2 inagibile o storica"

class is_inagibile_o_storico_C6(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Pertinenza C6 inagibile o storica"

class is_inagibile_o_storico_C7(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Pertinenza C7 inagibile o storica"


class importo_pertinenza_C2(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Importo di pertinenza C2"

    def formula(person, period, parameters):
        result = (person('rendita_catastale_non_rivalutata_C2',period)*
                1.05*
                person('moltiplicatore_catastale',period)*
                person('aliquota_imu',period)/1000)

        return round_(where(person('is_inagibile_o_storico_C2',period),result/2,result),2)


class importo_pertinenza_C7(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Importo di pertinenza C7"

    def formula(person, period, parameters):
        result = (person('rendita_catastale_non_rivalutata_C7',period)*
                1.05*
                person('moltiplicatore_catastale',period)*
                person('aliquota_imu',period)/1000)

        return round_(where(person('is_inagibile_o_storico_C7',period),result/2,result))

class importo_pertinenza_C6(Variable):
    value_type = float
    entity = Persona
    default_value = 0
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Importo di pertinenza C6"

    def formula(person, period, parameters):
        result = (person('rendita_catastale_non_rivalutata_C6',period)*
                1.05*
                person('moltiplicatore_catastale',period)*
                person('aliquota_imu',period)/1000)

        return round_(where(person('is_inagibile_o_storico_C6',period),result/2,result))

class importo_pertinenze(Variable):
    value_type = float
    entity = Persona
    default_value = 12
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Importo di tutte le pertinenze"

    def formula(person, period, parameters):
        cat = person('immobile_categoria_catastale',period)
        condition = (   (cat == CategoriaCatastale.A2) +
                        (cat == CategoriaCatastale.A3) +
                        (cat == CategoriaCatastale.A4) +
                        (cat == CategoriaCatastale.A5) +
                        (cat == CategoriaCatastale.A6) +
                        (cat == CategoriaCatastale.A7) )
        condition = condition * person('is_immobile_prima_casa',period)
        importo_totale = (person('importo_pertinenza_C2',period) + person('importo_pertinenza_C7',period) + person('importo_pertinenza_C6',period))
        return where(condition, 0, importo_totale)
