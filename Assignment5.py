content = '''The quick brown fox jumps over the lazy dog.
Python is a powerful programming language used in web development, data science, and automation.
42 is the answer to life, the universe, and everything.
Tomorrow's weather forecast: Sunny with a chance of code.
Did you know? Bananas are berries, but strawberries aren't!'''

with open("sample.txt", "w") as file:
    file.write(content + "\n")

with open("sample.txt", "a") as file:
    file.write("\nThis line is appended later.")

with open("sample.txt", "r") as file:
    content = file.read()
    print("Reading file after writing and appending:")
    print(content)

with open("sample.txt", "a+") as file:
    file.write("Appending content using a+ mode.\n")
    file.seek(0)
    content = file.read()
    print("Reading file after append and read:")
    print(content)
