from behave import *
from tests.features.fizz_buzz_class import FizzBuzz


@given("I created game with the number {number}")
def step_impl(context, number):
    context.product = FizzBuzz(number)


@then("the result of game will be {result_game}")
def step_impl(context, result_game):
    assert str(context.product.game()) == str(result_game)


@given("I created game Fizz with the string {string}")
def step_impl(context, string):
    context.product = FizzBuzz(string)


@then("the result of game Fizz will be {result_game}")
def step_impl(context, result_game):
    print(context.product.is_Fizz())
    print()
    assert str(context.product.is_Fizz()) == str(result_game)


@given("I created game Buzz with the string {string}")
def step_impl(context, string):
    context.product = FizzBuzz(string)


@then("the result of game Buzz will be {result_game}")
def step_impl(context, result_game):
    assert str(context.product.is_Buzz()) == str(result_game)
