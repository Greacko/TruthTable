#Creation of lists to store position______________________________________
def offsetin(input_dic):
    position = 40*(2**(len(input_dic.keys())))
    global endpoint; endpoint = position
    for i in input_dic.keys():
        #leng = len(input_dic.keys())
        position //= 2
        input_dic[i] = [position,0]


#findingAmountOfOperations________________________________________________
def paranumfunc(str):
    counter = 0
    for i in str:
        if i == '(':
            counter += 1
    return counter

#listOfOperators__________________________________________________________
def xorfunc():
    pass

def andfunc(a,b):
    if (a == 1 and b == 1):
        return 1
    else:
        return 0

def orfunc(a,b):
    if (a == 0 and b == 0):
        return 0
    else:
        return 1

#findingExcutions__________________________________________________________
def findParentheses(string,paraNum):
    for j in range(paraNum):
        curo = ''
        nexto = ''
        for i in range(len(string)):
            if string[i] ==")":
                nexto = i
                evaluate = string[curo+1:nexto].split()

                if evaluate[1] == 'and':
                    result = andfunc(input_dic[evaluate[0]][1],input_dic[evaluate[2]][1])
                    var = 'variableNumber' + str(j)
                    exec('input_dic[var]= ["null",result]')
                    string = string[0:curo] + var + string[nexto + 1:]
                    
                elif evaluate[1] == 'or':
                    result = orfunc(input_dic[evaluate[0]][1],input_dic[evaluate[2]][1])
                    var = 'variableNumber' + str(j)
                    exec('input_dic[var]= ["null",result]')
                    string = string[0:curo] + var + string[nexto + 1:]

                break

            elif string[i] =="(":
                curo = i

    finalValue = input_dic[var][1]
    return finalValue


#inputSettings_____________________________________________________________
def inputSettings(finalInfo, unitTime,locallist):
    
    for key in locallist:
        if unitTime == 0:
            input_dic[key][1] = 0
        elif (int(unitTime)%int(input_dic[key][0])) == 0:
            input_dic[key][1] = 0
        elif unitTime%(input_dic[key][0]//2) == 0:
            input_dic[key][1] = 1

#printVariableInformation__________________________________________________
def printVarInfo(finalInfo):
    for j in range(len(finalInfo[0][1])):
        print("The values under column #: " + str(j+1))
        for i in range(finalInfo[-1][0]+1):
            print(finalInfo[i][1][j])
        print()


#printMatrixInformation__________________________________________________
def printResInfo(finalInfo):
    print("Here are the results for the command:")
    for i in range(finalInfo[-1][0]+1):
        print(str(finalInfo[i][2][0]))

#storeInformationInMatrix__________________________________________________

def matrixMake(command, paraNum, endpoint, finalInfo):
    currentpoint = 0
    count = 0
    locallist = []
    for key in input_dic.keys():
        if key == 'varialbeNumber0':
            break
        else:
            locallist.append(key)

    for i in range(endpoint//40):
        finalInfo.append([count,[],[]])
        for j in locallist:
            inputSettings(finalInfo, currentpoint,locallist)
            finalInfo[count][1].append(input_dic[j][1])
        finalInfo[count][2].append(findParentheses(command,paraNum))

        count +=1
        currentpoint += 20

#mainProgram_______________________________________________________________
'''variables'''
input_dic = {}
finalInfo = []

command = input("Please input the command: ")

for i in range(len(command)):
    if command[i] =="(":
        if command[i+1] != "(":
            input_dic[command[i+1]] = []
    if command[i] == ")":
        if command[i-1] !=")":
            input_dic[command[i-1]] = []

offsetin(input_dic)
paraNum = paranumfunc(command)

ask = True
matrixMake(command, paraNum, endpoint, finalInfo)
while ask:
    printOptions = input("Put 1 for variable printout or 2 for result printout or 'end' to stop the program: ")
    
    if printOptions == '1':
        printVarInfo(finalInfo)
    elif printOptions == '2':
        printResInfo(finalInfo)
    elif printOptions == 'end':
        ask = False


