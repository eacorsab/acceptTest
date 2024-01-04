Feature: Add a task to the to-do list

    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds a task "Do homework"
        Then the to-do list should contain "Do homework"