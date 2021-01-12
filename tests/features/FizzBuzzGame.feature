Feature: game FizzBuzz

  Scenario Outline: numbers divisible by 3
    Given I created game with the number <number>
    Then the result of game will be <result_game>

    Examples: Game with Fizz
      | number | result_game |
      | 9      | Fizz        |
      | 12     | Fizz        |
      | 6      | Fizz        |



  Scenario Outline: numbers divisible by 5
    Given I created game with the number <number>
    Then the result of game will be <result_game>

    Examples: Game with Buzz
      | number | result_game |
      | 5      | Buzz        |
      | 10     | Buzz        |
      | 20     | Buzz        |



  Scenario Outline: numbers divisible by 15
    Given I created game with the number <number>
    Then the result of game will be <result_game>

    Examples: Game with FizzBuzz
      | number | result_game    |
      | 15     | FizzBuzz       |
      | 30     | FizzBuzz       |
      | 60     | FizzBuzz       |



  Scenario Outline: Is it Fizz?
    Given I created game Fizz with the string <string>
    Then the result of game Fizz will be <result_game>

    Examples: Fizz
      | string | result_game        |
      | None   | None is not Fizz!  |
      | 40     | 40 is not Fizz!   |
      | Fizz   | Fizz               |



  Scenario Outline: Is it Buzz?
    Given I created game Buzz with the string <string>
    Then the result of game Buzz will be <result_game>

    Examples: Buzz
      | string | result_game        |
      | Bzz    | Bzz is not Buzz!   |
      | Test   | Test is not Buzz! |
      | Buzz   | Buzz               |