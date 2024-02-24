# Created by liudi at 1/31/2024
Feature: Verify that logged out user can access Sign In
  # Enter feature description here

  Scenario: Access Target Sign In page
    Given Open Target main page
    When Click on Sign In tab
    When Click on Sign In
    Then Verify Sign into your Target account form open


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Click on Sign In tab
    And Click on Sign In
    And Store original window
    And Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current window
    And Return to original window