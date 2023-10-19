from kivy.app import *
from kivy.uix.floatlayout import *
from kivy.uix.button import Button
from kivy.uix.label import *
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
import sqlite3


    
class info(FloatLayout):
    def __init__(self):
        super().__init__()

        background = Image(source='workspace-with-books-stationery.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(background)

        self.btn = Button(text ="submit", size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.07})
        self.btn.bind(on_press=self.submit)
        self.add_widget(self.btn)
        
        #Creating text and inoput field for user
        self.label = Label(text= "What is your full name:", size_hint=(0.124,0.09), pos_hint={'center_x':0.1, 'center_y':0.9})
        self.entry = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.9})
        self.add_widget(self.label)
        self.add_widget(self.entry)

        self.label1 = Label(text="What is your Matric Number:", size_hint=(0.124,0.09),pos_hint={'center_x':0.128, 'center_y':0.8})
        self.entry1 = TextInput(multiline=False,size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.8})
        self.add_widget(self.label1)
        self.add_widget(self.entry1)

        self.label2 = Label(text="What faculty:", size_hint=(0.124,0.09),pos_hint={'center_x':0.1, 'center_y':0.7})
        self.entry2 = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.7})
        self.add_widget(self.label2)
        self.add_widget(self.entry2)

        self.label3 = Label(text="Which Department:", size_hint=(0.124,0.09),pos_hint={'center_x':0.1, 'center_y':0.6})
        self.entry3 = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.6})
        self.add_widget(self.label3)
        self.add_widget(self.entry3)

        self.label4 = Label(text="What is your course of study:", size_hint=(0.124,0.09),pos_hint={'center_x':0.128, 'center_y':0.5})
        self.entry4 = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.5})
        self.add_widget(self.label4)
        self.add_widget(self.entry4)

        self.label5 = Label(text="What is the name of your school:", size_hint=(0.124,0.09),pos_hint={'center_x':0.128, 'center_y':0.4})
        self.entry5 = TextInput(multiline=False, size_hint=(0.5,0.05), pos_hint={'center_x':0.55, 'center_y':0.4})
        self.add_widget(self.label5)
        self.add_widget(self.entry5)

        # Creating a database

        conn = sqlite3.connect('result.db')

        c = conn.cursor()
        #creating a table
        '''
        c.execute("""CREATE TABLE result(
                  NAME text,
                  REG NUMBER text,
                  FACULTY text,
                  DEPARTMENT text,
                  OPTION text,
                  SCHOOL text

                )""")'''
            
        '''
        c.execute("""CREATE TABLE subject1(
                  SUBJECT text,
                  UNIT integer,
                  GRADE text
                )""")'''
        conn.commit()
        conn.close()

    # creating a Function
    def submit(self, screen):
        self.name = self.entry._get_text().upper()
        self.name1 = self.entry1._get_text().upper()
        self.name2 = self.entry2._get_text().upper()
        self.name3 = self.entry3._get_text().upper()
        self.name4 = self.entry4._get_text().upper()
        self.name5= self.entry5._get_text().upper()

        self.entry.delete_selection()
        self.entry1.delete_selection()
        self.entry2.delete_selection()
        self.entry3.delete_selection()
        self.entry4.delete_selection()
        self.entry5.delete_selection()

        conn = sqlite3.connect('result.db')
        c = conn.cursor()
        
        # Inserting into the Table
        c.execute("INSERT INTO result VALUES(:self_entry, :self_entry1, :self_entry2, :self_entry3, :self_entry4, :self_entry5)",
                  {
                    'self_entry':self.name,
                    'self_entry1':self.name1,
                    'self_entry2':self.name2,
                    'self_entry3':self.name3,
                    'self_entry4':self.name4,
                    'self_entry5':self.name5
                  }
        )


        conn.commit()
        conn.close()

        Myapp.screen_manager.transition = SlideTransition(direction="left")
        Myapp.screen_manager.current = "score"

    
        #print(self.__name__0.upper(), self.__name__1.upper(), self.__name__2.upper(), self.__name__3, self.__name__4, self.__name__5.upper())

        
