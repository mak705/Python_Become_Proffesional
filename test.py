studentDict = {'Jeff':[78,88,93],
               'Alex':[92,76,88],
               'Sam':[89,92,93]}
			   
def main():
    print("""
    Welcome to Grade Central

    [1] - Enter Nam
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    [5] - Add new name
    """)

    action = input('What would you like to do today? (Enter a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    elif action == '5':
        addname()
    else:
        print('No valid choice was given, try again')

def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')

    print(studentDict)

def removeStudent():
    nameToRemove = input('What student to remove?: ')
    if nameToRemove in studentDict:
        print('removing student...')
        del studentDict[nameToRemove]

    print(studentDict)

def studentAVGs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)

        print(eachStudent,'has an average grade of:',avgGrade)
    



def addname():
    nameToEnter = input('Student Name: ')
    
    if nameToEnter in studentDict:
        print('Student name already exist.')    
    else:
        gradeToEnter = int(input('Grade: '))
        print('Adding name...')
        studentDict[nameToEnter] = [gradeToEnter]
    print(studentDict)  
	

main()

















