# Created by liudi at 1/31/2024
Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Cart show added item and price
    Given Open target main page
    When Search for coffee
    When Click Add to cart icon on Folgers Classic Medium
    When Click on Options
    When Click Add to cart bar
    When Click View cart and check out
    Then Verify cart have items