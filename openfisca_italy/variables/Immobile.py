# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

#https://www.amministrazionicomunali.it/imu/categorie_catastali.php
class CategoriaCatastale(Enum):
    #I - IMMOBILI A DESTINAZIONE ORDINARIA - Gruppo A - B - C
    A1 = u'Abitazioni di tipo signorile'
    A2 = u'Abitazioni di tipo civile'
    A3 = u'Abitazioni di tipo economico'
    A4 = u'Abitazioni di tipo popolare'
    A5 = u'Abitazioni di tipo ultrapopolare'
    A6 = u'Abitazioni di tipo rurale'
    A7 = u'Abitazioni in villini'
    A8 = u'Abitazioni in ville'
    A9 = u'Castelli, palazzi di eminenti pregi artistici o storici'
    A10 = u'Uffici e studi privati'
    A11 = u'Abitazioni ed alloggi tipici dei luoghi'
    B1 = u'Collegi e convitti, educandati; ricoveri; orfanotrofi; ospizi; conventi; seminari; caserme'
    B2 = u'Case di cura ed ospedali (senza fine di lucro)'
    B3 = u'Prigioni e riformatori'
    B4 = u'Uffici pubblici'
    B5 = u'Scuole e laboratori scientifici'
    B6 = u'Biblioteche, pinacoteche, musei, gallerie, accademie che non hanno sede in edifici della categoria A9'
    B7 = u'Cappelle ed oratori non destinati all’esercizio pubblico del culto'
    B8 = u'Magazzini sotterranei per depositi di derrate'
    C1 = u'Negozi e botteghe'
    C2 = u'Magazzini e locali di deposito'
    C3 = u'Laboratori per arti e mestieri'
    C4 = u'Fabbricati e locali per esercizi sportivi (senza fine di lucro)'
    C5 = u'Stabilimenti balneari e di acque curative (senza fine di lucro)'
    C6 = u'Stalle, scuderie, rimesse, autorimesse (senza fine di lucro)'
    C7 = u'Tettoie chiuse od aperte'
    #II - IMMOBILI A DESTINAZIONE SPECIALE - Gruppo D
    D1 = u'Opifici'
    D2 = u'Alberghi e pensioni (con fine di lucro)'
    D3 = u'Teatri, cinematografi, sale per concerti e spettacoli e simili (con fine di lucro)'
    D4 = u'Case di cura ed ospedali (con fine di lucro)'
    D5 = u'Istituto di credito, cambio e assicurazione (con fine di lucro)'
    D6 = u'Fabbricati e locali per esercizi sportivi (con fine di lucro)'
    D7 = u'Fabbricati costruiti o adattati per le speciali esigenze di un attivita industriale e non suscettibili di destinazione diversa senza radicali trasformazioni.'
    D8 = u'Fabbricati costruiti o adattati per le speciali esigenze di un attivita commerciale e non suscettibili di destinazione diversa senza radicali trasformazioni.'
    D9 = u'Edifici galleggianti o sospesi assicurati a punti fissi del suolo, ponti privati soggetti a pedaggio.'
    D10 = u'Fabbricati per funzioni produttive connesse alle attivita agricole.'
    #III - IMMOBILI A DESTINAZIONE PARTICOLARE - Gruppo E
    E1 = u'Stazioni per servizi di trasporto, terrestri, marittimi ed aerei.'
    E2 = u'Ponti comunali e provinciali soggetti a pedaggio'
    E3 = u'Costruzioni e fabbricati per speciali esigenze pubbliche'
    E4 = u'Recinti chiusi per speciali esigenze pubbliche.'
    E5 = u'Fabbricati costituenti fortificazioni e loro dipendenze.'
    E6 = u'Fari, semafori, torri per rendere d’uso pubblico l’orologio comunale'
    E7 = u'Fabbricati destinati all’esercizio pubblico dei culti.'
    E8 = u'Fabbricati e costruzioni nei cimiteri, esclusi i colombari, i sepolcri e le tombe di famiglia.'
    E9 = u'Edifici a destinazione particolare non compresi nelle categorie precedenti del gruppo E.'
    #IV – ENTITA’ URBANE - Gruppo F
    F1 = u'Area urbana'
    F2 = u'Unità collabenti'
    F3 = u'Unità in corso di costruzione'
    F4 = u'Unità in corso di definizione'
    F5 = u'Lastrico solare'
    F6 = u'Fabbricato in attesa di dichiarazione (circolare 1/2009)'
    T = u'Terreni Agricoli'

