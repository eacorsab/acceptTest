Feature: Remove a task

  Scenario: Remove a task from the to-do list
    Given the to-do list is
      | Task         |
      | Go to the gym|
      | Pay bills    |
    When the user removes the task "Go to the gym"
    Then the to-do list should not contain "Go to the gym"