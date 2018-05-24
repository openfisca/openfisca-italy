# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class RP66_detrazioni_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_55(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Detrazioni per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP66 col.detrazioni del 55%)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return round_((person('RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_55',period) * 0.55),2)


class RP66_detrazioni_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_65(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Detrazioni per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP66 col.detrazioni del 65%)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return round_((person('RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_65',period) * 0.65),2)


class RP66_detrazioni_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_70(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Detrazioni per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP66 col.detrazioni del 70%)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return round_((person('RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_70',period) * 0.70),2)


class RP66_detrazioni_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_75(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Detrazioni per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP66 col.detrazioni del 75%)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return round_((person('RP_65_importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_75',period) * 0.75),2)
