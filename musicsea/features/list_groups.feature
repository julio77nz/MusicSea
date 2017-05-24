Feature: List Groups
  In order to keep myself up to date about groups registered in musicseaapp
  As a user
  I want to list the last 5 registered groups

  Background: There are 6 registered groups by same user
    Given Exists a user "user" with password "password"
    And Exists group registered by "user"
      | name           | date        |
      | Group 1        | 2017-06-18  |
      | Group 2        | 2017-06-19  |
      | Group 3        | 2017-06-20  |
      | Group 4        | 2017-06-21  |
      | Group 5        | 2017-06-22  |

  Scenario: List the last five
    When I list groups
    Then I'm viewing a list containing
      | name           |
      | Group 5        |
      | Group 4        |
      | Group 3        |
      | Group 2        |
      | Group 1        |
    And The list contains 5 groups

  Scenario: List the last five
    Given Exists group registered by "user"
      | name            | date        |
      | Group 6         | 2017-06-17  |
    When I list groups
    Then I'm viewing a list containing
      | name            |
      | Group 6        |
      | Group 5        |
      | Group 4        |
      | Group 3        |
      | Group 2        |
    And The list contains 5 groups