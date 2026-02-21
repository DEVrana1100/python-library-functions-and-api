print("Hello")        # Prints output to the screen
input("Enter name")   # Takes input from user as string
len("Python")         # Returns length (6)
type(10)              # Returns data type
int("5")              # Converts to integer
float("3.5")          # Converts to float
str(100)              # Converts to string
range(5)              # Generates numbers 0 to 4
sum([1,2,3])          # Adds all elements
max([1,2,3])          # Largest value
min([1,2,3])          # Smallest value
sorted([3,1,2])       # Sorts list

lst = [1, 2, 3]

lst.append(4)        # Adds element at end
lst.extend([5,6])    # Adds multiple elements
lst.insert(1, 10)    # Inserts at index
lst.remove(2)        # Removes value
lst.pop()            # Removes last element
lst.clear()          # Removes all elements
lst.sort()           # Sorts list
lst.reverse()        # Reverses list
lst.append(lst1.upper()) #to convert the names in the list to uppercase

STRING: 
s = " python "
s.upper()        # Converts to UPPERCASE
s.lower()        # Converts to lowercase
s.capitalize()  # First letter capital
s.title()       # First letter of each word capital
s.swapcase()    # Upper ↔ lower
len(s)           # Returns length of string
s.strip()        # Removes spaces from both sides
s.lstrip()       # Removes left spaces
s.rstrip()       # Removes right spaces
s.find("World")      # Returns index (or -1 if not found)
s.rfind("o")         # Finds from right
s.index("hello")    # Like find(), but gives ERROR if not found
s.count("l")        # Counts occurrences
s.replace("hello", "hi")   # Replaces text
s.split()           # Splits string into list (by spaces)
s.split(",")        # Split by comma

words = ["Hello", "Rana"]
" ".join(words)     # Joins list into string
s.isupper()     # All uppercase?
s.islower()     # All lowercase?
s.isalpha()     # Only letters?
s.isdigit()     # Only digits?
s.isalnum()     # Letters + digits?
s.isspace()     # Only spaces?
s.startswith("hello")   # Starts with?
s.endswith("123")       # Ends with?
s.center(30)        # Centers text
s.ljust(30)         # Left align
s.rjust(30)         # Right align
s.zfill(5)          # Adds zeros at start
s.removeprefix("  ")   # Removes prefix
s.removesuffix("123")  # Removes suffix
s.encode()         # Converts string to bytes
name = "Rana"
age = 18

"My name is {} and age is {}".format(name, age)
f"My name is {name} and age is {age}"   # BEST way
s.isnumeric()      # Numbers only
s.isdecimal()      # Decimal numbers only
s.isprintable()    # Printable characters?
s.partition("World")   # Splits into 3 parts
s.rpartition("o")      # From right
table = str.maketrans("aeiou", "12345")
s.translate(table)     # Replaces characters

# Creating dictionary
d = {
    "name": "Rana",
    "age": 18,
    "branch": "CSE"
}

# Accessing values
d["name"]              # Access value using key (error if key missing)
d.get("age")           # Safe access
d.get("marks", 0)      # Default value if key not found

# Adding / Updating values
d["college"] = "KIIT"  # Add new key-value
d["age"] = 19          # Update existing key
d.update({"city": "BBSR", "age": 20})  # Add/update multiple values

# Removing elements
d.pop("age")           # Remove key and return value
d.popitem()            # Remove last inserted item
del d["branch"]        # Delete specific key
d.clear()              # Remove all items

# Length of dictionary
len(d)                 # Number of key-value pairs

# View methods
d.keys()               # Returns all keys
d.values()             # Returns all values
d.items()              # Returns (key, value) pairs

# Copying dictionary
d2 = d.copy()          # Shallow copy

# Creating dictionary from keys
keys = ["a", "b", "c"]
dict.fromkeys(keys, 0) # {'a':0, 'b':0, 'c':0}

# Checking key existence
"name" in d            # True if key exists
"marks" in d           # False if key not exists

# Looping through dictionary
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

# Nested dictionary
student = {
    "name": "Rana",
    "marks": {
        "maths": 85,
        "physics": 78
    }
}
student["marks"]["maths"]   # Access nested value

# Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}

# Key rules
# - Keys must be unique
# - Keys can be string, int, tuple
# - Keys CANNOT be list or dict

# Duplicate keys overwrite value
d3 = {"a": 1, "a": 2}   # {'a': 2}

s = {1,2,3}

s.add(4)             # Adds element
s.remove(2)          # Removes element
s.union({5,6})       # Combines sets
s.intersection({3})  # Common elements

f = open("file.txt", "r")   # Opens file
data = f.read()            # Reads content
f.close()                  # Closes file

# Best way
with open("file.txt","w") as f:
    f.write("Hello")       # Writes safely
    
class Student:
    def __init__(self, name):
        self.name = name   # Constructor

    def greet(self):
        print("Hi", self.name)

s = Student("Rana")
s.greet()

import numpy as np

a = np.array([1,2,3])      # Creates array
np.zeros(3)               # All zeros
np.ones(3)                # All ones
np.mean(a)                # Average
np.sum(a)                 # Sum
np.random.randint(1,10)   # Random number

import pandas as pd

df = pd.read_csv("data.csv")  # Loads CSV
df.head()                     # First 5 rows
df.info()                     # Data info
df.describe()                 # Statistics
df.isnull()                   # Missing values
df.dropna()                   # Remove missing rows
df.fillna(0)                  # Fill missing

import matplotlib.pyplot as plt

plt.plot([1,2,3],[4,5,6])   # Line graph
plt.bar([1,2,3],[3,2,1])    # Bar graph
plt.title("Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

import requests

r = requests.get("https://api.github.com")
r.status_code       # HTTP status
r.json()            # JSON response

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

app.run()
