# Created by liudi at 2/7/2024
Feature: Verify 5 benefit boxes in Target Circle

  Scenario: Show the 5 benefit boxes inside Target Circle
    Given Open target main page
    When Click on Target Circle tab
    Then Verify 5 benefit boxes


  Scenario: User can click through Circle tabs
    Given Open target main page
    When Click on Target Circle tab
    Then Verify that clicking though Circle tabs works


  Scenario: User is able to navigate to Google Play Target page
    Given Open target main page
    When Click on Target Circle tab
    And Store original window
    And Click Google Play button
    And Switch to new window
    Then Verify Google Play Target page opened
    And Close current window
    And Return to original window