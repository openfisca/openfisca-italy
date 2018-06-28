# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# Queste variabili sono da inserire all'interno del quadro RL quando questo verrà creato

class RL22_compensi_con_ritenuta_a_titolo_di_imposta(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RL 22 col.1 - Indicare importo colonna 3 Prospetto per i compensi ed altre somme derivanti da attività sportive dilettantistiche e da collaborazioni in cori, bande e filodrammatiche rese da direttori e collaboratori tecnici"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Normativa+e+Prassi/Provvedimenti/2018/Gennaio+2018+Provvedimenti/Provvedimento+30012018+PF/Redditi_PF2_istruzioni.pdf#page=12"  # Always use the most official source
