# Created by liudi at 2/14/2024
Feature: Search a product that have multiple variations and verify the variations.


  Scenario: Search for jeans and verify color option is show.
    Given Open Target main page
    When Search for DENIZEN from Levi's Men's 285
    And Click on DENIZEN from Levi's Men's 285
    Then User can click and verify through options

