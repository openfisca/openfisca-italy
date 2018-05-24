# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class is_destinazione_ad_usi_culturali(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Immobile con destinazione ad usi culturali?"
    reference = u"http://def.finanze.it/DocTribFrontend/getAttoNormativoDetail.do?ACTION=getArticolo&id={A2AB2374-12D3-47AC-9140-D8ACDB7869A9}&codiceOrdinamento=200000500000200&articolo=Articolo%205%20bis"

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
    reference = u"artt. 13, 14, 15 e 16 del Trattato lateranense (http://www.vatican.va/roman_curia/secretariat_state/archivio/documents/rc_seg-st_19290211_patti-lateranensi_it.html)"

#attività assistenziali, previdenziali,
#sanitarie, didattiche, ricettive, culturali, ricreative e sportive,
#nonché delle attività di religione o culto
class is_svolgimento_attivita_non_commerciali_di_un_determinato_tipo(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Immobile con destinazione: attività assistenziali, previdenziali, sanitarie, didattiche, ricettive, culturali, ricreative e sportive"
    reference = u"""http://def.finanze.it/DocTribFrontend/getAttoNormativoDetail.do?ACTION=getArticolo&id={69CB1D0C-B4B3-404C-8070-891C73712B82}&codiceOrdinamento=200001600000000&articolo=Articolo%2016
                        e
                    http://www.altalex.com/documents/leggi/2014/07/17/tuir-titolo-ii-capo-i-soggetti-passivi-e-disposizioni-generali#61906"
                    """
class is_immobile_rurale_ad_uso_strumentale_in_comune_montano(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Immobile ubicati nei comuni classificati montani o parzialmente montani di cui all’elenco dei comuni italiani predisposto dall’ISTAT"
    reference = u"""all’art. 9, comma 3-bis, del http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/FabbricatiTerreni/Fabbricati+rurali/Normativa+e+prassi+fabbricati+rurali/Articolo+9+Dl+30121993+n557/art_9_dl_557_1993.pdf
                    lista comuni esenti: https://www.istat.it/it/archivio/6789"""

class is_immobile_merce(Variable):  #magazzino
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Fabbricati costruiti e destinati dall’impresa costruttrice alla vendita, fintanto che permanga tale destinazione e non siano in ogni caso locati "
    reference = u"http://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.progressivo=0&art.idArticolo=2&art.versione=1&art.codiceRedazionale=13G00145&art.dataPubblicazioneGazzetta=2013-08-31&art.idGruppo=1&art.idSottoArticolo1=10&art.idSottoArticolo=1&art.flagTipoArticolo=0#art"


#Terreni (anche non coltivati) posseduti da coltivatori diretti (CD)
class is_immobile_posseduto_da_CD(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"L'immobile è posseduto da un coltivatore diretto?"
    reference = u"https://www.brocardi.it/codice-civile/libro-quinto/titolo-ii/capo-ii/sezione-i/art2135.html"
#Terreni (anche non coltivati) posseduti da imprenditori agricoli professionali iscritti nella previdenza agricola (IAP)
class is_immobile_posseduto_da_IAP(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"L'immobile è posseduto da un imprenditore agricolo professionale?"
    reference = u"https://www.brocardi.it/codice-civile/libro-quinto/titolo-ii/capo-ii/sezione-i/art2135.html"



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
    reference = u"Commi 53-54: http://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.progressivo=1&art.idArticolo=1&art.versione=1&art.codiceRedazionale=15G00222&art.dataPubblicazioneGazzetta=2015-12-30&art.idGruppo=0&art.idSottoArticolo1=10&art.idSottoArticolo=1&art.flagTipoArticolo=0#art"

class is_comodato_uso_gratuito_genitori_figli(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    #set_input = set_input_divide_by_period
    label = u"Se l'immobile è in comodato d'uso gratuito genitori-figli"
    reference = u"https://www.brocardi.it/codice-civile/libro-quarto/titolo-iii/capo-xiv/art1803.html"

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
    reference = u"Categorie A1 A8 A9"
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
    reference = u"http://www.finanze.it/export/sites/finanze/it/.content/Documenti/Varie/Risoluzione_n._9-2015_cooperative_edilizie_-_imprese_costruttrici_-_Natura_assegnazione._Sito.pdf"

class is_immobile_destinato_ad_alloggi_sociali(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Se l'immobile è destinato ad alloggi sociali"
    reference = u"http://www.finanze.it/export/sites/finanze/it/.content/Documenti/Varie/Domande_Sole_24_Ore-definitivo-H-20-22a.pdf"

class is_inagibile_accertato(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Se l'immobile è inagibile"
    reference = u"http://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.progressivo=0&art.idArticolo=3&art.versione=1&art.codiceRedazionale=011G0247&art.dataPubblicazioneGazzetta=2011-12-06&art.idGruppo=1&art.idSottoArticolo1=10&art.idSottoArticolo=1&art.flagTipoArticolo=0#art"

#c'è semplicemente da fare: RenditaCatastaleNonRivalutata*Imu
class is_area_fabbricabile(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Se l'area è fabbricabile"
    reference = u"Art 36 comma 2: http://www.camera.it/parlam/leggi/decreti/06223d.htm"


class is_interesse_storico_artistico(Variable):
    value_type = bool
    entity = Persona
    default_value = False
    definition_period = MONTH
    label = u"Se l'immobile ha un interesse storico/artistico"
    reference = u"http://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.progressivo=0&art.idArticolo=10&art.versione=1&art.codiceRedazionale=004G0066&art.dataPubblicazioneGazzetta=2004-02-24&art.idGruppo=2&art.idSottoArticolo1=10&art.idSottoArticolo=1&art.flagTipoArticolo=0#art"
