# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class TipiTerreniUrbani(Enum):
    nessun_codice = "Nessun codice inserito"
    codice_T = "Immobile è censito nel catasto terreni"
    codice_U = "Immobile è censito nel catasto edilizio urbano"
