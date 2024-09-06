from tkinter import *
from tkinter import messagebox
class Objective():
    def __init__(self,weight,experience,calories=0):
        self.calories = calories
        self.weight = weight
        self.experience = experience
    def Gain_Muscle(self):
        if self.experience == 'Begginer':
            self.weightResults = (self.weight*1.2) /100
            self.calories_to_eat = (self.weightResults*3500)/0.5
            self.calories_to_eat_daily = self.calories_to_eat /30
            self.superavit = self.calories + self.calories_to_eat_daily
            self.proteinGrames = 1.8 * self.weight
            self.calories_protein = self.proteinGrames * 4
            self.fatsGrames = 1.3 * self.weight
            self.calories_fats = self.fatsGrames * 9
            self.calories_carbos = self.superavit - (self.calories_protein + self.calories_fats)
            self.carbos_grames = self.calories_carbos / 4
        elif self.experience == 'Medium':
            self.weightResults = (self.weight*0.8) /100
            self.calories_to_eat = (self.weightResults*3500)/0.5
            self.calories_to_eat_daily = self.calories_to_eat /30
            self.superavit = self.calories + self.calories_to_eat_daily
            self.proteinGrames = 1.8 * self.weight
            self.calories_protein = self.proteinGrames * 4
            self.fatsGrames = 1.3 * self.weight
            self.calories_fats = self.fatsGrames * 9
            self.calories_carbos = self.superavit - (self.calories_protein + self.calories_fats)
            self.carbos_grames = self.calories_carbos / 4
        elif self.experience == "Advanced":
            self.weightResults = (self.weight*0.3) /100
            self.calories_to_eat = (self.weightResults*3500)/0.5
            self.calories_to_eat_daily = self.calories_to_eat /30
            self.superavit = self.calories + self.calories_to_eat_daily
            self.proteinGrames = 1.8 * self.weight
            self.calories_protein = self.proteinGrames * 4
            self.fatsGrames = 1.3 * self.weight
            self.calories_fats = self.fatsGrames * 9
            self.calories_carbos = self.superavit - (self.calories_protein + self.calories_fats)
            self.carbos_grames = self.calories_carbos / 4
        
    def Lost_Weight(self):
            
            self.weightResults = (self.weight*0.7) /100
            self.calories_to_eat = (self.weightResults*3500)/0.5
            self.calories_to_eat_daily = self.calories_to_eat /30
            self.deficit = self.calories - self.calories_to_eat_daily
            self.proteinGrames = 2.2 * self.weight
            self.calories_protein = self.proteinGrames * 4
            self.fatsGrames = 1* self.weight
            self.calories_fats = self.fatsGrames * 9
            self.calories_carbos = self.deficit - (self.calories_protein + self.calories_fats)
            self.carbos_grames = self.calories_carbos / 4