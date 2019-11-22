from pytest_bdd import given, when, then, parsers, scenarios
from calcRetirement import *
import pytest


EXTRA_TYPES = {
    'Number': int,
    'String': str,
}

CONVERTERS = {
    'birthYear': int,
    'birthMonth': int,
    'ageYear': int,
    'ageMonth': int,
    'retireMonth': str,
    'retireYear': int,
    'invalid_inputs': int,

}

scenarios('../features/calcRetirement.feature', example_converters=CONVERTERS)


@given("the program is running")
def test_calc():
    pass


@when(parsers.cfparse('I enter "{birthYear:Number}" for the birth year',
                      extra_types=EXTRA_TYPES))
@when('I enter "<birthYear>" for the birth year')
def birth_year(birthYear):
    age, month = retirement(birthYear)
    return age, month


@then(parsers.cfparse('my retirement age is "{ageYear:Number}" and '
                      '"{ageMonth}" months', extra_types=EXTRA_TYPES))
@then('my retirement age is "<ageYear>" years and "<ageMonth>" months')
def retire_age(ageYear, ageMonth):
    assert ageYear, ageMonth == birth_year


@when(parsers.cfparse('I enter "{invalid_inputs:Number}" for birth year', extra_types=EXTRA_TYPES))
@when('I enter "<invalid_inputs>" for birth year')
def invalid_inputs(invalid_inputs):
    return retirement(invalid_inputs)


@then("the program will raise an exception")
def raise_error():
    with pytest.raises(TypeError):
        invalid_inputs()



