# -*- coding: utf-8 -*-

# This file defines a reform.
# A reform is a set of modifications to be applied to a reference tax and benefit system to carry out experiments.
# See http://openfisca.org/doc/reforms.html


# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *


# Our reform replace `social_security_contribution` (the "reference" variable) by the following variable.
class contributo_sicurezza_sociale(Variable):
    # Variable metadata don't need to be redefined. By default, the reference variable metadatas will be used.
    def formula(person, period, parameters):
        return person('reddito_lavoro_dipendente', period) * 0.03


class contributo_piatto_sicurezza_sociale(Reform):
    # A reform always defines an `apply` method that builds the reformed tax and benefit system from the reference one.
    # See http://openfisca.org/doc/coding-the-legislation/reforms.html#writing-a-reform
    def apply(self):
        self.update_variable(contributo_sicurezza_sociale)
