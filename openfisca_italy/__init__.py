# -*- coding: utf-8 -*-

import os
from openfisca_core.taxbenefitsystems import TaxBenefitSystem


COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


# Our country tax and benefit class inherits from the general TaxBenefitSystem
# class.
#
# The name CountryTaxBenefitSystem must not be changed, as all tools of the
# OpenFisca ecosystem expect a CountryTaxBenefitSystem class to be exposed in
# the __init__ module of a country package.
class CountryTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        return
