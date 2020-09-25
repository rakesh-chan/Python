#script with prompt

from sys import argv

script, user_name = argv
prompt = '>'

print ("HI", user_name, "Iam script", script)
print("i would like to ask u a few questions")
print("do you like me? ", (user_name))
likes = input(prompt)
print("where do u live?", user_name)
lives = input(prompt)
print ("what icecream u love?", user_name)
love = input(prompt)

print ("""Alright, so you said %r about liking me. You live in %r and you like %r""" %(likes,lives,love))
