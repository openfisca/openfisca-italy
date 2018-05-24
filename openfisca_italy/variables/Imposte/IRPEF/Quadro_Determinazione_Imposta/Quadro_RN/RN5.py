# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# Import numpy
import numpy as np

class RN5_irpef_lorda (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Imposta sul reddito delle persone fisiche"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person, period, parameters):
        # In the IRPEF calculation the  gross base income calculation could be in two ways
        reddito_imponibile = person('reddito_imponibile',period)
        # this is a fixed calculation
        RN5_irpef_lorda = round_(parameters(period).imposte.IRPEF.aliquote_scaglioni_IRPEF.calc(reddito_imponibile),2)

        # agevolazione ACE section that is optional depending on possiede_diritto_agevolazione_ACE (optional)
        RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore = person('RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period)
        possiede_diritto_agevolazione_ACE = person('possiede_diritto_agevolazione_ACE',period)
        valore_da_sottrarre_in_caso_di_diritto_agevolazione_ACE = round_(parameters(period).imposte.IRPEF.aliquote_scaglioni_IRPEF.calc(RS37_importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore),2)
        RN5_irpef_lorda = where(possiede_diritto_agevolazione_ACE, (np.array(RN5_irpef_lorda - valore_da_sottrarre_in_caso_di_diritto_agevolazione_ACE)),(np.array(RN5_irpef_lorda)))

        # fees for amateur sports activities is optional
        RL22_compensi_con_ritenuta_a_titolo_di_imposta = person('RL22_compensi_con_ritenuta_a_titolo_di_imposta',period)
        possiede_diritto_agevolazione_per_attivita_sportive = person('possiede_diritto_agevolazione_per_attivita_sportive',period)
        valore_da_sottrarre_in_caso_di_diritto_attivita_sportive = round_(parameters(period).imposte.IRPEF.aliquote_scaglioni_IRPEF.calc(RL22_compensi_con_ritenuta_a_titolo_di_imposta),2)
        RN5_irpef_lorda = where(possiede_diritto_agevolazione_per_attivita_sportive, (np.array(RN5_irpef_lorda - valore_da_sottrarre_in_caso_di_diritto_attivita_sportive)),(np.array(RN5_irpef_lorda)))

        # incremento dell'irpef lorda nel caso di decadimento investimenti in startup
        RP80_detrazione_effettivamente_fruita_e_interessi_legali_per_investimenti_startup = person('RP80_detrazione_effettivamente_fruita_e_interessi_legali_per_investimenti_startup',period)
        RN5_irpef_lorda = where (RP80_detrazione_effettivamente_fruita_e_interessi_legali_per_investimenti_startup>0,(RN5_irpef_lorda + RP80_detrazione_effettivamente_fruita_e_interessi_legali_per_investimenti_startup),RN5_irpef_lorda)

         # conditions for what the Irpef values if fixed to 0
        irpef_non_dovuta_pensionati_e_terreni = person('irpef_non_dovuta_pensionati_e_terreni',period)
        irpef_non_dovuta_per_soli_terreni_e_fabbricati = np.array(person('irpef_non_dovuta_per_soli_terreni_e_fabbricati',period))

        # this boolean indicate that are no situations for what the Irpef values if fixed to 0
        no_condizioni_redditi_non_tassabili = not np.array(any([irpef_non_dovuta_pensionati_e_terreni,irpef_non_dovuta_per_soli_terreni_e_fabbricati]))
        # ovviamente se il reddito imponibile è 0 anche l'irpef lorda e netta devono essere 0
        return select([irpef_non_dovuta_pensionati_e_terreni, irpef_non_dovuta_per_soli_terreni_e_fabbricati, reddito_imponibile <= 0 ,no_condizioni_redditi_non_tassabili], [0, 0, 0, RN5_irpef_lorda])
