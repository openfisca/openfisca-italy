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
        importo_totale = 0
        Righi_RP41_47_anni = ['RP41_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP42_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP43_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP44_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP45_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP46_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP47_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici']
        Righi_RP41_47_codici_2012_2013_2017_antisismico = ['RP41_codice_2012_2013_2017_antisismico','RP42_codice_2012_2013_2017_antisismico','RP43_codice_2012_2013_2017_antisismico','RP44_codice_2012_2013_2017_antisismico',
                                                    'RP45_codice_2012_2013_2017_antisismico','RP46_codice_2012_2013_2017_antisismico','RP47_codice_2012_2013_2017_antisismico']
        Righi_RP41_47_importi_rate = ['RP41_importo_rata','RP42_importo_rata','RP43_importo_rata','RP44_importo_rata','RP45_importo_rata','RP46_importo_rata','RP47_importo_rata']

        for anno_rigo, codice_rigo, importo_rata in zip(Righi_RP41_47_anni,Righi_RP41_47_codici_2012_2013_2017_antisismico,Righi_RP41_47_importi_rate):
            condizione_per_il_36 = (person(anno_rigo,period) == 2012) * (person(codice_rigo,period) == 3)
            importo_totale = where (condizione_per_il_36,(importo_totale + person(importo_rata,period)),importo_totale)
        return importo_totale


