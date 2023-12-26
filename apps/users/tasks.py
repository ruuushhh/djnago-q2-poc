from django_q.models import Schedule
from datetime import datetime


# Function to add a task to the import_tasks cluster
def add_import_task():
    Schedule.objects.update_or_create(
        func='apps.users.import_functions.import_data',
        cluster='import_tasks',
        defaults={
            'schedule_type': Schedule.MINUTES,
            'minutes': 24 * 60,
            'next_run': datetime.now()
        }
    )

# Function to add a task to the export_tasks cluster
def add_export_task():
    Schedule.objects.update_or_create(
        func='apps.users.export_functions.export_data',
        cluster='export_tasks',
        defaults={
            'schedule_type': Schedule.MINUTES,
            'minutes': 24 * 60,
            'next_run': datetime.now()
        }
    )

