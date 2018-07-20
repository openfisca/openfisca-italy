# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

# Queste variabili sono da inserire all'interno del quadro RS quando questo verrà creato


# RS tax framework field
class RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RS 37 colonna 14 -la somma tra l’importo relativo al rendimento nozionale di spettanza dell’imprenditore (col. 11 – col. 12) che viene utilizzato nella presente dichiarazione in diminuzione del reddito complessivo e la quota dedotta dalle società partecipate beneficiarie della deduzione."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Normativa+e+Prassi/Provvedimenti/2018/Gennaio+2018+Provvedimenti/Provvedimento+30012018+PF/PF3_2018_istruzioni.pdf#page=48"  # Always use the most official source

class RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore_utilizzato(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "RS 37 colonna 16 - quota del rendimento nozionale indicato in colonna 14, di spettanza dell’imprenditore (col. 11 – col. 12) che viene utilizzato nella presente dichiarazione in diminuzione del reddito complessivo da indicare nella colonna 5 del rigo RN1."
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Normativa+e+Prassi/Provvedimenti/2018/Gennaio+2018+Provvedimenti/Provvedimento+30012018+PF/PF3_2018_istruzioni.pdf#page=48"  # Always use the most official source
