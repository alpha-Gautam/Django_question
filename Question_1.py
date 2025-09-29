# Question 1:-By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


# ANS:-   By default, Django signals are executed synchronously.

# Example code:

import time
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def receiver_1(sender, **kwargs):
    print("Receiver_1 started...")
    time.sleep(5) 
    print("Receiver_1 finished!")

@receiver(request_finished)
def receiver_2(sender, **kwargs):
    print("Receiver_2 executed!")



request_finished.send(sender=None)

# Output:-
# Receiver_1 started...
# Receiver_1 finished
# Receiver_2 executed


