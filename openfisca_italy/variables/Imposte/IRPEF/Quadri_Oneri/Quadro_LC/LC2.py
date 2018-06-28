# -*- coding: utf-8 -*-
# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
import numpy as np

class LC2_primo_acconto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC2 col.1 -  Indicare la prima rata dell' acconto cedolare secca locazioni per l’anno 2018. Guardare documentazione per maggiori dettagli "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        LC1_col_5 = person('LC1_differenza',period)
        caso_acconto_non_dovuto = LC1_col_5 <= parameters(period).imposte.IRPEF.Quadro_LC.limite_LC1_Col_5_per_acconto_LC2
        caso_acconto_dovuto = LC1_col_5 > parameters(period).imposte.IRPEF.Quadro_LC.limite_LC1_Col_5_per_acconto_LC2
        acconto_dovuto = round_((LC1_col_5 * parameters(period).imposte.IRPEF.Quadro_LC.percentuale_acconto_dovuto_LC2),2)
        caso_unica_soluzione = acconto_dovuto < parameters(period).imposte.IRPEF.Quadro_LC.limite_acconto_unico_LC2
        caso_soluzione_due_rate = acconto_dovuto > parameters(period).imposte.IRPEF.Quadro_LC.limite_acconto_unico_LC2
        prima_rata = round((acconto_dovuto * 0.4),2)
        return select([caso_acconto_non_dovuto,
                (caso_acconto_dovuto *caso_unica_soluzione),
                (caso_acconto_dovuto * caso_soluzione_due_rate)],
                [0,0,prima_rata])


class LC2_secondo_o_unico_acconto(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "LC2 col.2 -  Indicare la seconda rata o l'unico acconto cedolare secca locazioni per l’anno 2018. Guardare documentazione per maggiori dettagli "
    reference = "http://www.agenziaentrate.gov.it/wps/file/Nsilib/Nsi/Schede/Dichiarazioni/Redditi+Persone+fisiche+2018/Modello+e+istruzioni+Redditi+PF2018/Istruzioni+Redditi+Pf+-+Fascicolo+1+2018/PF1_istruzioni_2018_Ret.pdf#page=82"  # Always use the most official source

    def formula(person,period,parameters):
        LC1_col_5 = person('LC1_differenza',period)
        caso_acconto_non_dovuto = LC1_col_5 <= parameters(period).imposte.IRPEF.Quadro_LC.limite_LC1_Col_5_per_acconto_LC2
        caso_acconto_dovuto = LC1_col_5 > parameters(period).imposte.IRPEF.Quadro_LC.limite_LC1_Col_5_per_acconto_LC2
        acconto_dovuto = round_((LC1_col_5 * parameters(period).imposte.IRPEF.Quadro_LC.percentuale_acconto_dovuto_LC2),2)
        caso_unica_soluzione = acconto_dovuto < parameters(period).imposte.IRPEF.Quadro_LC.limite_acconto_unico_LC2
        caso_soluzione_due_rate = acconto_dovuto > parameters(period).imposte.IRPEF.Quadro_LC.limite_acconto_unico_LC2
        seconda_rata = round_((acconto_dovuto * 0.6),2)
        return select([caso_acconto_non_dovuto,
                (caso_acconto_dovuto *caso_unica_soluzione),
                (caso_acconto_dovuto * caso_soluzione_due_rate)],
                [0,acconto_dovuto,seconda_rata])
