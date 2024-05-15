import pandas

#todo create a dictionary with alphabets
file=pandas.read_csv("nato_phonetic_alphabet.csv")
length=file["letter"].to_list().__len__()
dict2={file.iloc[i][0] : file.iloc[i][1 ]for i in range(0,length)}
user_input=input("Enter a word \n")
word_list=[x for x in user_input]

new_dict={x:dict2[x.upper()] for x in word_list}
for x,y in new_dict.items():
    print(f"{x} : {y}")
