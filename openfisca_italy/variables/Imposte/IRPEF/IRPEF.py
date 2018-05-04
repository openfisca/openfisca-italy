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
        # eccedenza_trasformata_in_credito_irap is optional
        eccedenza_trasformata_in_credito_irap = person('eccedenza_trasformata_in_credito_irap',period)
        possiede_diritto_agevolazione_ACE = person('possiede_diritto_agevolazione_ACE',period)
        # this formula is fixed
        base_imponibile_netta = base_imponibile_lorda - deduzione_abitazione_principale - oneri_deducibili
        return where (possiede_diritto_agevolazione_ACE,(base_imponibile_netta + eccedenza_trasformata_in_credito_irap),base_imponibile_netta)

class irpef_lorda (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Imposta sul reddito delle persone fisiche"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person, period, parameters):
        # In the IRPEF calculation the  gross base income calculation could be in two ways
        base_imponibile_netta = person('base_imponibile_netta',period)
        # agevolazione ACE section that is optional depending on possiede_diritto_agevolazione_ACE
        eccedenza_trasformata_in_credito_irap = person('eccedenza_trasformata_in_credito_irap',period)
        possiede_diritto_agevolazione_ACE = person('possiede_diritto_agevolazione_ACE',period)
        valore_da_sottrarre_in_caso_di_diritto_agevolazione_ACE = round_(parameters(period).imposte.IRPEF.aliquote_scaglioni_IRPEF.calc(eccedenza_trasformata_in_credito_irap),2)
        # this is a fixed calculation
        irpef_lorda = round_(parameters(period).imposte.IRPEF.aliquote_scaglioni_IRPEF.calc(base_imponibile_netta),2) 
        return where(possiede_diritto_agevolazione_ACE, (np.array(irpef_lorda - valore_da_sottrarre_in_caso_di_diritto_agevolazione_ACE)),(np.array(irpef_lorda)))


class irpef_netta (Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR  # This housing tax is defined for a year.
    label = u"Imposta sul reddito delle persone fisiche"
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf"  # Always use the most official source

    def formula(person, period, parameters):
        irpef_lorda = person('irpef_lorda',period)
        detrazioni_imposta = person('detrazioni_imposta_annuale',period)
        irpef_netta = irpef_lorda - detrazioni_imposta
        return np.array(round_(irpef_netta,2))   
        # TO DO: variabile per capirese l'irpef del soggetto è da versare o no