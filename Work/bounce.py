# bounce.py
#
# Exercise 1.5
num_bounces = 0
current_height = 100

while num_bounces < 10:
    current_height *= 0.60
    num_bounces += 1
    print(num_bounces , round(current_height, 4))