from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# --- Harith's pages ---
def today_page(request):
    return render(request, 'today.html')


# --- Stefanos's page: one page with the add box, the course list and the selected course ---
def courses_page(request):
    return render(request, 'courses.html')


# Same page, but with one course picked (the number in the address) on the right side
def course_details_page(request, course_id):
    return render(request, 'courses.html', {'selected_id': course_id})


# --- Not assigned yet ---
def calendar_page(request):
    return render(request, 'calendar.html')