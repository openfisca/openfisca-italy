# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class TipiInterventiFinalizzatiRisparmioEnergetico(Enum):
    nessun_codice = "Non è stato compilato nessun codice per il RIGO RP61 col.1"
    codice_uno = "Interventi di riqualificazione energetica di edifici esistenti"
    codice_due = "Interventi sull’involucro degli edifici esistenti"
    codice_tre = "Installazione di pannelli solari"
    codice_quattro = "Sostituzione di impianti di climatizzazione invernale"
    codice_cinque = "Acquisto e posa in opera di schermature solari"
    codice_sei = "Acquisto e posa in opera di impianti di climatizzazione invernale a biomasse"
    codice_sette = "Acquisto, installazione e messa in opera di dispositivi multimediali per controllo da remoto"
    codice_otto = "Interventi sull’involucro di parti comuni degli edifici condominiali esistenti"
    codice_nove = " Interventi di riqualificazione energetica di parti comuni degli edifici condominiali esistenti"


class TipiPeriodo2013FinalizzatiRisparmioEnergetico(Enum):
    nessun_codice = "Non è stato compilato nessun codice per il RIGO RP61 col.3"
    codice_uno = "Spese sostenute dal 1° gennaio al 5 giugno 2013 (detrazione del 55%)"
    codice_due = "Spese sostenute dal 6 giugno al 31 dicembre 2013 (detrazione del 65%)"


class TipiCasiParticolariFinalizzatiRisparmioEnergetico(Enum):
    nessun_codice = "Non è stato compilato nessun codice per il RIGO RP61 col.3"
    codice_uno = "Nel caso di spese sostenute per lavori iniziati in anni precedenti e ancora in corso nel 2017"
    codice_due = "Nel caso in cui le spese sostenute in anni precedenti al 2017 riguardino un immobile ereditato, acquistato o ricevuto in donazione nell’anno 2017"
    codice_tre = "Se ricorrono contemporaneamente le condizioni di cui ai codici 1 e 2 (lavori che proseguono in più anni ed immobile ereditato, acquistato o ricevuto in donazione)"


class RangeSpesaDate(Enum):
    nessun_codice = "Non e' stata inserita alcuna spesa"
    codice_uno = "spese sostenute fino al 5 giugno 2013 (55%)"
    codice_due = "spese sostenute dal 6 giugno 2013 al 31 dicembre 2017 (65%)"
    codice_tre = "Spese sostenute dal 1 gennaio al 31 dicembre 2017"