class moltiplicatori_catastali(Variable):
    value_type = int
    entity = Persona
    definition_period = ETERNITY
    label = u""
    reference = u""

    def formula(person, period, parameters):
        immobile_categoria_catastale_temp = person('immobile_categoria_catastale',period)
        return select(  [   immobile_categoria_catastale_temp == CategoriaCatastale.C1,         #1
                            immobile_categoria_catastale_temp == CategoriaCatastale.D1 +        #2
                            immobile_categoria_catastale_temp == CategoriaCatastale.D2 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D3 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D4 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D6 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D7 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D8 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D9 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D10,
                            immobile_categoria_catastale_temp == CategoriaCatastale.A10 +       #3
                            immobile_categoria_catastale_temp == CategoriaCatastale.D5,
                            immobile_categoria_catastale_temp == CategoriaCatastale.C3 +        #4
                            immobile_categoria_catastale_temp == CategoriaCatastale.C4 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.C5 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B1 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B2 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B3 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B4 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B5 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B6 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B7 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B8,         #5
                            immobile_categoria_catastale_temp == CategoriaCatastale.C2 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.C6 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.C7 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.A1 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.A2 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.A3 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.A4 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.A5 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.A6 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.A7 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.A8 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.A9
                        ],
                        [
                            55,                                                                 #1
                            65,                                                                 #2
                            80,                                                                 #3
                            140,                                                                #4
                            160                                                                 #5
                        ])


class valore_immobile_non_rivalutato(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Valore dell'immobile non rivalutato"


class valore_immobile_rivalutato(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Valore dell'immobile rivalutato"
    def formula(person, period, parameters):
        coefficiente = 0
        immobile_categoria_catastale_temp = person('immobile_categoria_catastale',period)
        coefficiente = where(immobile_categoria_catastale_temp == CategoriaCatastale.T,1.25,1.05)
        #valore del mobile non rivalutato
        return person('valore_immobile_non_rivalutato',period) * coefficiente


class base_imponibile(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Base imponibile dell'immobile"

    def formula(person, period, parameters):
        return person('valore_immobile_rivalutato',period) * person('moltiplicatori_catastali',period)


class immobile_categoria_catastale(Variable):
    value_type = Enum
    possible_values = CategoriaCatastale
    default_value = CategoriaCatastale.A4  #default: Abitazione popolare
    entity = Persona
    definition_period = MONTH
    label = u"E' l'indice ufficiale utilizzato in Italia per classificare i beni immobili, e determinarne le rendite"

class is_immobile_prima_casa(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    #set_input = set_input_divide_by_period
    label = u"Se l'immobile è prima casa"
    reference = u""

class is_immobile_abitazione_principale(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    #set_input = set_input_divide_by_period
    label = u"Se l'immobile è abitazione principale"
    reference = u"http://www.normattiva.it/atto/caricaArticolo?art.progressivo=0&art.idArticolo=15&art.versione=22&art.codiceRedazionale=086U0917&art.dataPubblicazioneGazzetta=1986-12-31&atto.tipoProvvedimento=DECRETO%20DEL%20PRESIDENTE%20DELLA%20REPUBBLICA&art.idGruppo=1&art.idSottoArticolo1=10&art.idSottoArticolo=1&art.flagTipoArticolo=0#art"

class is_immobile_casa_di_lusso(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Se l'immobile è una casa di lusso"
    reference = u""
    #an "immobile" is categorized as "lusso" if entered in category A1 or A8 or A9
    def formula(person, period, parameters):
        is_lusso = person('immobile_categoria_catastale',period)
        return where(is_lusso == CategoriaCatastale.A1 + is_lusso == CategoriaCatastale.A8 + is_lusso == CategoriaCatastale.A9,True,False)

class is_immobile_appartenente_cooperativa_edilizia(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Se l'immobile appartiene a cooperative edilizie a proprietà indivisa, adibite ad abitazione principale e relative pertinenze dei soci assegnatari"
    reference = u""

class is_immobile_destinato_ad_alloggi_sociali(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Se l'immobile è destinato ad alloggi sociali"
    reference = u""
