
class Grade:
    def __init__(self):
        Grade.A = 5
        Grade.B = 4
        Grade.C = 3
        Grade.D = 2
        Grade.E = 1
        Grade.F = 0
        Grade.item = []
        Grade.unit = []
        Grade.lists = []
        self.info()
        self.subject_list()
        self.grade_asign()
        self.result()
        self.calculation()
        

    def info(self):
        print('Hi welcome to grade score program, answer the follow')
        Grade.Fn = input('your first name?:')
        Grade.Sn = input('Your surname?:')
        Grade.On = input('Your other name?:')
        Grade.reg = input('what is your matric number:')
        Grade.faculty = input('What faculty:')
        Grade.department = input('Which department:')
        Grade.option = input('what is your course of study:')
        

    def subject_list(self):
        print('please kindly list the subject your offer in your previous semeter')
        global subject
        subject = {}
        Grade.count = 0
        Grade.condition = input('Do you wish to continue y/n:')
        

        while Grade.condition != "n":
            print('type "quit" to quit listting')
            Grade.sub = input('enter the subject:')
            if Grade.sub =='quit':
                break
            else:
                Grade.Un = int(input('what is the unit of'+' ' +Grade.sub+':'))
                Grade.score = input('your grade in the subject:')
                subject[Grade.sub.upper()] = Grade.score.capitalize()
                Grade.unit.append(Grade.Un)
                Grade.count +=1
        Grade.asign = subject.values()
        Grade.dict_len = len(subject)


    def grade_asign(self):
        for var in subject.values():
            if var == 'A':
                vars =  Grade.A
            elif var == 'B':
                vars = Grade.B
            elif var == 'C':
                vars = Grade.C
            elif var == 'D':
                vars = Grade.D
            elif var == 'E':
                vars = Grade.E
            else:
                vars = Grade.F
            Grade.lists.append(vars)
                
        
        subject_length = len(subject)
        score_length = len(self.unit)
        if subject_length == score_length:
            for i in range(score_length):
                vars = self.lists[i] * Grade.unit[i]
                Grade.item.append(vars)

        print(self.item)
        print(sum(self.item))
        
        total_unit = sum(self.unit)
        
               
    def calculation(self):
        self.Total_unit = sum(self.unit)
        self.total_mark = sum(self.item)
        self.grade_score = self.total_mark/self.Total_unit
        print('Your GP is:' + self.grade_score)



    def result(self):
        print('NAME:'+Grade.Fn.upper(),' '+Grade.Sn.upper(),' '+Grade.On.upper())
        print('FACULTY:'+Grade.faculty.upper())
        print('DEPARTMENT:'+Grade.department.upper())
        print('OPTION:'+Grade.option.upper())
        print('REG, NUMBER:'+ Grade.reg.upper())

        for score, subjects in subject.items():
            print(f"Your score of {score} is {subjects}")
            
        
            
        
            


my_grade=Grade()