from django.shortcuts import render

from .stack import SPACE_COMPLEXITY, TIME_COMPLEXITIES, Stack


def index(request):
    raw_stack = request.session.get('stack', [])
    stack = Stack(raw_stack)
    message = ''

    if request.method == 'POST':
        if 'push' in request.POST:
            name = request.POST.get('name')
            student_id = request.POST.get('student_id')
            if name and student_id:
                stack.push({'name': name, 'id': student_id})
                message = f"Added student {name}"
            else:
                message = "Please provide name and ID"
        elif 'pop' in request.POST:
            popped = stack.pop()
            if popped:
                message = f"Removed student {popped['name']}"
            else:
                message = "Stack is empty"
        elif 'peek' in request.POST:
            top = stack.peek()
            if top:
                message = f"Top student: {top['name']} (ID: {top['id']})"
            else:
                message = "Stack is empty"
        elif 'is_empty' in request.POST:
            message = "Stack is empty" if stack.is_empty() else "Stack is not empty"
        elif 'size' in request.POST:
            message = f"Stack size: {stack.size()}"

    request.session['stack'] = stack.to_list()

    return render(
        request,
        'students/index.html',
        {
            'stack': stack.to_list(),
            'message': message,
            'space_complexity': SPACE_COMPLEXITY,
            'time_complexities': TIME_COMPLEXITIES,
        },
    )
