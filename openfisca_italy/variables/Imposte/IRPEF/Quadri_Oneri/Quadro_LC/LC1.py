# -*- coding: utf-8 -*-
# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class LC1_imposta_cedolare_secca(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC1 col.1 -  indicare l’ammontare dell’imposta sostitutiva dovuta indicato nella colonna 3 del rigo RB11 " # TODO: mettere importo col 3 RB11 quando RB sarà fatto
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=52"  # Always use the most official source
