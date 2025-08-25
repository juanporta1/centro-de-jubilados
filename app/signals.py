from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Member, MemberActivityLog
from django.utils import timezone

@receiver(pre_save, sender=Member)
def log_member_status_change(sender, instance, **kwargs):
  if not instance.pk:
    return
  
  # Obtenemos el registro actual de la DB
  old_instance = sender.objects.get(pk=instance.pk)
  
  if old_instance.isActive != instance.isActive:
    # El estado ha cambiado, creamos un log
    MemberActivityLog.objects.create(member=instance, activity = instance.isActive, date = timezone.now)
  