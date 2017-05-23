# Created by ierathenz at 23/05/17
Feature: List Groups
  As a User, I want to see how many groups there are.

  Background: There are 5 registered groups by same user
  Given Exist a user "user" with password "password"
  And Exist group registered by "user"
    | name        | genre      |
    | Group1      | pop        |
    | Group2      | pop        |
    | Group3      | pop        |
    | Group4      | pop        |
    | Group5      | pop        |

  Scenario: List the last five
    When I list groups
    Then I'm viewing a list containing
    | name        |
    | Group1      |
    | Group2      |
    | Group3      |
    | Group4      |
    | Group5      |
    And The list contains 5 groups

  Scenario: List the last five
    Given Exists group registered by "user"
      | name        | genre      |
      | Group6      | pop        |
    When I list groups
    Then I'm viewing a list containing
      | name        |
      | Group6      |
      | Group5      |
      | Group4      |
      | Group3      |
      | Group2      |

    And The list contains 5 groups