class score(FloatLayout):
    def __init__(self,):
        super().__init__()
        self.subject = {}
        self.unit = []

        background = Image(source='workspace-with-books-stationery.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(background)
            
        self.text1 = Label(text='click "submit" to store datas and continue to list your subjects', size_hint=(0.124,0.09), pos_hint={'center_x':0.5, 'center_y':0.9})
        self.text2 = Label(text='list the subject:', size_hint=(0.124,0.09), pos_hint={'center_x':0.128, 'center_y':0.8})
        self.sub = TextInput(size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.8})
        self.add_widget(self.text1)
        self.add_widget(self.text2)
        self.add_widget(self.sub)

        T_un = Label(text='what is the unit of:', size_hint=(0.124,0.09), pos_hint={'center_x':0.128, 'center_y':0.7})
        self.add_widget(T_un)
        self.Un = TextInput(size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.7})  
        self.add_widget(self.Un)

        T_un1 = Label(text='your grade in the subject?', size_hint=(0.124,0.09), pos_hint={'center_x':0.128, 'center_y':0.6})
        self.add_widget(T_un1)

        # Creating radiobuttons

        options = ['A','B','C','D','E','F']
        L_pos_x = 0.26
        
        for option in options:
            self.add_widget(Label(text=option, size_hint=(0.124,0.09), pos_hint={'center_x':L_pos_x, 'center_y':0.6}))
            L_pos_x +=0.04
            radiobutton = CheckBox(size_hint=(0.2,0.05),  pos_hint={'center_x':L_pos_x, 'center_y':0.6}, group='options', active=True)
            self.add_widget(radiobutton)
            radiobutton.bind(on_release=self.store)
            L_pos_x +=0.04
                
        # Creating buttons for the page
        self.btn = Button(text='NEXT', size_hint=(0.2,0.05), pos_hint={'center_x':0.9, 'center_y':0.07})
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.NEXT)

        self.btn1 = Button(text='PREVIOUS', size_hint=(0.2,0.05), pos_hint={'center_x':0.1, 'center_y':0.07})
        self.add_widget(self.btn1)
        self.btn1.bind(on_press=self.previous)

        self.btn1 = Button(text='SUBMIT', on_release=self.submit, size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.5})
        self.add_widget(self.btn1)
        self.btn1.bind(on_press=self.submit)
    
    def store(self, radiobutton):
        self.selected_value = radiobutton

    def submit(self, instance):
        self.g = self.Un._get_text()
        self.name1 = self.sub._get_text().upper()
        self.name2 = self.selected_value
        self.subject[self.name1.upper()] = self.name2
        self.unit.append(self.Un)


        conn = sqlite3.connect('result.db')
        c = conn.cursor()

        # inserting entrys
        c.execute("INSERT INTO subject1 VALUES(:subject, :unit, :grade)",
                  {
                     'subject': self.name1,
                     'unit': self.name2,
                     'grade': self.g
                  }
                  )

        self.sub = TextInput(size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.8})
        self.add_widget(self.sub)

        self.score = TextInput(size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.6})
        self.add_widget(self.score)
        
        self.Un = TextInput(size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.7})  
        self.add_widget(self.Un)

        conn.commit()
        conn.close()


    def previous(self, screen):
        Myapp.screen_manager.transition = SlideTransition(direction="right")
        Myapp.screen_manager.current = "info"

    def NEXT(self, screen):
        Myapp.screen_manager.transition = SlideTransition(direction="left")
        Myapp.screen_manager.current = "result"


