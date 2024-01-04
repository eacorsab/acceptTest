from behave import given, when, then
from todo_list import ToDoListManager

@given('the to-do list contains tasks:')
def step_given_todo_list_contains_tasks(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        context.todo_manager.add_task(row['Task'])


@when('the user clears the to-do list')
def step_when_user_clears_todo_list(context):
    context.todo_manager.clear_tasks()

@then('the to-do list should be empty')
def step_then_todo_list_should_be_empty(context):
    assert not context.todo_manager.tasks, "The to-do list is not empty as expected."