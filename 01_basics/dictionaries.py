
# dictionaries are key value pairs
weekDays = {
# key should be unique
#    keys: values
    "sun":"Sunday",
    "mon":"Monday",
    "tue":"Tuesday",
    "wed":"Wednesday",
    "thu":"Thursday",
    "fri":"Friday",
    "sat":"Saturday",
}

# print the value of given key
print(weekDays["sat"])
# print the value of given key
print(weekDays.get("mon"))
# print the value of key, if key not found, print the default value ("not a valid key")
print(weekDays.get("jan","Not a valid key"))