from django.test import TestCase
from enum_model.unit import Unit
# Create your tests here.

def test_unit_object():
    print(Unit.G.name)
    return
    unit = Unit(1)
    unit.transform(1,1,1)
    return


if __name__ == "__main__":
    test_unit_object()