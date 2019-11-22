
Feature: Calculate retirement age
  As someone who is curious about retirement,
  I want to find out at what age I can retire
  and when that date is.

  Scenario Outline: Inputting birth information into the program
    Given the program is running
    When I enter "<birthYear>" for the birth year
    Then my retirement age is "<ageYear>" years and "<ageMonth>" months

    Examples: Birth information inputs and their outputs
      | birthYear | ageYear | ageMonth |
      | 1900      | 65      | 0        |
      | 1938      | 65      | 2        |
      | 1939      | 65      | 4        |
      | 1940      | 65      | 6        |
      | 1958      | 66      | 8        |
      | 1959      | 66      | 10       |
      | 1954      | 66      | 0        |
      | 1999      | 67      | 0        |
      | 2020      | -1      | -1       |



  Scenario Outline: Inputting invalid birth years
    Given the program is running
    When I enter "<invalid_inputs>" for birth year
    Then the program will raise an exception

    Examples:
      | invalid_inputs |
      | 2020           |
      | 1889           |
      | -1             |




