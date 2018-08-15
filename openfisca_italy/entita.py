# -*- coding: utf-8 -*-

# This file defines the entities needed by our legislation.
from openfisca_core.entities import build_entity

Famiglia = build_entity(
    key = "household",
    plural = "households",
    label = u'Famiglia',
    doc = '''
    Una famiglia è un'entità di gruppo, formata da n persone.
    Ogni individuo assume un ruolo (un individuo sarà il genitore 1, un altro il genitore 2 ed infine n figli)
    Da ciò si assume che un certi ruoli avranno capienza limitata (genitore) mentre altri no (figli).

    Esempio di variabili di un'enità di gruppo:
    Nel caso della famiglia, potrebbero esistere sgravi fiscali relativi al numero dei figli facenti parte il nucleo famigliare.

    Utilizzo:
    E' possibile calcolare il numero di individui che ricopre un certo ruolo (ad esempio, vedere se esiste una figura del 'genitore 2' con household.nb_persons(Household.SECOND_PARENT)).
    Calcolare una variabile esistente per ogni tipo di individuo appartenente alla famiglia (ad esempio calcolare il 'salario' per ogni membro della 'Famiglia' con salario = household.members('salary', period = MONTH); sum_salaries = household.sum(salaries)).

    Per ulteriori informazioni vedere: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    roles = [
        {
            'key': 'parent',
            'plural': 'parents',
            'label': u'Parents',
            'max': 2,
            'subroles': ['first_parent', 'second_parent'],
            'doc': u'The one or two adults in charge of the household.'
            },
        {
            'key': 'child',
            'plural': 'children',
            'label': u'Child',
            'doc': u'Other individuals living in the household.'
            }
        ]
    )

Persona = build_entity(
    key = "person",
    plural = "persons",
    label = u'Persona',
    doc = '''
    A Person represents an individual, the minimal legal entity on which a legislation might be applied.

    Example:
    The 'salary' and 'income_tax' variables are usually defined for the entity 'Person'.

    Usage:
    Calculate a variable applied to a 'Person' (e.g. access the 'salary' of a specific month with person('salary', "2017-05")).
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'first_parent' in a 'Household' entity with person.has_role(Household.FIRST_PARENT)).

    For more information, see: http://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True,
    )

entities = [Famiglia, Persona]
