from django import forms
from .models import Course


DAY_CHOICES = [
    ('Mon', 'Mon'),
    ('Tue', 'Tue'),
    ('Wed', 'Wed'),
    ('Thu', 'Thu'),
    ('Fri', 'Fri'),
    ('Sat', 'Sat'),
]
ALL_DAYS = [day for day, _ in DAY_CHOICES]

# The database column only holds 20 characters, so these day groups are saved in short form
SHORT_FORMS = {
    'Mon - Fri': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Mon - Sat': ALL_DAYS,
}


class CourseForm(forms.ModelForm):
    # Meeting days is a list of checkboxes (shown as a drop-down on the page).
    # It is still saved in the database as text like "Mon, Wed".
    meetingDays = forms.MultipleChoiceField(
        choices=DAY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Meeting Days',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # When editing, turn the saved text back into ticked boxes
        saved = self.instance.meetingDays if self.instance and self.instance.pk else ''
        if saved in SHORT_FORMS:
            self.initial['meetingDays'] = SHORT_FORMS[saved]
        elif saved:
            self.initial['meetingDays'] = [day.strip() for day in saved.split(',')]

    def clean_meetingDays(self):
        days = self.cleaned_data['meetingDays']
        # Keep the days in week order, no matter what order they were ticked in
        days = [day for day in ALL_DAYS if day in days]
        for short, group in SHORT_FORMS.items():
            if days == group:
                return short
        text = ', '.join(days)
        # Five days with spaces is 23 characters, too long for the column, so drop the spaces
        if len(text) > 20:
            text = ','.join(days)
        return text

    class Meta:
        model = Course
        # user is left out on purpose: the view fills it in with whoever is logged in
        fields = [
            'code', 'name', 'meetingDays', 'building', 'startTime', 'endTime',
            'room', 'professorName', 'officeHours', 'officeLocation',
        ]
        labels = {
            'code': 'Course Code',
            'name': 'Course Name',
            'startTime': 'Start Time',
            'endTime': 'End Time',
            'professorName': 'Professor',
            'officeHours': 'Office Hours',
            'officeLocation': 'Office Location',
        }
        widgets = {
            # type="time" gives a time picker in the browser
            'startTime': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
            'endTime': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),
        }

    def clean(self):
        cleaned = super().clean()
        start = cleaned.get('startTime')
        end = cleaned.get('endTime')
        if start and end and end <= start:
            self.add_error('endTime', 'End time must be after the start time.')
        return cleaned
