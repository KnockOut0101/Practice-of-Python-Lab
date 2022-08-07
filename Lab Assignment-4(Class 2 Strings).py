
list=[]


for i in range(5):
    string = input("Enter a String:-")
    list.append(string)

print_list=[]
count = 0
for i in range(5):
    string = list[i]
    if (len(string) > 2 and string[0] == string[len(string) - 1]):
        count = count + 1
        print_list.append(string)
    else:
        continue

print(print_list)

str_len = input("Enter String to know the characters:-")

print(str_len)

characters_count = []
for i in range(len(str_len)):
    char = str_len[i]
    count = 0
    for j in range(len(str_len)):
        if(char == str_len[j]):
            count = count + 1
            characters_count.append(str_len[j])
    characters_count.append(count)

print(characters_count)

