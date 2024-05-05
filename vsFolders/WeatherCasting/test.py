import os
import random
import time
from secondtester import random_gen

def update_checker():

    while True:
        time.sleep(3)
        random_gen()

update_checker()