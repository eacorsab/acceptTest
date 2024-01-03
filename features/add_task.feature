Scenario: Adding a task
 Given the tasks list is empty
 When the user adds a task "Do Homework"
 Then the to-do list should contain "Do Homework"