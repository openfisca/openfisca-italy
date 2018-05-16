# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np

class base_imponibile_netta (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Base imponibile per L'irpef al netto della deduzione abitazione principale, oneri deducibili e maggiorata di alcune variabili condizionali"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person, period, parameters):
        # In the IRPEF calculation the  gross base income calculation could be in two ways
        base_imponibile_lorda = person('reddito_totale_lordo_annuale',period)
        oneri_deducibili = person('oneri_deducibili_totali_annuale',period)
        deduzione_abitazione_principale = person('deduzione_abitazione_principale_annuale',period)
        # this formula is fixed
        base_imponibile_netta = base_imponibile_lorda - deduzione_abitazione_principale - oneri_deducibili
        # agevolazione ACE section that is optional depending on possiede_diritto_agevolazione_ACE (optional)
        importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore = person('importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period)
        possiede_diritto_agevolazione_ACE = person('possiede_diritto_agevolazione_ACE',period)
        base_imponibile_netta = where (possiede_diritto_agevolazione_ACE,(base_imponibile_netta + importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore),base_imponibile_netta)
        # fees for amateur sports activities is optional
        compensi_con_ritenuta_a_titolo_di_imposta = person('compensi_con_ritenuta_a_titolo_di_imposta',period)
        possiede_diritto_agevolazione_per_attivita_sportive = person('possiede_diritto_agevolazione_per_attivita_sportive',period)
        base_imponibile_netta = where (possiede_diritto_agevolazione_per_attivita_sportive,(base_imponibile_netta + compensi_con_ritenuta_a_titolo_di_imposta),base_imponibile_netta)
        return base_imponibile_netta
