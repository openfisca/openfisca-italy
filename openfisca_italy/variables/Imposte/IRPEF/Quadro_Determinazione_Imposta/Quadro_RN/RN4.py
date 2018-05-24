# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np

class reddito_imponibile (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Base imponibile per L'irpef al netto della deduzione abitazione principale, oneri deducibili e maggiorata di alcune variabili condizionali"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person, period, parameters):
        # In the IRPEF calculation the  gross base income calculation could be in two ways
        reddito_imponibile = person('RN1_reddito_complessivo',period) + person('RN1_credito_per_fondi_comuni',period) - person('RN1_perdite_compensabili_con_crediti_per_fondi_comuni',period) - person('RN2_deduzione_abitazione_principale',period) - person('RN3_oneri_deducibili_totali',period)
        # agevolazione ACE section that is optional depending on possiede_diritto_agevolazione_ACE (optional)
        RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore = person('RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period)
        possiede_diritto_agevolazione_ACE = person('possiede_diritto_agevolazione_ACE',period)
        reddito_imponibile = where (possiede_diritto_agevolazione_ACE,(reddito_imponibile + RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore),reddito_imponibile)
        # fees for amateur sports activities is optional
        RL22_compensi_con_ritenuta_a_titolo_di_imposta = person('RL22_compensi_con_ritenuta_a_titolo_di_imposta',period)
        possiede_diritto_agevolazione_per_attivita_sportive = person('possiede_diritto_agevolazione_per_attivita_sportive',period)
        reddito_imponibile = where (possiede_diritto_agevolazione_per_attivita_sportive,(reddito_imponibile + RL22_compensi_con_ritenuta_a_titolo_di_imposta),reddito_imponibile)
        return where (reddito_imponibile >= 0, reddito_imponibile, np.array(0))
