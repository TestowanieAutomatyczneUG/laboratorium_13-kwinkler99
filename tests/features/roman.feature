Feature: Roman number
  Program allows change number to roman number

  Scenario: Numbers equal 1
    Given create class with number 1
    When roman number is generated
    Then roman number should be equal I

  Scenario: Number equal V
    Given create class with number 5
    When roman number is generated
    Then roman number should be equal V

  Scenario: Number equal 9
    Given create class with number 9
    When roman number is generated
    Then roman number should be equal IX

  Scenario: Number equal 27
    Given  create class with number 27
    When roman number is generated
    Then roman number should be equal XXVII

  Scenario: Number equal 48
    Given create class with number 48
    When roman number is generated
    Then roman number should be equal XLVIII

  Scenario: Number equal 49
    Given create class with number 49
    When roman number is generated
    Then roman number should be equal XLIX

  Scenario: Number equal  59
    Given create class with number 59
    When roman number is generated
    Then roman number should be equal LIX

  Scenario: Number equal 141
    Given create class with number 141
    When roman number is generated
    Then roman number should be equal CXLI