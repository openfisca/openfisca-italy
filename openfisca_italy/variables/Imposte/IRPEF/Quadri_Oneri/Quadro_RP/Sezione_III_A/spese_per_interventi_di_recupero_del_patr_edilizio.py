# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_annue(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Spese per interventi di recupero del patrimonio edilizio e misure antisismiche totali (Rigo RP49)"

    def formula(person,period,parameters):
        spese_scaglioni = ['spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_36',
                            'spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_50',
                            'spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_65',
                            'spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_70',
                            'spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_75',
                            'spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_80',
                            'spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_85',]
        return round_(sum(person(spesa, period) for spesa in spese_scaglioni),2)


class spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_36(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Spese per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 36 %_ i detrazioni "


class spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_50(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Spese per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 50 %_ i detrazioni"


class spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_65(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Spese per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 65 %_ i detrazioni"


class spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_70(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Spese per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 70 %_ i detrazioni"


class spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_75(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Spese per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 75 %_ i detrazioni"


class spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_80(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Spese per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 80 %_ i detrazioni"


class spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_85(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Spese per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 85 %_ i detrazioni"