class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_50(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 50% (Rigo RP48 col.2)"

    def formula(person,period,parameters):
        importo_totale = 0
        Righi_RP41_47_anni = ['RP41_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP42_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP43_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP44_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP45_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP46_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP47_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici']
        Righi_RP41_47_codici_2012_2013_2017_antisismico = ['RP41_codice_2012_2013_2017_antisismico','RP42_codice_2012_2013_2017_antisismico','RP43_codice_2012_2013_2017_antisismico','RP44_codice_2012_2013_2017_antisismico',
                                                    'RP45_codice_2012_2013_2017_antisismico','RP46_codice_2012_2013_2017_antisismico','RP47_codice_2012_2013_2017_antisismico']
        Righi_RP41_47_importi_rate = ['RP41_importo_rata','RP42_importo_rata','RP43_importo_rata','RP44_importo_rata','RP45_importo_rata','RP46_importo_rata','RP47_importo_rata']

        for anno_rigo, codice_rigo, importo_rata in zip(Righi_RP41_47_anni,Righi_RP41_47_codici_2012_2013_2017_antisismico,Righi_RP41_47_importi_rate):
            condizione_per_il_50 = ((person(anno_rigo,period) == 2012) * (person(codice_rigo,period) == 4)) + ((person(anno_rigo,period) == 2017) * (person(codice_rigo,period) == 6))
            importo_totale = where (condizione_per_il_50,(importo_totale + person(importo_rata,period)),importo_totale)
        return importo_totale


class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_65(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 65% (Rigo RP48 col.3)"

    def formula(person,period,parameters):
        importo_totale = 0
        Righi_RP41_47_anni = ['RP41_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP42_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP43_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP44_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP45_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP46_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP47_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici']
        Righi_RP41_47_codici_2012_2013_2017_antisismico = ['RP41_codice_2012_2013_2017_antisismico','RP42_codice_2012_2013_2017_antisismico','RP43_codice_2012_2013_2017_antisismico','RP44_codice_2012_2013_2017_antisismico',
                                                    'RP45_codice_2012_2013_2017_antisismico','RP46_codice_2012_2013_2017_antisismico','RP47_codice_2012_2013_2017_antisismico']
        Righi_RP41_47_importi_rate = ['RP41_importo_rata','RP42_importo_rata','RP43_importo_rata','RP44_importo_rata','RP45_importo_rata','RP46_importo_rata','RP47_importo_rata']

        for anno_rigo, codice_rigo, importo_rata in zip(Righi_RP41_47_anni,Righi_RP41_47_codici_2012_2013_2017_antisismico,Righi_RP41_47_importi_rate):
            condizione_per_il_65 = ((person(anno_rigo,period) >= 2012) * (person(anno_rigo,period) <= 2016) * (person(codice_rigo,period) == 5))
            importo_totale = where (condizione_per_il_65,(importo_totale + person(importo_rata,period)),importo_totale)
        return importo_totale

class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_70(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 70% (Rigo RP48 col.4)"

    def formula(person,period,parameters):
        importo_totale = 0
        Righi_RP41_47_anni = ['RP41_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP42_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP43_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP44_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP45_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP46_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP47_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici']
        Righi_RP41_47_codici_2012_2013_2017_antisismico = ['RP41_codice_2012_2013_2017_antisismico','RP42_codice_2012_2013_2017_antisismico','RP43_codice_2012_2013_2017_antisismico','RP44_codice_2012_2013_2017_antisismico',
                                                    'RP45_codice_2012_2013_2017_antisismico','RP46_codice_2012_2013_2017_antisismico','RP47_codice_2012_2013_2017_antisismico']
        Righi_RP41_47_importi_rate = ['RP41_importo_rata','RP42_importo_rata','RP43_importo_rata','RP44_importo_rata','RP45_importo_rata','RP46_importo_rata','RP47_importo_rata']

        for anno_rigo, codice_rigo, importo_rata in zip(Righi_RP41_47_anni,Righi_RP41_47_codici_2012_2013_2017_antisismico,Righi_RP41_47_importi_rate):
            condizione_per_il_70 = ((person(anno_rigo,period) >= 2017) * (person(codice_rigo,period) == 8))
            importo_totale = where (condizione_per_il_70,(importo_totale + person(importo_rata,period)),importo_totale)
        return importo_totale

class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_75(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 75% (Rigo RP48 col.5)"

    def formula(person,period,parameters):
        importo_totale = 0
        Righi_RP41_47_anni = ['RP41_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP42_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP43_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP44_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP45_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP46_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP47_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici']
        Righi_RP41_47_codici_2012_2013_2017_antisismico = ['RP41_codice_2012_2013_2017_antisismico','RP42_codice_2012_2013_2017_antisismico','RP43_codice_2012_2013_2017_antisismico','RP44_codice_2012_2013_2017_antisismico',
                                                    'RP45_codice_2012_2013_2017_antisismico','RP46_codice_2012_2013_2017_antisismico','RP47_codice_2012_2013_2017_antisismico']
        Righi_RP41_47_importi_rate = ['RP41_importo_rata','RP42_importo_rata','RP43_importo_rata','RP44_importo_rata','RP45_importo_rata','RP46_importo_rata','RP47_importo_rata']

        for anno_rigo, codice_rigo, importo_rata in zip(Righi_RP41_47_anni,Righi_RP41_47_codici_2012_2013_2017_antisismico,Righi_RP41_47_importi_rate):
            condizione_per_il_75 = ((person(anno_rigo,period) == 2017) * (person(codice_rigo,period) == 0)) + ((person(anno_rigo,period) == 2017) * (person(codice_rigo,period) == 10))
            importo_totale = where (condizione_per_il_75,(importo_totale + person(importo_rata,period)),importo_totale)
        return importo_totale

class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_80(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 80% (Rigo RP48 col.6)"

    def formula(person,period,parameters):
        importo_totale = 0
        Righi_RP41_47_anni = ['RP41_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP42_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP43_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP44_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP45_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP46_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP47_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici']
        Righi_RP41_47_codici_2012_2013_2017_antisismico = ['RP41_codice_2012_2013_2017_antisismico','RP42_codice_2012_2013_2017_antisismico','RP43_codice_2012_2013_2017_antisismico','RP44_codice_2012_2013_2017_antisismico',
                                                    'RP45_codice_2012_2013_2017_antisismico','RP46_codice_2012_2013_2017_antisismico','RP47_codice_2012_2013_2017_antisismico']
        Righi_RP41_47_importi_rate = ['RP41_importo_rata','RP42_importo_rata','RP43_importo_rata','RP44_importo_rata','RP45_importo_rata','RP46_importo_rata','RP47_importo_rata']

        for anno_rigo, codice_rigo, importo_rata in zip(Righi_RP41_47_anni,Righi_RP41_47_codici_2012_2013_2017_antisismico,Righi_RP41_47_importi_rate):
            condizione_per_il_80 = ((person(anno_rigo,period) == 2017) * (person(codice_rigo,period) == 7))
            importo_totale = where (condizione_per_il_80,(importo_totale + person(importo_rata,period)),importo_totale)
        return importo_totale

class importo_rata_su_spese_per_interventi_recupero_patrimonio_edilizione_misure_antisismiche_soggette_a_detrazione_del_85(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rata per spese sezione III A con diritto di detrazione al 85% (Rigo RP48 col.7)"

    def formula(person,period,parameters):
        importo_totale = 0
        Righi_RP41_47_anni = ['RP41_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP42_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP43_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP44_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici',
            'RP45_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP46_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici','RP47_anno_in_cui_sono_state_sostenute_spese_per_recupero_patrimonio_edilizio_interventi_antisismici']
        Righi_RP41_47_codici_2012_2013_2017_antisismico = ['RP41_codice_2012_2013_2017_antisismico','RP42_codice_2012_2013_2017_antisismico','RP43_codice_2012_2013_2017_antisismico','RP44_codice_2012_2013_2017_antisismico',
                                                    'RP45_codice_2012_2013_2017_antisismico','RP46_codice_2012_2013_2017_antisismico','RP47_codice_2012_2013_2017_antisismico']
        Righi_RP41_47_importi_rate = ['RP41_importo_rata','RP42_importo_rata','RP43_importo_rata','RP44_importo_rata','RP45_importo_rata','RP46_importo_rata','RP47_importo_rata']

        for anno_rigo, codice_rigo, importo_rata in zip(Righi_RP41_47_anni,Righi_RP41_47_codici_2012_2013_2017_antisismico,Righi_RP41_47_importi_rate):
            condizione_per_il_90 = ((person(anno_rigo,period) == 2017) * (person(codice_rigo,period) == 2)) + ((person(anno_rigo,period) == 2017) * (person(codice_rigo,period) == 9))
            importo_totale = where (condizione_per_il_90,(importo_totale + person(importo_rata,period)),importo_totale)
        return importo_totale
