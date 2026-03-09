from django.shortcuts import render

# Create your views here.
def dtl_syntax_demo(request):
    context = {
        'name': "Someone",
        'age': 24,
        'courses': ["Python", "Django", "Git", "SQL", "FastAPI", "HTML/CSS"],
        'is_logged_in': True,
        'no_of_messages': 3,
        'students_grades': {'Pelumi': 'A', "Olumide": "B", "Joshua": "C", "Francis": "D", "Adil": "E"},
        'library': [
            {"title": "Title 1", "author": "Author 1"},
            {"title": "Title 2", "author": "Author 2"},
            {"title": "Title 3", "author": "Author 3"},
        ]
    }
    return render(request, "dtl/dtl.html", context)