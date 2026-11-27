from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# --- Harith's pages ---
def today_page(request):
    return render(request, 'today.html')


# --- Stefanos's pages ---
def courses_page(request):
    return render(request, 'courses.html')


def add_course_page(request):
    return render(request, 'add_course.html')


def course_details_page(request, course_id):
    return render(request, 'course_details.html', {'course_id': course_id})


# --- Not assigned yet ---
def calendar_page(request):
    return render(request, 'calendar.html')