from behave import *
from tests.features.roman import RomanNumerals


@given('create class with number 1')
def step_impl(context):
    context.number = RomanNumerals(1)


@when('roman number is generated')
def step_impl(context):
    context.new_number = context.number.roman()


@then('roman number should be equal I')
def step_impl(context):
    assert context.new_number == "I"


@given('create class with number 5')
def step_impl(context):
    context.number = RomanNumerals(5)


@then('roman number should be equal V')
def step_impl(context):
    assert context.new_number == "V"


@given('create class with number 9')
def step_impl(context):
    context.number = RomanNumerals(9)


@then('roman number should be equal IX')
def step_impl(context):
    assert context.new_number == "IX"


@given('create class with number 27')
def step_impl(context):
    context.number = RomanNumerals(27)


@then('roman number should be equal XXVII')
def step_impl(context):
    assert context.new_number == "XXVII"


@given('create class with number 48')
def step_impl(context):
    context.number = RomanNumerals(48)


@then('roman number should be equal XLVIII')
def step_impl(context):
    assert context.new_number == "XLVIII"


@given('create class with number 49')
def step_impl(context):
    context.number = RomanNumerals(49)


@then('roman number should be equal XLIX')
def step_impl(context):
    assert context.new_number == "XLIX"


@given('create class with number 59')
def step_impl(context):
    context.number = RomanNumerals(59)


@then('roman number should be equal LIX')
def step_impl(context):
    print(context.new_number)
    assert context.new_number == "LIX"


@given('create class with number 141')
def step_impl(context):
    context.number = RomanNumerals(141)


@then('roman number should be equal CXLI')
def step_impl(context):
    assert context.new_number == "CXLI"
