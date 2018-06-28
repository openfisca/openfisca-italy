 #-*- coding: utf-8 -*-

from openfisca_core import conv
from openfisca_core.scenarios import AbstractScenario


class Scenario(AbstractScenario):
    def init_single_entity(self, axes = None, children = None, households = None, parent1 = None, parent2 = None,
            period = None):
        if children is None:
            children = []
        assert parent1 is not None
        households = households.copy() if households is not None else {}
        persons = []
        for index, person in enumerate([parent1, parent2] + (children or [])):
            if person is None:
                continue
            id = person.get('id')
            if id is None:
                person = person.copy()
                person['id'] = id = 'ind{}'.format(index)
            persons.append(person)
            if index <= 1:
                households.setdefault('parents', []).append(id)
            else:
                households.setdefault('children', []).append(id)
        households.setdefault('children', [])
        conv.check(self.make_json_or_python_to_attributes())(dict(
            axes = axes,
            period = period,
            test_case = dict(
                households = [households],
                persons = persons,
                ),
            ))
        return self
