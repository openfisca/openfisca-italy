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

    #Not implemented for E and F because they are real estate of State.
    def formula(person, period, parameters):
        immobile_categoria_catastale_temp = person('immobile_categoria_catastale',period)
        c1               =  immobile_categoria_catastale_temp == CategoriaCatastale.C1

        d1_10_tranne_d5  =  immobile_categoria_catastale_temp == CategoriaCatastale.D1 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D2 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D3 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D4 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D6 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D7 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D8 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D9 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D10

        a10_d5           =  immobile_categoria_catastale_temp == CategoriaCatastale.A10 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.D5

        c3_c4_c5_b       =  immobile_categoria_catastale_temp == CategoriaCatastale.C3 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.C4 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.C5 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B1 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B2 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B3 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B4 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B5 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B6 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B7 +
                            immobile_categoria_catastale_temp == CategoriaCatastale.B8

        c2_c6_c7_a1_9    =  immobile_categoria_catastale_temp == CategoriaCatastale.C2 +
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

        terreno_cd_iap    = (person('is_immobile_posseduto_da_CD',period) + person('is_immobile_posseduto_da_IAP',period)) * immobile_categoria_catastale_temp == CategoriaCatastale.T
        terreno_normale   = not_(person('is_immobile_posseduto_da_CD',period) + person('is_immobile_posseduto_da_IAP',period)) * immobile_categoria_catastale_temp == CategoriaCatastale.T
        return select(  [   c1,
                            d1_10_tranne_d5,
                            a10_d5,
                            c3_c4_c5_b,
                            c2_c6_c7_a1_9,
                            terreno_cd_iap,
                            terreno_normale

                        ],
                        [
                            55,
                            65,
                            80,
                            140,
                            160,
                            110,
                            135
                        ])

