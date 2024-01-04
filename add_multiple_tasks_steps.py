from behave import given, when, then
from todo_list import ToDoListManager

@given("the to-do list is empty:")
def step_given_empty_todo_list(context):
    context.todo_manager = ToDoListManager()

@when('the user adds tasks:')
def step_when_user_adds_multiple_tasks(context):
    for row in context.table:
        context.todo_manager.add_task(row['Task'])