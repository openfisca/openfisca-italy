# -*- coding: utf-8 -*-
#https://www.amministrazionicomunali.it/imu/categorie_catastali.php
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class categoria_catastale(Enum):
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

class categoria_catastale(Variable):
    value_type = Enum
    possible_values = categoria_catastale
    default_value = categoria_catastale.A4  #default: Abitazione popolare
    entity = Immobile
    definition_period = YEAR
    label = u"E' l'indice ufficiale utilizzato in Italia per classificare i beni immobili, e determinarne le rendite"

class is_prima_casa(Variable):
    value_type = bool
    entity = Immobile
    definition_period = YEAR
    #set_input = set_input_divide_by_period
    label = "Se l'immobile è prima casa"
    reference = ""

class is_abitazione_principale(Variable):
    value_type = bool
    entity = Immobile
    definition_period = YEAR
    #set_input = set_input_divide_by_period
    label = "Se l'immobile è abitazione principale"
    reference = "http://www.normattiva.it/atto/caricaArticolo?art.progressivo=0&art.idArticolo=15&art.versione=22&art.codiceRedazionale=086U0917&art.dataPubblicazioneGazzetta=1986-12-31&atto.tipoProvvedimento=DECRETO%20DEL%20PRESIDENTE%20DELLA%20REPUBBLICA&art.idGruppo=1&art.idSottoArticolo1=10&art.idSottoArticolo=1&art.flagTipoArticolo=0#art"
