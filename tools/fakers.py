import time
import random
import string


def random_email():
    return(f"user.{time.time()}@mail.ru")

def random_password():
    return''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))