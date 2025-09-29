# Question 2:  Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.



# Ans:-  Yes, By default Django signals run synchronously and in the same thread as the code that sends the signal


# Example:-
# code:


import threading
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def receiver_1(sender, **kwargs):
    print(f"Receiver_1 running in thread: {threading.current_thread().name}")

@receiver(request_finished)
def receiver_2(sender, **kwargs):
    print(f"Receiver_2 running in thread: {threading.current_thread().name}")


print(f"Caller running in thread: {threading.current_thread().name}")
request_finished.send(sender=None)



# OutPut:-

# Caller running in thread: MainThread
# Receiver_1 running in thread: MainThread
# Receiver_2 running in thread: MainThread

