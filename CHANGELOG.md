# Changelog

# 0.1.0 - [#2](https://github.com/openfisca/openfisca-italy/pull/2)

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas:
  - Parameters
  - Reforms
  - Variables
* Massive files renaming respect to openFisca_country_template:
  - Folders
    * `parameters/benefits` -> `parameters/benefici`
    * `parameters/general` -> `parameters/eta`
    * `parameters/taxes` -> `parameters/tasse`
    * `tests/reforms` -> `tests/Riforme`
  - Files
    * `benefici/housing_allowance.yaml` -> `benefici/indennita_alloggio.yaml`
    * `benefici/basic_income.yaml` -> `benefici/indennita_alloggio.yaml`
    * `eta/age_of_majority.yaml` -> `eta/maggiore_eta.yaml`
    * `eta/age_of_retirement.yaml.yaml` -> `eta/eta_pensionamento.yaml`
    * `tasse/income_tax_rate.yaml` -> `tasse/aliquota_imposta_reddito.yaml`
    * `tasse/social_security_contribution.yaml` -> `tasse/contributo_sicurezza_sociale.yaml`
    * `reforms/flat_social_security_contribution.py` -> `reforms/contributo_piatto_sicurezza_sociale.py`
    * `reforms/modify_social_security_taxation.py` -> `reforms/modifica_tassazione_sicurezza_sociale.py`
    * `reforms/removal_basic_income.py` -> `reforms/rimozione_reddito_base.py`
    * `situation_example/couple.json` -> `situation_example/coppie.json`
    * `tests/Riforme/modify_social_security_taxation.yaml` -> 
    * `tests/Riforme/modifica_la_tassazione_sulla_sicurezza_sociale.yaml`
    * `tests/social_security_contribution.yaml` -> `tests/contributi_previdenziali.yaml`
    * `tests/age_of_majority.yaml` -> `tests/eta_pensionabile.yaml`
    * `tests/age.yaml` -> `tests/eta.yaml`
    * `tests/income_tax.yaml` -> `tests/imposta_sul_reddito.yaml`
    * `tests/housing_allowance.yaml` -> `tests/indennita_di_alloggio.yaml`
    * `tests/basic_income.yaml` -> `tests/reddito_di_base.yaml`
    * `tests/age_of_majority.yaml` -> `tests/reddito_disponibile.yaml`
    * `tests/housing_tax.yaml` -> `tests/tassa_di_alloggio.yaml`
    * `variables/housing.py` -> `variables/alloggio.py`
    * `variables/benefits.py` -> `variables/benefici.py`
    * `variables/demographics.py` -> `variables/demografia.py`
    * `variables/income.py` -> `variables/reddito.py`
    * `variables/stats.py` -> `variables/statistiche.py`
    * `variables/taxes.py` -> `variables/tasse.py`
    * `entities.py` -> `entita.py`
* Details:
  - Build the structure of the italian tax and benefit system (adapt country_template translating names of      files, variables...)
  - Introduce directory `tasse_lavoro` to distinguish work taxes and all the other type of taxes
  - Introduce parameter `eta_pensionabile.yaml` in `parameters/eta` used to know if a person could retire
  - Introduce variable `is_age_retirement` in `demografia.py` used to know if a person has the minimum age to   retire (using the parameter `parameters/eta/eta_pensionabile.yaml`)
  - Add tests yaml for `is_age_retirement` in `tests/eta/eta_pensionabile.yaml`
  - Introduce parameter `eta_lavorativa.yaml` in `parameters/eta` used to know if a person could work
  - Introduce variable `is_age_of_work` in `demografia.py` used to know if a person has the minimum age to   work (using the parameter `parameters/eta/eta_lavorativa.yaml`)
  - Add tests yaml for `is_age_of_work` in `tests/eta/eta_lavorativa.yaml`
  - Introduce parameter `maggiore_eta.yaml` in `parameters/eta` used to know if a person is adult
  - Introduce variable `is_adult` in `demografia.py` used to know if a person is adult (using the parameter `parameters/eta/maggiore_eta.yaml`)
  - Add tests yaml for `is_adult` in  `tests/eta/maggiore_eta.yaml`
  - Build using Core v21
