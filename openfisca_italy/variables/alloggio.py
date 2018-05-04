# -*- coding: utf-8 -*-

# This file defines the variables of our legislation.
# A variable is property of a person, or an entity (e.g. a household).
# See http://openfisca.org/doc/variables.html

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_italy.entita import *


# This variable is a pure input: it doesn't have a formula
class accomodation_size(Variable):
    value_type = float
    entity = Famiglia
    definition_period = MONTH
    label = u"Dimensione dell'alloggio, in metri quadri"


# This variable is a pure input: it doesn't have a formula
class rent(Variable):
    value_type = float
    entity = Famiglia
    definition_period = MONTH
    label = u"Affitto pagato dalla famiglia"


#  Possible values for the housing_occupancy_status variable, defined further down
class HousingOccupancyStatus(Enum):
    __order__ = "owner tenant free_lodger homeless"
    owner = u'Proprietario'
    tenant = u'Inquilino'
    free_lodger = u'Inquilino gratuito'
    homeless = u'Senzatetto'


class housing_occupancy_status(Variable):
    value_type = Enum
    possible_values = HousingOccupancyStatus
    default_value = HousingOccupancyStatus.tenant
    entity = Famiglia
    definition_period = MONTH
    label = u"Situazione abitativa legale della famiglia riguardante la loro residenza principale"