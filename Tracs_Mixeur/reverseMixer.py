import csv
from datetime import datetime

#Result
EvilMan = 'DLX26mmbPunP15JjTUbqj2M5ZPASmQ5lqi'

targetAddr = 'D8t5PGChNNidpcEwvoGTqFnEymqKeu3cSb'
valueOnTarget = 1736746.5599999996 

def find():
    PossibleTarget = []
    Amounts = {}
    childs =[targetAddr]
    with open('output.csv') as f:
        file = csv.reader(f)

        for line in file:
            lst  = line[0].split(";")
            From = lst[0]
            To = lst[1]
            Value = float(lst[2])
            fee = float(lst[5])

            if(To in childs):
                childs.append(From)
                if(To in Amounts):
                    Amounts[To] -= Value
                else:
                    Amounts[To] = -Value
                
                if(From in Amounts):
                    Amounts[From] += Value
                else:
                    Amounts[From] = Value

                if(Amounts[From] >= valueOnTarget):
                    if(From not in PossibleTarget):
                        PossibleTarget.append(From)
        
        print(PossibleTarget)





if __name__ == "__main__":
    find()