import json
import random
import string
from pathlib import Path




class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
         with open(database)as fs:
            data = json.loads(fs.read())
        else:
           print("no such file exist")    
    except Exception as err:
        print(f"an exception occured as {err}")        

    @classmethod
    def __update(cls):
       with open(cls.database,'w')as fs :
          fs.write(json.dumps(Bank.data))



    @classmethod
    def __accountgenerate(cls):
       alpha = random.choices(string.ascii_letters,k = 3)
       num = random.choices(string.digits, k = 3)
       spchar = random.choices("!@#$%^&*",k = 1)
       id = alpha + num + spchar
       random.shuffle(id)
       return"".join(id)



    def Createaccount(self):
        
        info = {
           "name": input("tell your name :-"),
           "age": int(input("tell your age :-")),
           "email": input("tell your email:-"),
           "pin" : int(input("tell your pin :-")),
           "accountNo":Bank.__accountgenerate(),
           "balence": 0

        }
        if info['age'] < 18 or len(str(info['pin'])) !=4:
           print("sorry you cannot create your account")
        else:
           print("account has been created succesfully")
           for i in info:
              print(f"{i} : {info[i]}")
           print("please nate down your account number")  
            
           Bank.data.append(info)

           Bank.__update()

    def depositmoney(self):
       accnumber = input("tell your account number")
       pin = int(input("tell your pin"))

       userdata = [i for i in Bank.data if['accountNo'] == accnumber and i['pin'] == pin ]
       if userdata == False:
          print("sorry no data found")
       else:
          amount = int(input("how much you wnt to deposit")) 
          if amount > 10000 or amount < 0 :
             print("sorry the amount is too much you can deposit below 10000")

          else:
             print(userdata)
             userdata[0]['balance'] += amount
             Bank.__update()
             print("amount dposited successfully")





user = Bank()

print("press 1 for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawling the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :-"))

if check == 1:
    user.Createaccount()
if check == 2:
   user.depositmoney()
   