from behave import given, when, then
from todo_list import ToDoListManager

@given("the to-do list is empty")
def step_given_empty_todo_list(context):
    context.todo_manager = ToDoListManager()

@when('the user adds a task "{task}"')
def step_when_user_adds_task(context, task):
    context.todo_manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_then_todo_list_should_contain(context, task):
    tasks = [t['description'] for t in context.todo_manager.tasks]
    assert task in tasks, f"Expected task '{task}' not found in the to-do list."
