# Created by liudi at 1/31/2024
Feature: Target.com search tests

  Scenario: User can search for a product on target
    Given Open Target main page
    When Search for coffee
    Then Search results for coffee are shown

  # Make sure Scenario names are unique:
  Scenario: User can search for a mug on target
    Given Open Target main page
#    When Search for mug
#    Then Search results for coffee are shown