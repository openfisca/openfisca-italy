# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
#import numpy
import numpy as np

class oneri_deducibili_totali_mensili(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    label = "Oneri deducibili mensili da sottrarre al reddito lordo mensile per il calcolo dell'IRPEF"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(person, period, parameters):
        tipi_deduzione = ['contributi_previdenziali_assistenziali','assegni_periodo_coniuge','contributi_addetti_servizi_domestici_e_familiari',
        'erogazioni_istituzioni_religiose','spese_mediche_e_assistenza_disabili','contributi_previdenza_complementare']
        totale_oneri_deducibili_mensile = round_(sum(person(deduzione, period,options=[DIVIDE]) for deduzione in tipi_deduzione),2)
        return np.array(totale_oneri_deducibili_mensile)


class oneri_deducibili_totali_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Oneri deducibili annuali da sottrarre al reddito lordo annuale per il calcolo dell'IRPEF"
    reference = "http://www.aclimperia.it/documenti/la_dichiarazione_dei_redditi.pdf"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.
    def formula(person, period, parameters):
        tipi_deduzione = ['contributi_previdenziali_assistenziali','assegni_periodo_coniuge','contributi_addetti_servizi_domestici_e_familiari',
        'erogazioni_istituzioni_religiose','spese_mediche_e_assistenza_disabili','contributi_previdenza_complementare']
        totale_oneri_deducibili_mensile = round_(sum(person(deduzione, period) for deduzione in tipi_deduzione),2)
        return np.array(totale_oneri_deducibili_mensile)
