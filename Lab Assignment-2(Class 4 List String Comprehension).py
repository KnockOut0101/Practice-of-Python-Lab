string_input = input("Enter a string:-")
string_input_split = string_input.split()

spaces = [x for x in string_input if x == ' ']
word_5 = [x for x in string_input_split if len(x)< 5]
len_dict = {word: len(word) for word in string_input_split}


print("Blank Count :-",spaces.count(' '),"\n")

print("Word Count (less than 5 letters):-",word_5,"\n")

print("Word Lenght",len_dict,"\n")