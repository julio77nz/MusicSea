Feature: Register Artist
  In order to have my web up to day
  As a user
  I want to register an artist in the corresponding group together

  Background: There is a registered user and group
    Given Exists a user "user" with password "password"
    And Exists group registered by "use/musicseaapp/r"
      | name           |
      | Music Group 1  |

  Scenario: Register just artist name
    Given I login as user "user" with password "password"
    When I register artist at group "Music Group 1"
      | name      |
      | Singer 1  |
    Then I'm viewing the details page for artist at group "Music Group 1" by "user"
      | name      |
      | Singer 1  |
    And There are 1 artists

  Scenario: Try to register artist but not logged in
    Given I'm not logged in
    When I register artist at group "Music Group 1"
      | name      |
      | Singer 1  |
    Then I'm redirected to the login form
    And There are 0 artists