weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# result = {new_key:new_value for key,value in dict.items() if test }


def convert(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f

#option 1
weather_f = {day:convert(temp_c) for day,temp_c in weather_c.items()}

#option 2
weather_f = {day:(temp_c * 9/5) +32 for day,temp_c in weather_c.items()}

print(weather_f)