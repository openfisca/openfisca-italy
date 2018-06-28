# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


# possibili codici esistente (dal 9 al 42)
class CodiciAltreSpeseDetraibili(Enum):
    nessun_codice = u"Non c'e' stata nessuna altra spesa per questo rigo relativamente alle altre spese per detrazioni negli oneri deducibili"
    codice_9 = u"Interessi per mutui contratti nel 1997 per recupero edilizio"
    codice_10 = u"Interessi per mutui ipotecari per costruzione abitazione principale"
    codice_11 = u"Interessi per prestiti o mutui agrari"
    codice_12 = u"Spese per istruzione diverse da quelle universitarie"
    codice_13 = u"Spese per istruzione universitaria"
    codice_14 = u"Spese funebri"
    codice_15 = u"Spese per addetti all'assistenza personale"
    codice_16 = u"Spese per attivita' sportive per ragazzi"
    codice_17 = u"Spese per intermediazione immobiliare"
    codice_18 = u"Spese per canoni di locazione sostenute da studenti universitari fuori sede"
    codice_20 = u"Erogazioni liberali a favore delle popolazioni colpite da calamita' pubbliche o eventi straordinari"
    codice_21 = u"Erogazioni liberali alle societa' ed associazioni sportive dilettantistiche"
    codice_22 = u"Contributi associativi alle societa' di mutuo soccorso"
    codice_23 = u"Erogazioni liberali a favore delle associazioni di promozione sociale"
    codice_24 = u"Erogazioni liberali a favore della societa' di cultura Biennale di Venezia"
    codice_25 = u"Spese relative a beni soggetti a regime vincolistico"
    codice_26 = u"Erogazioni liberali per attivita' culturali ed artistiche"
    codice_27 = u"Erogazioni liberali a favore di enti operanti nello spettacolo"
    codice_28 = u"Erogazioni liberali a favore di fondazioni operanti nel settore musicale"
    codice_29 = u"Spese veterinarie"
    codice_30 = u"Spese sostenute per servizi di interpretariato dai soggetti ricosciuti sordi"
    codice_31 = u"Erogazioni liberali a favore degli istituti scolastici di ogni ordine e grado"
    codice_32 = u"Spese relative ai contributi versati per il riscatto degli anni di laurea dei familiari a carico"
    codice_33 = u"Spese per asili nido"
    codice_35 = u"Erogazioni liberali al fondo per l'ammortamento di titoli di Stato"
    codice_36 = u"Premi per assicurazioni sulla vita e contro gli infortuni"
    codice_38 = u"Premi per assicurazioni per tutela delle persone con disaibilita grave"
    codice_39 = u"Premi per assicurazioni per rischio di non autosufficienza"
    codice_41 = u"Erogazioni liberali a favore delle Onlus" # 26%
    codice_42 = u"Erogazioni liberali a favore dei partiti politici" # 26%
    codice_99= u"Altre spese detraibili"
