@webdriver

Feature: Search Property for Rent
  As a home seeker
  In dubai
  I want to search for apartments or villa using dubizzle

  Scenario: Navigate to Dubai home page
    Given I am on dubizzle dubai home page
    When I check for content
    Then I the title of home page should be dubizzle Dubai Classifieds
    And I should see place an ad option
    And I should see search form
    And I should see quick links