class is_destinazione_ad_usi_culturali(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Immobile con destinazione ad usi culturali?"
    reference = u"art. 5-bis del D.P.R. 29 settembre 1973, n. 601"

class is_destinazione_ad_uso_di_culto(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Immobile con destinazione ad usi di culto?"
    reference = u"artt. 8 e 19 della Costituzione"

class is_proprieta_santa_sede(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Immobile appartentente alla Santa Sede?"
    reference = u"artt. 13, 14, 15 e 16 del Trattato lateranense, sottoscritto l’11 febbraio 1929 e reso esecutivo con legge 27 maggio 1929, n. 810"

#i fabbricati appartenenti agli Stati esteri e alle organizzazioni internazionali
#per i quali è prevista l’esenzione dall’imposta locale sul reddito dei fabbricati
#in base ad accordi internazionali resi esecutivi in Italia
class is_svolgimento_attivita_non_commerciali_di_un_determinato_tipo(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Immobile con destinazione: attività assistenziali, previdenziali, sanitarie, didattiche, ricettive, culturali, ricreative e sportive"
    reference = u"art. 16, lett. a), della legge 20 maggio 1985, n. 222 e all’art. 73, comma 1, lett. c), del TUIR"

class is_fabbricati_rurali_ad_uso_strumentale_in_comuni_montani(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Immobile ubicati nei comuni classificati montani o parzialmente montani di cui all’elenco dei comuni italiani predisposto dall’ISTAT"
    reference = u"all’art. 9, comma 3-bis, del D. L. n. 557 del 1993, lista comuni esenti: https://www.istat.it/it/archivio/6789"




#Terreni (anche non coltivati) posseduti da coltivatori diretti (CD)
class is_immobile_posseduto_da_CD(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"L'immobile è posseduto da un coltivatore diretto?"
    reference = u""
#Terreni (anche non coltivati) posseduti da imprenditori agricoli professionali iscritti nella previdenza agricola (IAP)
class is_immobile_posseduto_da_IAP(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"L'immobile è posseduto da un imprenditore agricolo professionale?"
    reference = u""

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
        is_scontato_50_percento = where(    person('is_interesse_storico_artistico',period)+
                                            person('is_inagibile_accertato',period),
                                            True,False)
        is_scontato_25_percento = where(    person('is_canone_concordato',period),
                                            True,False)
        is_scontato_75_percento = where(    is_scontato_25_percento*is_scontato_50_percento,
                                            True,False)
        other_case = not_(is_scontato_25_percento)+not_(is_scontato_50_percento)+not_(is_scontato_75_percento)
        base_imponibile = person('valore_immobile_rivalutato',period) * person('moltiplicatori_catastali',period)
        return select(  [
                            is_scontato_25_percento,
                            is_scontato_50_percento,
                            is_scontato_75_percento,
                            other_case
                        ],[
                            base_imponibile-(base_imponibile*25/100),
                            base_imponibile-(base_imponibile*50/100),
                            base_imponibile-(base_imponibile*75/100),
                            base_imponibile
                        ])

                        class X(Variable):
                            blablalba

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

class is_canone_concordato(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    #set_input = set_input_divide_by_period
    label = u"Se l'immobile è in canone concordato"
    reference = u"commi 53 e 54 dell’articolo 1 della legge 208/2015, definiti dalla legge 431 del 1998"

class is_comodato_uso_gratuito_genitori_figli(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    #set_input = set_input_divide_by_period
    label = u"Se l'immobile è in comodato d'uso gratuito genitori-figli"
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

class is_inagibile_accertato(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Se l'immobile è inagibile"
    reference = u"Decreto del presidente della Repubblica 28 dicembre 2000, n. 445"

class is_interesse_storico_artistico(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Se l'immobile ha un interesse storico/artistico"
    reference = u"Decreto del presidente della Repubblica 28 dicembre 2000, n. 445"

class aliquota_imu(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Aliquota IMU che cambia a seconda della categoria"

    def formula(person, period, parameters):
        immobile_categoria_catastale_temp = person('immobile_categoria_catastale',period)
        a1_a8_a9 =
                        immobile_categoria_catastale_temp == CategoriaCatastale.A1+
                        immobile_categoria_catastale_temp == CategoriaCatastale.A8+
                        immobile_categoria_catastale_temp == CategoriaCatastale.A9
        other_case = not_(a1_a8_a9)
        #A1,A8,A9 hanno l'aliquota del 4 per mille
        return select(
                            [a1_a8_a9,  other_case  ]
                            ,
                            [(4/1000),  (7.6/1000)  ]
                    )
class imposta_imu(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Imposta IMU, risultato della moltiplicazione tra la base imponibile e l'aliquota imu"

    def formula(person, period, parameters):
        is_esenti = where(  person('is_destinazione_ad_uso_di_culto',period)+
                            person('is_destinazione_ad_usi_culturali',period)+
                            person('is_proprieta_santa_sede',period)+
                            person('is_svolgimento_attivita_non_commerciali_di_un_determinato_tipo',period)+
                            person('is_fabbricati_rurali_ad_uso_strumentale_in_comuni_montani',period)
                        ,True,False)
        other_case = not_(is_esenti)
        return select([is_esenti,other_case],[0,person('base_imponibile',period) * person('aliquota_imu',period)])

class importo_imu(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Importo IMU, la differenza tra l'imposta imu e le detrazioni"

    def formula(person, period, parameters):
        is_esenti = where(  person('is_destinazione_ad_uso_di_culto',period)+
                            person('is_destinazione_ad_usi_culturali',period)+
                            person('is_proprieta_santa_sede',period)+
                            person('is_svolgimento_attivita_non_commerciali_di_un_determinato_tipo',period)+
                            person('is_fabbricati_rurali_ad_uso_strumentale_in_comuni_montani',period)
                        ,True,False)
        #se è esente ritorna 0 altrimenti calcola il risultato
        return where(is_esenti,0,person('base_imponibile',period) * person('aliquota_imu',period))


class detrazioni_imu(Variable):
    value_type = float
    entity = Persona
    definition_period = MONTH
    set_input = set_input_divide_by_period
    label = u"Detrazioni applicate all'imposta imu"

    def formula(person, period, parameters):
        immobile_categoria_catastale_temp = person('immobile_categoria_catastale',period)

        is_esenti = where(  person('is_destinazione_ad_uso_di_culto',period)+
                            person('is_destinazione_ad_usi_culturali',period)+
                            person('is_proprieta_santa_sede',period)+
                            person('is_svolgimento_attivita_non_commerciali_di_un_determinato_tipo',period)+
                            person('is_fabbricati_rurali_ad_uso_strumentale_in_comuni_montani',period)
                        ,True,False)
        a1_a8_a9_case = immobile_categoria_catastale_temp == CategoriaCatastale.A1+
                        immobile_categoria_catastale_temp == CategoriaCatastale.A8+
                        immobile_categoria_catastale_temp == CategoriaCatastale.A9
        other_case = not_(a1_a2_a9_case)+not_(is_esenti)
        return select( [
                            is_esenti,
                            a1_a8_a9_case,
                            other_case
                        ],
                        [
                            0,
                            200,    #A1,A8,A9 hanno una detrazione fissa di 200 euro
                            0
                        ])
