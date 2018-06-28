# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# questi codici servono per calcolare gli importi dei righi RP28 ed RP29
class TipiCodiciCampo411ModelloUnico(Enum):
     nessun_codice = u"Nessun codice inserito"
     codice_uno = u"Inserito codice uno"
     codice_due = u"Inserito codice due"
     codice_tre = u"Inserito codice tre"
     codice_quattro = u"Inserito codice quattro"
     codice_cinque = u"Inserito codice cinque"
