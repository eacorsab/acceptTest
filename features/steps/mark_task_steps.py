from behave import given, when, then
from todo_list import ToDoListManager

@given('a set of todo list')
def step_impl(context):
    context.todo_manager = ToDoListManager()
    
@then('the status of task "{task}" should change to "Completed" and be updated')
def step_impl(context, task):
    # Implementa aquí la lógica para verificar si el estado de la tarea ha cambiado a "Completado" y se ha actualizado
    pass