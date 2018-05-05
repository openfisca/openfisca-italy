# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *

class detrazioni_per_conigue_a_carico(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period  
    label = "Detrazioni dovute per coniuge a carico"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source
    
    def formula(person,period,parameters):
        #reddito per detrazioni è uguale alla somma del reddito_totale_lordo_annuale - deduzione_abitazione_principale + importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore
        reddito_per_detrazioni = person('reddito_totale_lordo_annuale',period) - person('deduzione_abitazione_principale_annuale',period) + person('importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period)
        # detrazioni varie
        return reddito_per_detrazioni