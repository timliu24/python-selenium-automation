# Created by liudi at 1/31/2024
Feature: Verify that logged out user can access Sign In
  # Enter feature description here

  Scenario: Access Target Sign In page
    Given Open Target main page
    When Click on Sign In tab
    When Click on Sign In
    Then Verify Sign into your Target account form open