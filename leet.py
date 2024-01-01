leet_dict = {'A': '4', 'B': '8', 'C': '<', 'E': '3', 'G': '9', 'H': '#', 'I': '1', 'L': '|', 'O': '0', 'S': '$', 'T': '7', 'Z': '2'}

str = input("Enter your text : ")
stri = str.upper()
leet_char = [leet_dict[x] for x in stri if x in leet_dict]
leet_sentence = "".join(leet_char)
print(leet_sentence)
