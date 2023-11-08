import re
import matplotlib.pyplot as plt

# Read the text file and extract "i" and "n" values using regular expressions
with open("output.txt", "r") as file:
    data = file.read()

# Use regular expressions to find all "(i, n)" pairs
matches = re.findall(r'\((\d+), ([\d.]+)\)', data)

# Extract "i" and "n" values and convert them to integers and floats, respectively
i_values = [int(match[0]) for match in matches]
n_values = [float(match[1]) for match in matches]

# Create a bar graph of "i" vs "n"
plt.bar(i_values, n_values)
plt.xlabel("i Values")
plt.ylabel("n Values")
plt.title("Bar Graph of i vs n")
plt.show()
