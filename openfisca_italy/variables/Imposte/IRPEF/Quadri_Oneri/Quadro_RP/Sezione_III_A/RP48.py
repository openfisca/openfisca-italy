# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_36(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 36% (Rigo RP48 col.1)"

    def formula(person,period,parameters):
        return person('spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_36',period)/10.00

class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_50(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR

    label = u"Importo rata per spese sezione III A con diritto di detrazione al 50% (Rigo RP48 col.2)"

    def formula(person,period,parameters):
        return person('spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_50',period)/10.00

class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_65(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 65% (Rigo RP48 col.3)"

    def formula(person,period,parameters):
        return person('spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_65',period)/10.00


class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_70(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 70% (Rigo RP48 col.4)"

    def formula(person,period,parameters):
        return person('spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_70',period)/10.00


class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_75(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 75% (Rigo RP48 col.5)"

    def formula(person,period,parameters):
        return person('spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_75',period)/10.00


class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_80(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 80% (Rigo RP48 col.6)"

    def formula(person,period,parameters):
        return person('spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_80',period)/10.00


class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_85(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 85% (Rigo RP48 col.7)"

    def formula(person,period,parameters):
        return person('spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_85',period)/10.00
