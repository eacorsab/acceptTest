from behave import given, when, then
from todo_list import ToDoListManager

@given("the to-do list contains")
def step_given_todo_list_with_tasks(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        context.todo_manager.add_task(row['Task'])

@when('the user marks task "{task}" as completed')
def step_when_user_marks_task_completed(context, task):
    context.todo_manager.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_then_todo_list_should_show_completed(context, task):
    for t in context.todo_manager.tasks:
        if t['description'] == task:
            assert t['completed'], f"Task '{task}' is not marked as completed in the to-do list."
