import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal started processing.")
    time.sleep(5)  # Simulating a time-consuming task
    print("Signal finished processing.")

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal is running within the same database transaction.")
    else:
        print("Signal is not running within the same database transaction.")
