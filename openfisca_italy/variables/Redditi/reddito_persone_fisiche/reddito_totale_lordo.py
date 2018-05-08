# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
#import numpy
import numpy as np

class reddito_totale_lordo_mensile(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    label = "Reddito totale lordo della persona"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(person, period, parameters):
        tipi_reddito = ['reddito_lavoro_dipendente_e_assimilati_annuale','reddito_di_capitali_annuale',
        'reddito_fondiari_annuale','reddito_diversi_annuale','redditi_da_attivita_sportive_dilettantistiche']
        # TO DO Check if incomes are taxable or not
        totale_reddito_mensile = round_(sum(person(reddito, period,options=[DIVIDE]) for reddito in tipi_reddito),2)
        return np.array(totale_reddito_mensile)


class reddito_totale_lordo_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito totale lordo della persona"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.

    def formula(person, period, parameters):
        tipi_reddito = ['reddito_lavoro_dipendente_e_assimilati_annuale','reddito_di_capitali_annuale',
        'reddito_fondiari_annuale','reddito_diversi_annuale','redditi_da_attivita_sportive_dilettantistiche']
        # TO DO Check if incomes are taxable or not
        totale_reddito_annuale = round_(sum(person(reddito, period) for reddito in tipi_reddito),2) # get first two decimale
        return np.array(totale_reddito_annuale) #return converting in np.array becaues tests accept only this type
