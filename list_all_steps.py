from behave import given, when, then
from todo_list import ToDoListManager

@given('the to-do list contains the following tasks:')
def step_given_todo_list_contains_tasks(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        context.todo_manager.add_task(row['Description'])
        if row['Status'].lower() == 'completed':
            context.todo_manager.mark_task_completed(row['Description'])

@when('the user lists all tasks')
def step_when_list_all_tasks(context):
    context.listed_tasks = context.todo_manager.list_tasks()

@then('the output should contain:')
def step_then_output_should_contain(context):
    expected_output = context.text.strip()
    assert context.output == expected_output, f"Expected output:\n{expected_output}\nActual output:\n{context.output}"

'''
@then('show the tasks in order')
def step_then_should_see_tasks_in_order(context):
    expected_tasks = [dict(row) for row in context.table]
    actual_tasks = [{'Description': task['description'], 'Status': 'Completed' if task['completed'] else 'Pending'}
                    for task in context.listed_tasks]
    assert actual_tasks == expected_tasks
    '''