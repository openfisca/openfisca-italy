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
    label = u"Base imponibile netta per L'irpef"
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

class irpef_lorda (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Imposta sul reddito delle persone fisiche"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person, period, parameters):
        # In the IRPEF calculation the  gross base income calculation could be in two ways
        base_imponibile_netta = person('base_imponibile_netta',period)
        # this is a fixed calculation
        irpef_lorda = round_(parameters(period).imposte.IRPEF.aliquote_scaglioni_IRPEF.calc(base_imponibile_netta),2)

        # agevolazione ACE section that is optional depending on possiede_diritto_agevolazione_ACE (optional)
        importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore = person('importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore',period)
        possiede_diritto_agevolazione_ACE = person('possiede_diritto_agevolazione_ACE',period)
        valore_da_sottrarre_in_caso_di_diritto_agevolazione_ACE = round_(parameters(period).imposte.IRPEF.aliquote_scaglioni_IRPEF.calc(importo_del_rendimento_nozionale_di_spettanza_dell_imprenditore),2)
        irpef_lorda = where(possiede_diritto_agevolazione_ACE, (np.array(irpef_lorda - valore_da_sottrarre_in_caso_di_diritto_agevolazione_ACE)),(np.array(irpef_lorda)))

        # fees for amateur sports activities is optional
        compensi_con_ritenuta_a_titolo_di_imposta = person('compensi_con_ritenuta_a_titolo_di_imposta',period)
        possiede_diritto_agevolazione_per_attivita_sportive = person('possiede_diritto_agevolazione_per_attivita_sportive',period)
        valore_da_sottrarre_in_caso_di_diritto_attivita_sportive = round_(parameters(period).imposte.IRPEF.aliquote_scaglioni_IRPEF.calc(compensi_con_ritenuta_a_titolo_di_imposta),2)
        irpef_lorda = where(possiede_diritto_agevolazione_per_attivita_sportive, (np.array(irpef_lorda - valore_da_sottrarre_in_caso_di_diritto_attivita_sportive)),(np.array(irpef_lorda)))

        # incremento dell'irpef lorda nel caso di decadimento investimenti in startup
        detrazione_effettivamente_fruita_e_interessi_legali_per_investimenti_startup = person('detrazione_effettivamente_fruita_e_interessi_legali_per_investimenti_startup',period)
        irpef_lorda = where (detrazione_effettivamente_fruita_e_interessi_legali_per_investimenti_startup>0,(irpef_lorda + detrazione_effettivamente_fruita_e_interessi_legali_per_investimenti_startup),irpef_lorda)

         # conditions for what the Irpef values if fixed to 0
        irpef_non_dovuta_pensionati_e_terreni = person('irpef_non_dovuta_pensionati_e_terreni',period)
        irpef_non_dovuta_per_soli_terreni_e_fabbricati = np.array(person('irpef_non_dovuta_per_soli_terreni_e_fabbricati',period))

        # this boolean indicate that are no situations for what the Irpef values if fixed to 0
        no_condizioni_redditi_non_tassabili = not np.array(any([irpef_non_dovuta_pensionati_e_terreni,irpef_non_dovuta_per_soli_terreni_e_fabbricati]))
        return select([irpef_non_dovuta_pensionati_e_terreni, irpef_non_dovuta_per_soli_terreni_e_fabbricati, no_condizioni_redditi_non_tassabili], [0, 0, irpef_lorda])

# TODO: definire quadro TR per poter compilare la colonna 1 del rigo RN 26
class irpef_netta (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Imposta sul reddito delle persone fisiche netta Rigo RN26 col.2"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person, period, parameters):
        irpef_lorda = person('irpef_lorda',period)
        detrazioni_imposta_annuale = person('detrazioni_imposta_annuale',period)
        totale_altre_detrazioni_crediti_di_imposta = person('totale_altre_detrazioni_crediti_di_imposta',period)
        irpef_netta = irpef_lorda - detrazioni_imposta_annuale - totale_altre_detrazioni_crediti_di_imposta
        return where (irpef_netta>0,np.array(round_(irpef_netta,2),np.array(0)))