class result(FloatLayout):
    def __init__(self):
        super().__init__()

        background = Image(source='workspace-with-books-stationery.jpg', keep_ratio=False, allow_stretch=True)
        self.add_widget(background)

        conn = sqlite3.connect('result.db')
        c = conn.cursor()
        
        c.execute("DELETE from result WHERE NAME = ''")
        # query the database
        c.execute("SELECT * FROM result ORDER BY oid DESC LIMIT 1")
        records = c.fetchall()
        print_record = []
        

        for record in records:

            self.Name= Label(text='NAME:'+str(record[0]), size_hint=(0.124,0.09), pos_hint={'center_x':0.228, 'center_y':0.98})
            self.reg = Label(text='REG NUMBER:'+ str(record[1]), size_hint=(0.124,0.09), pos_hint={'center_x':0.228, 'center_y':0.95})
            self.Faculty = Label(text='FACULTY:'+str(record[2]), size_hint=(0.124,0.09), pos_hint={'center_x':0.228, 'center_y':0.92})
            self.department = Label(text='DEPARTMENT:'+str(record[3]), size_hint=(0.124,0.09), pos_hint={'center_x':0.228, 'center_y':0.89})
            self.option = Label(text='OPTION:'+str(record[4]), size_hint=(0.124,0.09), pos_hint={'center_x':0.228, 'center_y':0.86})
            self.school = Label(text="SCHOOL:"+ str(record[5]), size_hint=(0.124,0.09), pos_hint={'center_x':0.228, 'center_y':0.83})

            self.add_widget(self.Name)
            self.add_widget(self.Faculty)
            self.add_widget(self.department)
            self.add_widget(self.option)
            self.add_widget(self.reg)
            self.add_widget(self.school)
        
            print_record += str(record[0]) + str(record[1]) + str(record[2]) + str(record[3]) + str(record[4]) + str(record[5])
        
        c.execute("SELECT * FROM subject1 ORDER BY oid DESC LIMIT 7")

        subjects = c.fetchall()
        print_subjects = []

        # Creating a loop
        L_incr = 0.79
        unit_list = []
        mark = []
        two_list = []
        

        for subs in subjects:
            
            self.su= Label(text='Your score:'+' '+str(subs[0]) +' '+'is'+' '+str(subs[1]), size_hint=(0.124,0.09), pos_hint={'center_x':0.128, 'center_y':L_incr})
            L_incr -=0.03
            self.add_widget(self.su)

            unit = int(subs[2])
            unit_list.append(unit)

            if subs[1] =='A':
                grade = 5
            elif subs[1] =='B':
                grade = 4
            elif subs[1] =='C':
                grade = 3
            elif subs[1] =='D':
                grade = 2
            elif subs[1] =='E':
                grade = 1
            else:
                grade = 0
            mark.append(grade)

            print_subjects += str(subs[0]) + str(subs[1]) + str([3])


        # Creating a while loop

        length = len(unit_list)
        if len(unit_list) == len(mark):
            for i in range(len(unit_list)):
                two_list.append(unit_list[i] * mark[i])
        else:
            pass




        total_unit = sum(unit_list)
        total_mark = sum(two_list)

        # This condition is necessary to by pass local variable not define
        if total_unit == 0:
            total_unit = 1
            gp = total_mark/total_unit
        else:
            gp= int()

        gp = total_mark/total_unit
        

        GP = Label(text='Your GP is:'+''+str(gp) ,size_hint=(0.124,0.09), pos_hint={'center_x':0.128, 'center_y':L_incr-0.03})
        self.add_widget(GP)


        #deleting record
        c.execute("DELETE from subject1 ")
        c.execute("DELETE from result")
        c.execute("DELETE from subject1 WHERE SUBJECT=''")
        conn.commit()
        conn.close()


        
        self.btn1 = Button(text='HOME', size_hint=(0.2,0.05), pos_hint={'center_x':0.5, 'center_y':0.07})
        self.add_widget(self.btn1)
        self.btn1.bind(on_press=self.previous)

    def previous(self, screen):
        Myapp.screen_manager.transition = SlideTransition(direction="right")
        Myapp.screen_manager.current = "info"


class GradescoreApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        firstpage = info()
        screen = Screen(name="info")
        screen.add_widget(firstpage)
        self.screen_manager.add_widget(screen)

        secondpage = score()
        screen2 = Screen(name="score")
        screen2.add_widget(secondpage)
        self.screen_manager.add_widget(screen2)

        thirdpage = result()
        screen3 = Screen(name="result")
        screen3.add_widget(thirdpage)
        self.screen_manager.add_widget(screen3)

        return self.screen_manager
        
        
        

if __name__ == '__main__':
    Myapp = GradescoreApp()
    Myapp.run()