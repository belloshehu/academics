from .models import (
    Notification,
    IndividualNotification,
    NotificationDegree,
)
from django.shortcuts import get_object_or_404

def course_assignment_notification(sender, target_receiver, course):
    notification = IndividualNotification(
            title='Course assignment.',
            message=f'''You have been assigned a course with the following details:\n
                    Title: {course.title}
                    Credit unit: {course.credit_unit}
                    Department: {course.department}
                    level: {course.level}
                    Option: {course.option}
                    Semester: {course.semester}<hr>
            ''',
            sender=sender,
            target_receiver=target_receiver,
            degree=get_object_or_404(
                NotificationDegree,
                abbreviated_name='i'
            )
        )
    notification.save()


def course_deassignment_notification(sender, target_receiver, course):
    notification = IndividualNotification(
            title='Course de-assignment.',
            message=f'''You have been deassigned a course with the following details:\n
                    Title: {course.title}\n
                    Credit unit: {course.credit_unit}\n
                    Department: {course.department}\n
                    level: {course.level}\n
                    Option: {course.option}\n
                    Semester: {course.semester}
            ''',
            sender=sender,
            target_receiver=target_receiver,
            degree=get_object_or_404(
                NotificationDegree,
                abbreviated_name='i'
            )
        )
    notification.save()