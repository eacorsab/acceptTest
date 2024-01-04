Feature: Add multiple tasks

    Scenario: Add multiple tasks to the to-do list
    Given the to-do list is empty:
    When the user adds tasks:
        | Task          |
        | Buy groceries |
        | Pay bills     |
        | Clean house   |
    Then the to-do list should contain:
        """
        - Buy groceries
        - Pay bills
        - Clean house
        """