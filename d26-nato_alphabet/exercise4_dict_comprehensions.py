sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# result = {new_key:new_value for key,value in dict.items() if test }

result = {word:len(word) for word in sentence.split()}

print(result)