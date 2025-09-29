# Question 3:- By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.


# Ans:-
# 1. By default, Django signals do not run in the same database transaction as the caller. 
# 2. This is because Django operates in autocommit mode by default, where each database query is treated as its own transaction and is committed immediately



# Example:-



from django.db import connection, transaction
# from myapp.models import Item

def prove_autocommit():
    Item.objects.all().delete()

    Item.objects.create(name="autocommit-demo")

    print("Autocommit ON? ->", connection.get_autocommit())

    # Have NO effect because commit already happened
    transaction.rollback()

   # This will return 'True' because in 'autocommit mode' 
   # the create query is executed immediately, so the rollback has no effect.
    exists = Item.objects.filter(name="autocommit-demo").exists() 
    print("Does 'autocommit-demo' still exist after rollback? ->", exists)

