# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class reddito_totale_lordo_mensile(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    label = "Reddito totale lordo della persona"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.
   
    def formula(person, period, parameters):
        tipi_reddito = ['reddito_lavoro_dipendente_annuale','reddito_lavoro_autonomo_annuale','reddito_fabbricati_annuale','reddito_terreni_annuale','reddito_di_impresa_annuale']
        # TO DO Check if incomes are taxable or not
        totale_reddito_mensile = sum(person(reddito, period,options=[DIVIDE]) for reddito in tipi_reddito)
        return totale_reddito_mensile


class reddito_totale_lordo_annuale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito totale lordo della persona"
    reference = "https://stats.gov.example/disposable_income"  # Some variables represent quantities used in economic models, and not defined by law. Always give the source of your definition.
   
    def formula(person, period, parameters):
        tipi_reddito = ['reddito_lavoro_dipendente_annuale','reddito_lavoro_autonomo_annuale','reddito_fabbricati_annuale','reddito_terreni_annuale','reddito_di_impresa_annuale']
        # TO DO Check if incomes are taxable or not
        totale_reddito_annuale = sum(person(reddito, period) for reddito in tipi_reddito)
        return totale_reddito_annuale