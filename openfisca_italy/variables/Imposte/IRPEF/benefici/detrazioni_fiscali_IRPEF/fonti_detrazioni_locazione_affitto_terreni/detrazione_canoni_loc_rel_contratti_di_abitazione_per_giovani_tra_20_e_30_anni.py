# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


class detrazione_per_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni  per gli inquilini di alloggi adibiti ad abitazione principale con contratti per i giovani di età compresa tra i 20 ed i 30 anni"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person, period, parameters):
        percentuale_di_spettanza = round_((1.00 / person('numero_inquilini_relativo_a_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni',period)),2)
        percentuale_giorni = round_((person('numero_giorni_immobile_adibito_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni',period)/365.00),2)
        reddito_totale_lordo_annuale = person('reddito_totale_lordo_annuale',period)
        detrazione_senza_percentuali = select([not_(person('canoni_di_locazione_relativi_a_contratti_di_locazione_per_abitazione_principale_per_giovani_tra_20_e_30_anni_compilato',period)),
                                                reddito_totale_lordo_annuale<=15493.71,
                                                reddito_totale_lordo_annuale>=15493.71],
                                                [0,991.60,0])
        return round_((detrazione_senza_percentuali * percentuale_di_spettanza * percentuale_giorni),0)



class canoni_di_locazione_relativi_a_contratti_di_locazione_per_abitazione_principale_per_giovani_tra_20_e_30_anni_compilato(Variable):
    value_type = bool
    entity = Persona
    definition_period = YEAR
    label = "E' stato indicato il codice “3” nella colonna 1 del rigo RP71 "
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class numero_giorni_immobile_adibito_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Numero di giorni per cui è valso il contratto tra inquilini alloggi_adibiti_ad_abitazione_principale con contratti per i giovani di età compresa tra i 20 ed i 30 anni"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source


class numero_inquilini_relativo_a_inquilini_alloggi_adibiti_ad_abitazione_principale_con_contratti_per_giovani_tra_20_e_30_anni(Variable):
    value_type = int
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Numero di inquilini per cui è valso il contratto tra inquilini alloggi_adibiti_ad_abitazione_principale con contratti per i giovani di età compresa tra i 20 ed i 30 anni"
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source
