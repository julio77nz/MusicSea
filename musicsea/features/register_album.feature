Feature: Register Album
  In order to have my web up to day
  As a user
  I want to register an album in the corresponding group together

  Background: There is a registered user and group
    Given Exists a user "user" with password "password"
    And Exists group registered by "user"
      | name           |
      | Music Group 1  |

  Scenario: Register just album name
    Given I login as user "user" with password "password"
    When I register album at group "Music Group 1"
      | name     |
      | Album 1  |
    Then I'm viewing the details page for album at group "Music Group 1" by "user"
      | name     |
      | Album 1  |
    And There are 1 albums

  Scenario: Try to register album but not logged in
    Given I'm not logged in
    When I register album at group "Music Group 1"
      | name     |
      | Album 1  |
    Then I'm redirected to the login form
    And There are 0 albums