# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# Se l’ammontare complessivo delle detrazioni spettanti è superiore all’imposta lorda diminuita delle detrazioni per carichi di famiglia e
# delle detrazioni per redditi di lavoro dipendente ed assimilati, di pensione e/o altri redditi, è riconosciuto un ammontare pari alla quota di
# detrazione che non ha trovato capienza nella predetta imposta.


class totale_detrazione_lavoro_annuo (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione per lavoro totale"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        tipi_detrazioni_lavoro = ['detrazioni_per_lavoro_dipendente','detrazione_per_redditi_assimilati_a_lavoro_dipendente_e_altri_redditi',
        'detrazioni_per_pensionati']
        return round_(sum(person(detrazione, period) for detrazione in tipi_detrazioni_lavoro),2)
