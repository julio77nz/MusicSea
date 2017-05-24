Feature: Register Song
  In order to have my web up to day
  As a user
  I want to register a song in the corresponding group and album together

  Background: There is a registered user and group and album
    Given Exists a user "user" with password "password"
    And Exists group registered by "user"
      | name           |
      | Music Group 1  |
    And Exists album registered by "user"
      | name           |
      | Album Group 1  |

  Scenario: Register just song name
    Given I login as user "user" with password "password"
    When I register song at group "Music Group 1"
      | name    |
      | Song 1  |
    And I register song at album "Album Group 1"
      | name    |
      | Song 1  |
    Then I'm viewing the details page for song at group "Music Group 1" album "Album Group 1" by "user"
      | name    |
      | Song 1  |
    And There are 1 songs

  Scenario: Try to register song but not logged in
    Given I'm not logged in
    When I register song at group "Music Group 1"
      | name    |
      | Song 1  |
    And I register song at album "Album Group 1"
      | name    |
      | Song 1  |
    Then I'm redirected to the login form
    And There are 0 songs