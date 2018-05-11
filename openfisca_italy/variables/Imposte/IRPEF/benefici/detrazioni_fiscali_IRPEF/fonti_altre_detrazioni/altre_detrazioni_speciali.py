# total gross income for one month and one year
# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *
# import numpy
import numpy as np


class TipiAltreDetrazioni(Enum):
    nessun_codice_inserito=u'Non sono stati fatti investimenti in startup'
    codice_uno = u'Detrazione per le borse di studio assegnate dalle Regioni o dalle Province autonome di Trento e Bolzano'
    codice_due = u'Detrazione per le donazioni all ente ospedaliero Ospedali Galliera di Genova'


class tipi_altre_detrazioni(Variable):
    value_type = Enum
    possible_values = TipiAltreDetrazioni
    default_value = TipiAltreDetrazioni.nessun_codice_inserito  # The default is codice_uno
    entity = Persona
    definition_period = YEAR
    label = u"Altre detrazioni speciali (Rigo RP83 col. 1 del quadro RP)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class importo_altre_detrazioni_speciali(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    label = u"Importo altre detrazioni speciali (Rigo RP83 col. 2 del quadro RP)"
    reference = "https://www.gbsoftware.it/legginotizia.asp?IdNews=2364"  # Always use the most official source


class altre_detrazioni(Variable):
    value_type = float
    entity = Persona
    definition_period = YEAR
    set_input = set_input_divide_by_period
    label = "Detrazioni speciali per borse di studio e donazioni ad enti ospedalieri "
    reference = "http://www.agenziaentrate.gov.it/wps/wcm/connect/fcae4d804bb1ef709472f5d94f8d55f4/Annuario_online_Parte_III.pdf?MOD=AJPERES"  # Always use the most official source

    def formula(person,period,parameters):
        return where(not_(person('tipi_altre_detrazioni',period) == TipiAltreDetrazioni.nessun_codice_inserito),np.array(0),round_(person('importo_altre_detrazioni_speciali',period),2))
