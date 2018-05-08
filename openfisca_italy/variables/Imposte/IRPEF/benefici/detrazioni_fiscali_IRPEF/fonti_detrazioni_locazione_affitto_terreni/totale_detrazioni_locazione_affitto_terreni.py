# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# Se l’ammontare complessivo delle detrazioni spettanti è superiore all’imposta lorda diminuita delle detrazioni per carichi di famiglia e
# delle detrazioni per redditi di lavoro dipendente ed assimilati, di pensione e/o altri redditi, è riconosciuto un ammontare pari alla quota di
# detrazione che non ha trovato capienza nella predetta imposta.
