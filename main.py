# list
string_var = ['H','e','l','l','o']

# cascading Hello
for i in range(len(string_var)):
    for k in range(i+1): # i starts at 0
        print(string_var[k], end="")
    print()

# cascading again but with slicing
# cooler because no nested for-loop
cooler_string = "World!"
for i in range(len(cooler_string)):
    print(cooler_string[:i+1]) # exclusive end index
