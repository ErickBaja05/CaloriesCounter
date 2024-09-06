from tkinter import *
class Women():
    def __init__(self,weight,height,age,activity,days=0):   
        self.weight = weight
        self.height =height
        self.age = age
        self.Metabolism = 655.1+(9.5663*self.weight)+(1.85*self.height)-(4.676*self.age)
        self.days = float(days)
        self.activity_level = activity
        self.Total_Calories = StringVar()

    def Exercise(self,excercise=0):
        if excercise == 0:
            self.exercise = False
        else:
            self.exercise = True

    def Calc(self):
        if self.exercise:
            if self.activity_level == "sedentary":
                if self.days == 1:
                    self.Total_Calories = self.Metabolism * 1.1
                elif self.days ==2:
                    self.Total_Calories = self.Metabolism * 1.2
                elif self.days ==3:
                    self.Total_Calories = self.Metabolism * 1.3
                elif self.days ==4:
                    self.Total_Calories = self.Metabolism * 1.4
                elif self.days ==5:
                    self.Total_Calories = self.Metabolism * 1.5
                elif self.days ==6:
                    self.Total_Calories = self.Metabolism * 1.6
                else:
                    self.Total_Calories = self.Metabolism * 1.7
            elif self.activity_level == "lightactive":
                if self.days == 1:
                    self.Total_Calories = self.Metabolism * 1.3
                elif self.days ==2:
                    self.Total_Calories = self.Metabolism * 1.4
                elif self.days ==3:
                    self.Total_Calories = self.Metabolism * 1.5
                elif self.days ==4:
                    self.Total_Calories = self.Metabolism * 1.6
                elif self.days ==5:
                    self.Total_Calories = self.Metabolism * 1.7
                elif self.days ==6:
                    self.Total_Calories = self.Metabolism * 1.8
                else:
                    self.Total_Calories = self.Metabolism * 1.9
            elif self.activity_level == "active":
                if self.days == 1:
                    self.Total_Calories = self.Metabolism * 1.5
                elif self.days ==2:
                    self.Total_Calories = self.Metabolism * 1.6
                elif self.days ==3:
                    self.Total_Calories = self.Metabolism * 1.7
                elif self.days ==4:
                    self.Total_Calories = self.Metabolism * 1.8
                elif self.days ==5:
                    self.Total_Calories = self.Metabolism * 1.9
                elif self.days ==6:
                    self.Total_Calories = self.Metabolism * 2.0
                else:
                    self.Total_Calories = self.Metabolism * 2.1
            else:
                if self.days == 1:
                    self.Total_Calories = self.Metabolism * 1.7
                elif self.days ==2:
                    self.Total_Calories = self.Metabolism * 1.8
                elif self.days ==3:
                    self.Total_Calories = self.Metabolism * 1.9
                elif self.days ==4:
                    self.Total_Calories = self.Metabolism * 2.0
                elif self.days ==5:
                    self.Total_Calories = self.Metabolism * 2.1
                elif self.days ==6:
                    self.Total_Calories = self.Metabolism * 2.2
                else:
                    self.Total_Calories = self.Metabolism * 2.2
        else:
            if self.activity_level == "sedentary":
                self.Total_Calories = self.Metabolism * 1.1
            elif self.activity_level == 'lightactive':
                self.Total_Calories = self.Metabolism * 1.2
            elif self.activity_level == 'active':
                self.Total_Calories = self.Metabolism * 1.4
            else:
                self.Total_Calories = self.Metabolism * 1.6
    


    