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
s = " python "

s.lower()            # Converts to lowercase
s.upper()            # Converts to uppercase
s.strip()            # Removes spaces
s.split()            # Splits into list
s.replace("p","P")   # Replaces characters
s.find("t")          # Finds index
s.startswith("p")    # Checks start
s.endswith("n")      # Checks end

d = {"a":1, "b":2}

d.keys()             # Returns keys
d.values()           # Returns values
d.items()            # Returns key-value pairs
d.get("a")           # Safe value access
d.pop("a")           # Removes key
d.update({"c":3})    # Adds/updates items

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