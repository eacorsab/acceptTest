Feature: Show all tasks from to-do list

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks:
        | Task         |
        | Buy groceries|
        | Pay bills    |
        When the user lists all tasks
        Then the output should contain:
        """
        Tasks:
        - Buy groceries
        - Pay bills
        """
