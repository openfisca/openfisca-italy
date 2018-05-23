# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
#import common
from openfisca_italy.variables.Imposte.IRPEF.Quadri_Oneri.Quadro_RP.Sezione_IV_common import *
# Import numpy
import numpy as np


# SEZIONE DELLE RATE

class RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_totale_annue(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rate per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP67-64 somma colonne 8)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_importo_rate_per_risparmio_energetico = ['RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_55',
                                                'RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_65',
                                                'RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_70',
                                                'RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_75',]
        return round_(sum(person(rata, period) for rata in tipi_importo_rate_per_risparmio_energetico),2)


class RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_55(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP 65 col.1 - riportare la somma degli importi indicati nei righi da RP61 a RP64 nei quali nella colonna 2 è stato indicato un anno precedente al 2013 ovvero è stato indicato l’anno 2013 con il codice “1” nella colonna 3"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        importo_rata_al_55 = 0
        codici_righi_anni_da_controllare = ['RP61_anno_sostenimento_spese_risparmio_energetico','RP62_anno_sostenimento_spese_risparmio_energetico',
        'RP63_anno_sostenimento_spese_risparmio_energetico','RP64_anno_sostenimento_spese_risparmio_energetico']
        codici_periodo_2013_da_controllare = ['RP61_periodo_2013','RP62_periodo_2013','RP63_periodo_2013','RP64_periodo_2013']
        importi_rata = ['RP61_importo_rata','RP62_importo_rata','RP63_importo_rata','RP64_importo_rata']
        for codice_anno, codice_periodo_2013 , importo_rata in zip(codici_righi_anni_da_controllare,codici_periodo_2013_da_controllare,importi_rata):
            condizione_vera = (person(codice_anno,period) < 2013) + ((person(codice_anno,period) == 2013) * (person(codice_periodo_2013,period) == TipiPeriodo2013FinalizzatiRisparmioEnergetico.codice_uno))
            importo_rata_al_55 = where (condizione_vera, importo_rata_al_55 + person(importo_rata,period) ,importo_rata_al_55)
        return importo_rata_al_55


class RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_65(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP 65 col.2 - riportare la somma degli importi indicati nei righi da RP61 a RP64 nei quali nella colonna 2 è stato indicato l’anno 2013 con il codice 2 nella colonna 3 ovvero è stato indicato l’anno 2014 o l’anno 2015 o l’anno 2016 ovvero l’anno 2017 con i codici 1, 2, 3, 4, 5, 6 o 7 nella colonna 1"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        importo_rata_al_65 = 0
        codici_righi_anni_da_controllare = ['RP61_anno_sostenimento_spese_risparmio_energetico','RP62_anno_sostenimento_spese_risparmio_energetico',
        'RP63_anno_sostenimento_spese_risparmio_energetico','RP64_anno_sostenimento_spese_risparmio_energetico']
        codici_periodo_2013_da_controllare = ['RP61_periodo_2013','RP62_periodo_2013','RP63_periodo_2013','RP64_periodo_2013']
        codice_tipo_intevento_da_controllare = ['RP61_tipo_intervento','RP62_tipo_intervento','RP63_tipo_intervento','RP64_tipo_intervento',]
        importi_rata = ['RP61_importo_rata','RP62_importo_rata','RP63_importo_rata','RP64_importo_rata']
        for codice_anno, codice_periodo_2013 , codice_tipo_intervento, importo_rata in zip(codici_righi_anni_da_controllare,codici_periodo_2013_da_controllare,codice_tipo_intevento_da_controllare,importi_rata):
            condizione_vera =   ((person(codice_anno,period) == 2014) +
                                (person(codice_anno,period) == 2015) +
                                (person(codice_anno,period) == 2016) +
                                ((person(codice_anno,period) == 2013) * (person(codice_periodo_2013,period) == TipiPeriodo2013FinalizzatiRisparmioEnergetico.codice_due)) +
                                ((person(codice_anno,period) == 2017) * (person(codice_tipo_intervento,period) == TipiInterventiFinalizzatiRisparmioEnergetico.codice_uno)) +
                                ((person(codice_anno,period) == 2017) * (person(codice_tipo_intervento,period) == TipiInterventiFinalizzatiRisparmioEnergetico.codice_due)) +
                                ((person(codice_anno,period) == 2017) * (person(codice_tipo_intervento,period) == TipiInterventiFinalizzatiRisparmioEnergetico.codice_tre)) +
                                ((person(codice_anno,period) == 2017) * (person(codice_tipo_intervento,period) == TipiInterventiFinalizzatiRisparmioEnergetico.codice_quattro)) +
                                ((person(codice_anno,period) == 2017) * (person(codice_tipo_intervento,period) == TipiInterventiFinalizzatiRisparmioEnergetico.codice_cinque)) +
                                ((person(codice_anno,period) == 2017) * (person(codice_tipo_intervento,period) == TipiInterventiFinalizzatiRisparmioEnergetico.codice_sei)) +
                                ((person(codice_anno,period) == 2017) * (person(codice_tipo_intervento,period) == TipiInterventiFinalizzatiRisparmioEnergetico.codice_sette)))
            importo_rata_al_65 = where (condizione_vera, importo_rata_al_65 + person(importo_rata,period) ,importo_rata_al_65)
        return importo_rata_al_65



class RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_70(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP 65 col.3 -  riportare la somma degli importi indicati nei righi da RP61 a RP64 nei quali nella colonna 2 è stato indicato l’anno 2017 con il codice 8 nella colonna 1."
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        importo_rata_al_70 = 0
        codici_righi_anni_da_controllare = ['RP61_anno_sostenimento_spese_risparmio_energetico','RP62_anno_sostenimento_spese_risparmio_energetico',
        'RP63_anno_sostenimento_spese_risparmio_energetico','RP64_anno_sostenimento_spese_risparmio_energetico']
        codice_tipo_intevento_da_controllare = ['RP61_tipo_intervento','RP62_tipo_intervento','RP63_tipo_intervento','RP64_tipo_intervento',]
        importi_rata = ['RP61_importo_rata','RP62_importo_rata','RP63_importo_rata','RP64_importo_rata']
        for codice_anno, codice_tipo_intervento, importo_rata in zip(codici_righi_anni_da_controllare,codice_tipo_intevento_da_controllare,importi_rata):
            condizione_vera = ((person(codice_anno,period) == 2017) * (person(codice_tipo_intervento,period) == TipiInterventiFinalizzatiRisparmioEnergetico.codice_otto))
            importo_rata_al_70 = where (condizione_vera, importo_rata_al_70 + person(importo_rata,period) ,importo_rata_al_70)
        return importo_rata_al_70


class RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_75(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"RP 65 col.3 - riportare la somma degli importi indicati nei righi da RP61 a RP64 nei quali nella colonna 2 è stato indicato l’anno 2017 con il codice 9 nella colonna 1."
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        importo_rata_al_75 = 0
        codici_righi_anni_da_controllare = ['RP61_anno_sostenimento_spese_risparmio_energetico','RP62_anno_sostenimento_spese_risparmio_energetico',
        'RP63_anno_sostenimento_spese_risparmio_energetico','RP64_anno_sostenimento_spese_risparmio_energetico']
        codice_tipo_intevento_da_controllare = ['RP61_tipo_intervento','RP62_tipo_intervento','RP63_tipo_intervento','RP64_tipo_intervento',]
        importi_rata = ['RP61_importo_rata','RP62_importo_rata','RP63_importo_rata','RP64_importo_rata']
        for codice_anno, codice_tipo_intervento, importo_rata in zip(codici_righi_anni_da_controllare,codice_tipo_intevento_da_controllare,importi_rata):
            condizione_vera = ((person(codice_anno,period) == 2017) * (person(codice_tipo_intervento,period) == TipiInterventiFinalizzatiRisparmioEnergetico.codice_nove))
            importo_rata_al_75 = where (condizione_vera, importo_rata_al_75 + person(importo_rata,period) ,importo_rata_al_75)
        return importo_rata_al_75
