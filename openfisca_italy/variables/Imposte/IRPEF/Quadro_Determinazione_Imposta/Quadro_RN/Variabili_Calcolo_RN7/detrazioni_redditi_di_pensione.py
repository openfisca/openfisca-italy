# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class detrazioni_per_pensionati(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni per i pensionati"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        # pensioni percepite
        percepita_pensione_normale = person('percepita_pensione_normale',period)
        percepita_pensione_residente_campione_italia = person('percepita_pensione_residente_campione_italia',period)
        percepito_pensione_favore_dei_superstiti_corrisposte_agli_orfani = person('percepito_pensione_favore_dei_superstiti_corrisposte_agli_orfani',period)
        # situations
        solo_pensione_normale =  not_(percepita_pensione_residente_campione_italia) * not_(percepito_pensione_favore_dei_superstiti_corrisposte_agli_orfani)
        solo_pensione_residente_campione_italia = not_(percepita_pensione_normale) * not_(percepito_pensione_favore_dei_superstiti_corrisposte_agli_orfani)
        solo_pensione_favore_dei_superstiti_corrisposte_agli_orfani = not_(percepita_pensione_normale) * not_(percepita_pensione_residente_campione_italia)
        percepite_pensioni_favore_dei_superstiti_corrisposte_agli_orfani_e_residente_campione_italia = percepita_pensione_residente_campione_italia * percepito_pensione_favore_dei_superstiti_corrisposte_agli_orfani

        # income
        reddito_totale_da_pensioni = person('reddito_totale_da_pensioni',period) # it's the sum of the three income tipologies
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        # parametri di esenzione
        soglia_per_esenzioni_detrazioni_pensioni_solo_campione_italia = parameters(period).imposte.IRPEF.QuadroRN.detrazioni_pensione.soglia_per_detrazione_esente_residenti_campioni_italia
        soglia_per_esenzioni_detrazioni_pensioni_solo_favore_dei_superstiti_corrisposte_agli_orfani = parameters(period).imposte.IRPEF.QuadroRN.detrazioni_pensione.soglia_per_detrazione_esente_a_favore_superstiti_corrisposte_agli_orfani
        soglia_per_esenzioni_detrazioni_pensioni_solo_campione_italia_e_favore_dei_superstiti_corrisposte_agli_orfani = soglia_per_esenzioni_detrazioni_pensioni_solo_campione_italia + soglia_per_esenzioni_detrazioni_pensioni_solo_favore_dei_superstiti_corrisposte_agli_orfani
        # Condizioni
        return select([solo_pensione_residente_campione_italia * (reddito_totale_da_pensioni <= soglia_per_esenzioni_detrazioni_pensioni_solo_campione_italia),
                        solo_pensione_favore_dei_superstiti_corrisposte_agli_orfani * (reddito_totale_da_pensioni <= soglia_per_esenzioni_detrazioni_pensioni_solo_favore_dei_superstiti_corrisposte_agli_orfani),
                        percepite_pensioni_favore_dei_superstiti_corrisposte_agli_orfani_e_residente_campione_italia * (reddito_totale_da_pensioni <= soglia_per_esenzioni_detrazioni_pensioni_solo_campione_italia_e_favore_dei_superstiti_corrisposte_agli_orfani),
                        reddito_per_detrazioni <=8000,
                        reddito_per_detrazioni <=28000,
                        reddito_per_detrazioni <=55000,
                        reddito_per_detrazioni >=55000],
                        [0,0,0,person('detrazioni_per_reddito_da_pensione_inferiore_8000',period),person('detrazioni_per_reddito_da_pensione_inferiore_28000',period),person('detrazioni_per_reddito_da_pensione_inferiore_55000',period),0])


# Tipi di pensione
class percepita_pensione_normale(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha percepito reddito da pensione in maniera normale"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class percepita_pensione_residente_campione_italia(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha percepito reddito da pensione nel comune Campione D'italia"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class percepito_pensione_favore_dei_superstiti_corrisposte_agli_orfani(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha percepito reddito da pensione in favore dei supersitit corrisposte agli orfani"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


# Tipi di redditi percepibili

class reddito_pensione_normale(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito nel comune di Campione d'Italia"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class reddito_pensione_residente_campione_italia(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito frontaliero"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class reddito_pensione_favore_dei_superstiti_corrisposte_agli_orfani(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = "Reddito lavori socialmente utile"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

# Detrazioni per scaglioni di reddito
# Non un è parametro perchè cambia la formula

class detrazioni_per_reddito_da_pensione_inferiore_8000(Variable):
    value_type =  float
    entity = Persona
    definition_period = YEAR
    label = "Calcolo detrazioni per reddito da lavoro dipendente inferiore a 8000 euro"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameter):
        detrazione_spettante =  round_(((1880 * ((person('giorni_in_cui_si_e_percepita_la_pensione',period) / 365.00)))),2)
        return where (detrazione_spettante>713,detrazione_spettante,713)


class detrazioni_per_reddito_da_pensione_inferiore_28000(Variable):
    value_type =  float
    entity = Persona
    definition_period = YEAR
    label = "Calcolo detrazioni per reddito da lavoro dipendente inferiore a 28000 euro"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameter):
        quoziente = round_(((15000 -(person('reddito_per_detrazioni',period)))/7000),4)
        quoziente_valido = quoziente>0 * quoziente<1
        detrazione_spettante = round_(((1297 + (583*quoziente)) * (person('giorni_in_cui_si_e_percepita_la_pensione',period) / 365.00)),2)
        return where (quoziente_valido,detrazione_spettante,0)


class detrazioni_per_reddito_da_pensione_inferiore_55000(Variable):

    value_type =  float
    entity = Persona
    definition_period = YEAR
    label = "Calcolo detrazioni per reddito da lavoro dipendente inferiore a 55000 euro"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameter):
        quoziente = round_(((55000 -(person('reddito_per_detrazioni',period)))/40000),4)
        quoziente_valido = quoziente>0 * quoziente<1
        detrazione_spettante = round_(((1297.00 * quoziente) * (person('giorni_in_cui_si_e_percepita_la_pensione',period) / 365.00)),2)
        return where (quoziente_valido,detrazione_spettante,0)
