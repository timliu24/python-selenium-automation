# Created by liudi at 1/31/2024
Feature: Verify target cart is empty
  # Enter feature description here

  Scenario: Access to shopping cart and verify that it is empty
    Given Open Target main page
    When Click on cart icon
    Then Verify cart is empty