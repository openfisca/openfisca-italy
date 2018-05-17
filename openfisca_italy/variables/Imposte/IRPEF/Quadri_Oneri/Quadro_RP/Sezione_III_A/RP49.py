# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_36(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"detrazioni per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 36 %_ i detrazioni (Rigo RP49 col.1)"

    def formula(person,period,parameters):
        return round_((0.36 * person('importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_36',period)),2)


class detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_50(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"detrazioni per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 50 %_ i detrazioni (Rigo RP49 col.2)"

    def formula(person,period,parameters):
        return round_((0.50 * person('importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_50',period)),2)


class detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_65(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"detrazioni per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 65 %_ i detrazioni (Rigo RP49 col.3)"

    def formula(person,period,parameters):
        return round_((0.65 * person('importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_65',period)),2)


class detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_70(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"detrazioni per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 70 %_ i detrazioni (Rigo RP49 col.4)"

    def formula(person,period,parameters):
        return round_((0.70 * person('importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_70',period)),2)


class detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_75(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"detrazioni per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 75 %_ i detrazioni (Rigo RP49 col.5)"

    def formula(person,period,parameters):
        return round_((0.75 * person('importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_75',period)),2)


class detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_80(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"detrazioni per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 80 %_ i detrazioni (Rigo RP49 col.6)"

    def formula(person,period,parameters):
        return round_((0.80 * person('importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_80',period)),2)


class detrazioni_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_85(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"detrazioni per interventi di recupero del patrimonio edilizio e misure antisismiche soggette a 85 %_ i detrazioni (Rigo RP49 col.7)"

    def formula(person,period,parameters):
        return round_((0.85 * person('importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_85',period)),2)
