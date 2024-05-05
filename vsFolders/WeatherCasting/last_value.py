import random
import time

previous = None
while True:
    print("old", previous)
    other_segment_angles = random.randint(0,9)
    print("new", other_segment_angles)

    previous = other_segment_angles
    time.sleep(2)