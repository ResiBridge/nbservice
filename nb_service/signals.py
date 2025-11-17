from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

from dcim.models import Device
from virtualization.models import VirtualMachine

from . import models

def handle_IC_assigned_Object_delete(sender,instance,*args,**kwargs):
    related_ics = models.IC.objects.filter(
        assigned_object_type=ContentType.objects.get_for_model(instance),
         assigned_object_id=instance.id)
    for ic in related_ics:
        ic.delete()


def handle_Service_create(sender, instance, created, *args, **kwargs):
    """
    Auto-create an Infrastructure Component when a Service is created.
    This allows the service to be used in relations immediately.
    """
    if created:
        # Check if IC already exists for this service
        service_ct = ContentType.objects.get_for_model(models.Service)
        existing_ic = models.IC.objects.filter(
            service=instance,
            assigned_object_type=service_ct,
            assigned_object_id=instance.id
        ).first()

        if not existing_ic:
            # Create IC for the service
            models.IC.objects.create(
                service=instance,
                assigned_object_type=service_ct,
                assigned_object_id=instance.id
            )


device_delete = receiver(post_delete, sender=Device)(handle_IC_assigned_Object_delete)
vm_delete = receiver(post_delete, sender=VirtualMachine)(handle_IC_assigned_Object_delete)
app_delete = receiver(post_delete, sender=models.Application)(handle_IC_assigned_Object_delete)
service_create = receiver(post_save, sender=models.Service)(handle_Service_create)
