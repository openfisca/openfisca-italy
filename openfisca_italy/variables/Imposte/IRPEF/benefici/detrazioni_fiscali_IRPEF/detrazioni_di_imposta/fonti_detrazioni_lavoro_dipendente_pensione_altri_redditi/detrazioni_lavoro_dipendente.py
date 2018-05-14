# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# TO DO: regolamentare solo il reddito per lavori socialmente utili (codice 3)

class detrazioni_per_lavoro_dipendente(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni per lavoro dipendente"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameter):
        percepito_reddito_lavori_socialmente_utili = person('percepito_reddito_lavori_socialmente_utili',period)
        percepito_reddito_lavoro_frontaliere = person('percepito_reddito_lavoro_frontaliere',period)
        percepito_reddito_comune_campione_italia = person('percepito_reddito_comune_campione_italia',period)
        # income combination to return a correct result
        solo_reddito_frontalieri = percepito_reddito_lavoro_frontaliere * not_(percepito_reddito_lavori_socialmente_utili) * not_(percepito_reddito_lavoro_dipendente_indeterminato) * not_(percepito_reddito_lavoro_dipendente_determinato) * not_(percepito_reddito_comune_campione_italia)
        solo_reddito_comune_campione_italia = percepito_reddito_comune_campione_italia * not_(percepito_reddito_lavori_socialmente_utili) * not_(percepito_reddito_lavoro_dipendente_indeterminato) * not_(percepito_reddito_lavoro_dipendente_determinato)* not_(percepito_reddito_lavoro_frontaliere)
        solo_reddito_comune_campione_italia_e_frontalieri = percepito_reddito_lavoro_frontaliere * percepito_reddito_comune_campione_italia * not_(percepito_reddito_lavori_socialmente_utili) * not_(percepito_reddito_lavoro_dipendente_indeterminato) * not_(percepito_reddito_lavoro_dipendente_determinato)
        reddito_lavoro_dipendente_annuale = person('reddito_lavoro_dipendente_annuale',period)
        # reddito per detrazioni
        reddito_per_detrazioni = person('reddito_per_detrazioni',period)
        return select([solo_reddito_frontalieri==True * reddito_lavoro_dipendente_annuale <= parameter(period).imposte.IRPEF.detrazioni.detrazioni_lavoro_dipendente.soglia_per_detrazioni_lavoro_dip_frontaliero,
         solo_reddito_comune_campione_italia==True * reddito_lavoro_dipendente_annuale <= parameter(period).imposte.IRPEF.detrazioni.detrazioni_lavoro_dipendente.soglia_per_detrazioni_lavoro_dip_campione_italia,
         solo_reddito_comune_campione_italia_e_frontalieri * not_(reddito_lavoro_dipendente_annuale <= parameter(period).imposte.IRPEF.detrazioni.detrazioni_lavoro_dipendente.soglia_per_detrazioni_lavoro_dip_campione_italia) * not_(reddito_lavoro_dipendente_annuale<=parameter(period).imposte.IRPEF.detrazioni.detrazioni_lavoro_dipendente.soglia_per_detrazioni_lavoro_dip_frontaliero),
         reddito_per_detrazioni<=8000,
         reddito_per_detrazioni<=28000,
         reddito_per_detrazioni<=55000,
         reddito_per_detrazioni>55000,],[0,0,0,
         person('detrazioni_per_reddito_da_lavoro_dipendente_inferiore_8000',period),
         person('detrazioni_per_reddito_da_lavoro_dipendente_inferiore_28000',period),
         person('detrazioni_per_reddito_da_lavoro_dipendente_inferiore_55000',period),
         0])

# Vedere se redditi percepiti o no

class percepito_reddito_lavoro_dipendente_determinato(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha percepito reddito da lavoro dipendente con contratto a tempo determinato"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

class percepito_reddito_lavoro_dipendente_indeterminato(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha percepito reddito da lavoro dipendente con contratto a tempo indeterminato"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class percepito_reddito_lavori_socialmente_utili(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha percepito reddito da lavori socialmente utili"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class percepito_reddito_lavoro_frontaliere(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha percepito reddito da lavoro frontaliere"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class percepito_reddito_comune_campione_italia(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "La persona ha percepito reddito nel comune di Campion d'Italia"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source



# Detrazioni per scaglioni di reddito
# Non un parametro perchè cambia la formula

class detrazioni_per_reddito_da_lavoro_dipendente_inferiore_8000(Variable):
    value_type =  float
    entity = Persona
    definition_period = YEAR
    label = "Calcolo detrazioni per reddito da lavoro dipendente inferiore a 8000 euro"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameter):
        detrazione_spettante =  round_(((1880 * ((person('numero_giorni_lavoro_dipendente',period) / 365.00)))),2)
        percepito_reddito_lavoro_dipendente_determinato = person('percepito_reddito_lavoro_dipendente_determinato',period)
        percepito_reddito_lavoro_dipendente_indeterminato = person('percepito_reddito_lavoro_dipendente_indeterminato',period)
        return select([percepito_reddito_lavoro_dipendente_determinato * (detrazione_spettante<=1380), percepito_reddito_lavoro_dipendente_indeterminato * (detrazione_spettante<=690), percepito_reddito_lavoro_dipendente_indeterminato * percepito_reddito_lavoro_dipendente_determinato * (detrazione_spettante<=1380), detrazione_spettante>=1380],[1380,690,1380,detrazione_spettante])


class detrazioni_per_reddito_da_lavoro_dipendente_inferiore_28000(Variable):
    value_type =  float
    entity = Persona
    definition_period = YEAR
    label = "Calcolo detrazioni per reddito da lavoro dipendente inferiore a 28000 euro"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameter):
        quoziente = round_(((28000 -(person('reddito_per_detrazioni',period)))/20000),4)
        quoziente_valido = quoziente>0 * quoziente<1
        detrazione_spettante = round_(((978 + (902*quoziente)) * (person('numero_giorni_lavoro_dipendente',period) / 365.00)),2)
        return where (quoziente_valido,detrazione_spettante,0)


class detrazioni_per_reddito_da_lavoro_dipendente_inferiore_55000(Variable):

    value_type =  float
    entity = Persona
    definition_period = YEAR
    label = "Calcolo detrazioni per reddito da lavoro dipendente inferiore a 55000 euro"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameter):
        quoziente = round_(((55000 -(person('reddito_per_detrazioni',period)))/27000),4)
        quoziente_valido = quoziente>0 * quoziente<1
        detrazione_spettante = round_(((978.00 * quoziente) * (person('numero_giorni_lavoro_dipendente',period) / 365.00)),2)
        return where (quoziente_valido,detrazione_spettante,0)
