# -*- coding: utf-8 -*-
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


# Informazioni più dettagliata riguardo la decadenza delle detrazioni per investimenti in startup qua http://www.gazzettaufficiale.it/eli/id/2016/04/11/16A02786/sg


class interessi_legali_su_imposta_non_versata_per_detrazioni_invesimenti_startup(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Gli interessi legali sull’imposta non versata per effetto dell’utilizzo della detrazione, maturati dalla data in cui l’imposta medesima avrebbe dovuto essere pagata (Rigo RP80 col.7)"
    reference = "http://www.gazzettaufficiale.it/eli/id/2016/04/11/16A02786/sg"  # Always use the most official source


class detrazione_effettivamente_fruita_negli_anni_precedenti_per_investimenti_in_startup(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"La detrazione effettivamente fruita negli anni precedenti per investimenti in startup da sommare con gli interessi legati"
    reference = "http://www.gazzettaufficiale.it/eli/id/2016/04/11/16A02786/sg"  # Always use the most official source


class detrazione_effettivamente_fruita_e_interessi_legali_per_investimenti_startup(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Questa rappresenta la colonna 8 che è data dalla detrazione più gli interessi (Rigo RP80 col.8). Questa somma va ad incrementare l'imposta lorda del periodo in esame"
    reference = "http://www.gazzettaufficiale.it/eli/id/2016/04/11/16A02786/sg"  # Always use the most official source

    def formula(person,period,parameters):
        return person('interessi_legali_su_imposta_non_versata_per_detrazioni_invesimenti_startup',period) +person('detrazione_effettivamente_fruita_negli_anni_precedenti_per_investimenti_in_startup',period)


class eccedenza_detrazione_non_fruita_e_non_piu_spettante(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"L’eccedenza di detrazione non ancora fruita, non più spettante. Tale importo va sottratto dai rispettivi residui di detrazione risultanti dagli anni precedenti, da indicare nelle colonne 1 dei righi RN18, RN19 e RN20 del presente modello.(Rigo RP80 col.9). Questa somma va ad incrementare l'imposta lorda del periodo in esame"
    reference = "http://www.gazzettaufficiale.it/eli/id/2016/04/11/16A02786/sg"  # Always use the most official source
