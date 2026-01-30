import pandas as pd

df = pd.read_csv("Akinator_Dataset.csv")

characters = df['Name'].tolist()
#print(characters)

qus = df.columns[1:]
#print(qus)

print("Wellcome to Akinator !")
print("Think of a character among these guys :")

ind = 1
for character in characters :
    print(str(ind) +". " + character )
    ind = ind + 1

probable_characters =  df.copy()
i=0
#main loop
while i < len(qus):
    question = qus[i]
    ans = input(qus[i] + " (yes/no): ").strip().lower()

    if ans == "yes":
        result = 1
        i += 1  # move to next question
    elif ans == "no":
        result = 0
        i += 1  # move to next question
    elif ans == "stop" :
        break
    else :
        print("Enter valid input (yes/no).")
        continue

    
    for index,row in probable_characters.iterrows() :

        if row[question] != result :
            probable_characters = probable_characters.drop(index)
    
    
    if len(probable_characters) == 1 :
        print("\n I got it !, You are thinking of",probable_characters['Name'].values[0] + '\n' )
        break




