Feature: Register Group
  In order to have my web up to day
  As a user
  I want to register a group

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just group name
    Given I login as user "user" with password "password"
    When I register group
      | name           |
      | Music Group 1  |
    Then I'm viewing the details page for group by "user"
      | name           |
      | Music Group 1  |
    And There are 1 groups

  Scenario: Register just group name and city
    Given I login as user "user" with password "password"
    When I register group
      | name           | city      | country   |
      | Music Group 1  | Madrid    | Spain     |
    Then I'm viewing the details page for group by "user"
      | name           | city      | country   |
      | Music Group 1  | Madrid    | Spain     |
    And There are 1 groups

  Scenario: Try to register group but not logged in
    Given I'm not logged in
    When I register group
      | name        |
      | The Tavern  |
    Then I'm redirected to the login form
    And There are 0 groups