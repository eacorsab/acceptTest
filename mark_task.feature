Feature: Mark a task completed

  Scenario: Mark a task as completed
    Given the to-do list contains
      | Task          | Status  |
      | Do Homework   | Pending |
    When the user marks task "Do Homework" as completed
    Then the to-do list should show task "Do Homework" as completed

