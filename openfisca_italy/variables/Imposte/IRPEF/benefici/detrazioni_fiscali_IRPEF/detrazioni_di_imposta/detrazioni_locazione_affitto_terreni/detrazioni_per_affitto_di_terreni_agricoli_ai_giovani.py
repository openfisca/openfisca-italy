# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class detrazioni_per_affitto_terreni_agricoli_ai_giovani(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione per l’affitto di terreni agricoli ai giovani"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        detrazione_spettante_teorica = 0.19 * person('spese_per_detrazione_affitto_terreni_agricoli_ai_giovani',period)
        detrazione_spettante_teorica = where(detrazione_spettante_teorica>1200, 1200,detrazione_spettante_teorica)
        detrazione_senza_percentuali = select([not_(person('spese_per_detrazione_affitto_terreni_agricoli_ai_giovani_compilato',period)),
                                                True], # in all the other case
                                                [0,detrazione_spettante_teorica])
        return round_((detrazione_senza_percentuali),0)

class spese_per_detrazione_affitto_terreni_agricoli_ai_giovani_compilato(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "E' stato compilato rigo RP72 "
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source