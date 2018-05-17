# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np


# SEZIONE DELLE RATE

class importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_totale_annue(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rate per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP67-64 somma colonne 8)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_importo_rate_per_risparmio_energetico = ['importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_55',
                                                'importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_65',
                                                'importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_70',
                                                'importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_75',]
        return round_(sum(person(rata, period) for rata in tipi_importo_rate_per_risparmio_energetico),2)


class importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_55(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rate per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP67-64 somma colonne 8 delle spese da detrarre per il 55%)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('spesa_per_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_55',period) / 10.0


class importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_65(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rate per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP67-64 somma colonne 8 delle spese da detrarre per il 65%)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('spesa_per_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_65',period) / 10.0


class importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_70(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rate per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP67-64 somma colonne 8 delle spese da detrarre per il 70%)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('spesa_per_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_70',period) / 10.0

class importo_rate_per_spese_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_75(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo rate per spese indicate nella sezione IV del Quadro RP (Spese per inteventi finalizzati al risparmio energetico) (Rigo RP67-64 somma colonne 8 delle spese da detrarre per il 75%)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source

    def formula(person,period,parameters):
        return person('spesa_per_interventi_finalizzati_al_risparmio_energetico_da_detrarre_per_il_75',period) / 10.0
