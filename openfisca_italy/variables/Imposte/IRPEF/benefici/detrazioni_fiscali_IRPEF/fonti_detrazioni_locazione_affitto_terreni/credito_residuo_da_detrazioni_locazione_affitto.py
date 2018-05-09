# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class credito_residuo_da_detrazioni_locazione_affitto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Credito residuo che non ha trovato capienza nell'imposta IRPEF in quanto l'ammontare delle detrazione da locazione e affitto erano maggiore dell'irpef lorda diminuita di detrazioni per lavoro e famiglia"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
            irpef_lorda = person('irpef_lorda',period)
            detrazioni_imposta_famiglia_lavoro = person('detrazioni_per_carichi_famigliari',period) + person('detrazione_per_lavoro',period)
            irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia =  irpef_lorda - detrazioni_imposta_famiglia_lavoro
            residuo_detrazione_startup = 0 # TODO
            capienza = irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia - residuo_detrazione_startup
            detrazione_canoni_di_locazione_e_affitto_terreni_annuo = person('detrazione_canoni_di_locazione_e_affitto_terreni_annuo',period)
            return select([capienza<=0,
                    capienza<detrazione_canoni_di_locazione_e_affitto_terreni_annuo,
                    capienza>=detrazione_canoni_di_locazione_e_affitto_terreni_annuo],
                    [detrazione_canoni_di_locazione_e_affitto_terreni_annuo,
                    detrazione_canoni_di_locazione_e_affitto_terreni_annuo-capienza,
                    0
                    ])


class detrazione_fruita_da_detrazioni_locazione_affitto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazione fruita nell'imposta IRPEF in quanto l'ammontare delle detrazione da locazione e affitto erano minori o uguali dell'irpef lorda diminuita di detrazioni per lavoro e famiglia"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
            irpef_lorda = person('irpef_lorda',period)
            detrazioni_imposta_famiglia_lavoro = person('detrazioni_per_carichi_famigliari',period) + person('detrazione_per_lavoro',period)
            irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia =  irpef_lorda - detrazioni_imposta_famiglia_lavoro
            residuo_detrazione_startup = 0 # TODO
            capienza = irpef_lorda_diminuita_delle_detrazioni_lavoro_e_famiglia - residuo_detrazione_startup
            detrazione_canoni_di_locazione_e_affitto_terreni_annuo = person('detrazione_canoni_di_locazione_e_affitto_terreni_annuo',period)
            return select([capienza<=0,
                    capienza<detrazione_canoni_di_locazione_e_affitto_terreni_annuo,
                    capienza>=detrazione_canoni_di_locazione_e_affitto_terreni_annuo],
                    [0,
                    detrazione_canoni_di_locazione_e_affitto_terreni_annuo - person('credito_residuo_da_detrazioni_locazione_affitto',period),
                    detrazione_canoni_di_locazione_e_affitto_terreni_annuo
                    ])
