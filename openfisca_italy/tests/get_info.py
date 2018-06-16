# importo reform
from openfisca_italy import ItalyTaxBenefitSystem # import tax benefit system
from openfisca_italy.scenarios import Scenario # import scenario
from openfisca_italy.entita import * # import scenario
import inspect



# main
tax_benefit_system = ItalyTaxBenefitSystem() #prendi il sistema di tasse e benefici
# scenario normale
variables = tax_benefit_system.get_variables(entity = Persona)

for k,v in variables.iteritems():
    if not (v.is_input_variable()):
        print "\nVariable:", k
        print v.value_type.__name__
        print v.entity.__name__
        if v.label:
            print v.label.encode("utf-8")
        print v.definition_period
        lines = inspect.getsource(v.get_formula())  # get formula if the variable if exist
        print lines
