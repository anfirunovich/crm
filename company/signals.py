from django.core.mail import send_mail
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from company.models.employee import JobTitle


@receiver(m2m_changed, sender=JobTitle)
def add_employee_in_company(
        sender,
        instance,
        action,
        reverse,
        model,
        pk_set,
        *args,
        **kwargs,
):
    if action == 'post_add' and reverse:
        hired_employees = model.objects.filter(id__in=pk_set).all()

        hr_employees_ids = JobTitle.objects.filter(
            job_title="HR", company=instance
        ).values_list("employee_id", flat=True).all()

        hr_employees_emails = model.objects.filter(
            id__in=hr_employees_ids
        ).values_list("email", flat=True).all()

        send_mail(
            subject=f"New hiring inside {instance.name}",
            message=(
                f"In {instance.name} add new employee: "
                f"{','.join([hired_employee.full_name for hired_employee in hired_employees])}"
            ),
            from_email="a@gmail.com",
            recipient_list=hr_employees_emails,
        )
