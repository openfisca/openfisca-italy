# -*- coding: utf-8 -*-

import os
from openfisca_core.taxbenefitsystems import TaxBenefitSystem
import entita
import scenarios

COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


# Our country tax and benefit class inherits from the general TaxBenefitSystem class.
# The name ItalyTaxBenefitSystem must not be changed, as all tools of the OpenFisca ecosystem expect a ItalyTaxBenefitSystem class to be exposed in the __init__ module of a country package.
class ItalyTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        # We initialize our tax and benefit system with the general constructor
        super(ItalyTaxBenefitSystem, self).__init__(entita.entities)
        # We add to our tax and benefit system all the variables
        self.add_variables_from_directory(os.path.join(COUNTRY_DIR, 'variables'))
        # We add to our tax and benefit system all the legislation parameters defined in the  parameters files
        self.load_parameters(os.path.join(COUNTRY_DIR, 'parameters'))
        self.Scenario = scenarios.Scenario
