alphabets = "ABCDEFGHIKLMN"

String_input = input("Enter a string :")
shift_input = int(input("enter in a value to shift by : "))

input_length = len(String_input)

string_output = ""

for i in range (input_length):
    character = String_input(i)
    location_of_character = alphabets.find(character)
    new_location = (location_of_character + shift_input) % 26
    string_output = string_output + alphabets(new_location)

print("Encrypted text : ", string_output)