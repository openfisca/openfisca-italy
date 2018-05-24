# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np


class RN26_irpef_netta (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Imposta sul reddito delle persone fisiche netta Rigo RN26 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person, period, parameters):
        reddito_imponibile = person('reddito_imponibile',period) # prendo il reddito imponibile perchè se questo era 0 o minore di 0 l'irpef netta è 0
        RN5_irpef_lorda = person('RN5_irpef_lorda',period)
        RN22_totale_detrazioni_imposta = person('RN22_totale_detrazioni_imposta',period)
        RN25_totale_altre_detrazioni_crediti_imposta = person('RN25_totale_altre_detrazioni_crediti_imposta',period)
        RN26_irpef_netta = RN5_irpef_lorda - RN22_totale_detrazioni_imposta - RN25_totale_altre_detrazioni_crediti_imposta
        RN26_irpef_netta = where(reddito_imponibile <= 0, 0, RN26_irpef_netta) # se reddito imponibile è uguale a 0 anche l'imposta netta è 0
        return where (RN26_irpef_netta>0,np.array(round_(RN26_irpef_netta,2)),np.array(0))
