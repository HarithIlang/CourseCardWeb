from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseForm
from .models import Course

# Create your views here.
def home(request):
    return render(request, 'home.html')

# --- Harith's pages ---
def today_page(request):
    return render(request, 'today.html')

# --- Stefanos's page: one page with the add box, the course list and the selected course ---
def courses_page(request, course_id=None):

    # If the user is not logged in, show the "please log in" message
    if not request.user.is_authenticated:
        return render(request, 'courses.html', {'needs_login': True})

    # Only show the logged in student's courses, most recently added first
    # (each new course gets a higher id, so '-id' puts the newest at the top)
    courses = Course.objects.filter(user=request.user).order_by('-id')

    # Starts with no course picked.
    selected = None

    # If the course id is valid select it, otherwise show error 404
    if course_id is not None:
        selected = get_object_or_404(Course, id=course_id, user=request.user)

    # When the user clicks "Add course", validate and save the form
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            # Builds course from form
            course = form.save(commit=False)
            # Sets user as course owner
            course.user = request.user
            #Saves course to database
            course.save()
            # Open the new course on the right side
            return redirect('course_details', course_id=course.id)
    else:
        # Case for when the page opens without user clicking "Add course"
        form = CourseForm()

    return render(request, 'courses.html', {
        'form': form,
        'courses': courses,
        'selected': selected,
    })


# Same page, but with one course picked (the number in the address) on the right side
def course_details_page(request, course_id):
    return courses_page(request, course_id)


# Same page, but this course's card opens up into a form so it can be changed
def course_edit_page(request, course_id):

    # If the user is not logged in, show the "please log in" message
    if not request.user.is_authenticated:
        return render(request, 'courses.html', {'needs_login': True})

    # Only let the owner edit the course; anyone else gets a 404 error
    course = get_object_or_404(Course, id=course_id, user=request.user)
    # Most recently added first, same as the main page
    courses = Course.objects.filter(user=request.user).order_by('-id')

    # prefix='edit' gives the edit boxes their own names, so they don't clash
    # with the "Add Course" box that is on the same page

    # When the user clicks "Save", check the form and update the same course
    if request.method == 'POST':
        # instance=course means "change this course" instead of making a new one
        edit_form = CourseForm(request.POST, instance=course, prefix='edit')
        if edit_form.is_valid():
            edit_form.save()
            # Go back to the course on the right side
            return redirect('course_details', course_id=course.id)
    else:
        # Page just opened: fill the form with the course's current info
        edit_form = CourseForm(instance=course, prefix='edit')

    return render(request, 'courses.html', {
        # The "Add Course" box at the top stays empty for adding a new course
        'form': CourseForm(),
        'edit_form': edit_form,
        'courses': courses,
        'selected': course,
        'editing': course,
    })


# Deletes a course when the user clicks "Delete" (only on POST, so a plain link can't delete)
def course_delete(request, course_id):

    # If the user is not logged in, show the "please log in" message
    if not request.user.is_authenticated:
        return render(request, 'courses.html', {'needs_login': True})

    # Only let the owner delete the course; anyone else gets a 404 error
    course = get_object_or_404(Course, id=course_id, user=request.user)

    if request.method == 'POST':
        course.delete()

    # Back to the course list either way
    return redirect('courses')


# --- Not assigned yet ---
def calendar_page(request):
    return render(request, 'calendar.html')