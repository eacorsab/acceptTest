from behave import given, when, then
from todo_list import ToDoListManager

@given("the to-do list is")
def step_given_todo_list_with_tasks(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        context.todo_manager.add_task(row['Task'])

@when('the user removes the task "{task}"')
def step_when_user_removes_task(context, task):
    context.todo_manager.remove_task(task)

@then('the to-do list should not contain "{task}"')
def step_then_todo_list_should_not_contain(context, task):
    tasks = [t['description'] for t in context.todo_manager.tasks]
    assert task not in tasks, f"Expected task '{task}' to be removed from the to-do list."
