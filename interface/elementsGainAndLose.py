from tkinter import *
from calcs import objectives
from tkinter import messagebox
class Gain_Muscle_Lost_Weight():
    def __init__(self,window,objective=0):
        self.window = window
        self.experience = StringVar()
        self.experience.set(None)
        self.weight = DoubleVar()
        self.calories = DoubleVar()
        self.objective = objective
        self.proteinGrames = StringVar()
        self.fatsGrames = StringVar()
        self.carbosGrames = StringVar()
        self.calories_to_eat = StringVar()
        #FRAMES
        self.experience_frame = Frame(self.window.window)
        self.Calories_frame = Frame(self.window.window)
        self.CaloriesToEat_frame = Frame(self.window.window)
        self.MacroNutrients_frame = Frame(self.window.window)
        #LABELS
        self.label_title = Label(self.window.window,text="CALORIAS PARA GANAR MASA MUSCULAR")
        self.label_experience = Label(self.experience_frame, text="NIVEL ASPECTO FISICO")
        self.label_calories = Label(self.Calories_frame, text="INGRESA TUS DATOS")
        self.label_calories_info = Label(self.Calories_frame,text='Puedes calcularlo en el Menu "Gasto Calorico"')
        self.label_caloriesToEat1 = Label(self.CaloriesToEat_frame,text="DEBES CONSUMIR:")
        self.label_caloriesToEat2 = Label(self.CaloriesToEat_frame,textvariable=self.calories_to_eat)
        self.label_caloriesToEat3 = Label(self.CaloriesToEat_frame,text="PARA GANAR MASA")
        self.label_macros_info = Label(self.MacroNutrients_frame,text="MACRONUTRIENTES A CONSUMIR")
        self.label_proteingrames = Label(self.MacroNutrients_frame,textvariable=self.proteinGrames)
        self.label_proteininfo = Label(self.MacroNutrients_frame,text="GRAMOS DE PROTEINA")
        self.label_carbogrames = Label(self.MacroNutrients_frame,textvariable=self.carbosGrames)
        self.label_carboinfo = Label(self.MacroNutrients_frame,text="GRAMOS DE CARBOHIDRATOS")
        self.label_fatsgrames = Label(self.MacroNutrients_frame,textvariable=self.fatsGrames)
        self.label_fatsinfo = Label(self.MacroNutrients_frame,text="GRAMOS DE GRASAS")
        self.label_weight = Label(self.Calories_frame,text="Peso (Kg):")
        self.label_calories_info2 = Label(self.Calories_frame,text="Gasto Calorico: ")
        self.label_infoAboutExperince = Label(self.experience_frame,text="PARA PERDER GRASA TU NIVEL NO AFECTA AL RESULTADO")
        #Radio Buttons

        self.begginer_Button = Radiobutton(self.experience_frame,
                                           text="Principiante",
                                           value="Begginer",
                                           variable=self.experience
                                           )
        self.intermediate_Button = Radiobutton(self.experience_frame,
                                           text="Intermedio",
                                           value="Medium",
                                           variable=self.experience
                                           )
        self.advance_Button = Radiobutton(self.experience_frame,
                                          text="Avanzado",
                                          value="Advanced",
                                          variable=self.experience)
        
        #ENTRYS

        self.Calories_entry = Entry(self.Calories_frame,textvariable=self.calories)
        self.weight_entry = Entry(self.Calories_frame,textvariable=self.weight)

        #BUTTONS

        self.calculate_button = Button(self.Calories_frame,command= lambda: self.calculate(self.objective))
        self.clean_button = Button(self.Calories_frame,command=self.clean)
        
        
        
        
        
    def config_elements_GainMuscle_Lost_Weight(self):
        #FRAMES
        self.experience_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=370,
            height=200,
           
        )
        self.Calories_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=370,
            height=200,  
        )
        self.CaloriesToEat_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=370,
            height=200,
        )
        self.MacroNutrients_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=370,
            height=200,
        )
        #LABEL
        self.label_experience.config(
            font = ("Open Sans Condensed SemiBold",14),
            padx=5
        )
        self.label_calories.config(
           font = ("Open Sans Condensed SemiBold",11),
           padx=15 
        )
        self.label_calories_info.config(
            font = ("Open Sans Condensed SemiBold",10),
            padx=8
        )

       
        self.label_weight.config(
            font = ("Open Sans Condensed",10),
        )
        self.label_calories_info2.config(
            font = ("Open Sans Condensed",10),
           
        )
        self.label_caloriesToEat1.config(
            font = ("Open Sans Condensed SemiBold",13),
            padx=8
        )
        self.label_caloriesToEat2.config(
            font = ("Open Sans Condensed SemiBold",14),
          
        )
        self.label_caloriesToEat3.config(
            font = ("Open Sans Condensed SemiBold",11),
        )
        # if self.objective == 1:
        #     self.label_caloriesToEat3.config(
        #         text="CALORIAS PARA (PROCANDO) PERDER GRASA SANAMENTE"
        #     )
        self.label_macros_info.config(
            font = ("Open Sans Condensed SemiBold",15),
            padx=8
        )
        self.label_proteingrames.config(
            font = ("Open Sans Condensed",15),
            padx=8
        )
        self.label_proteininfo.config(
            font = ("Open Sans Condensed",12),
            padx=8
        )
        self.label_carbogrames.config(
            font = ("Open Sans Condensed",15),
            padx=8
        )
        self.label_carboinfo.config(
            font = ("Open Sans Condensed",12),
            padx=8
        )
        self.label_fatsgrames.config(
            font = ("Open Sans Condensed",15),
            padx=8
        )
        self.label_fatsinfo.config(
            font = ("Open Sans Condensed",12),
            padx=8
        )

        #ENTRYS
        self.weight_entry.config(
            font = ("Open Sans Condensed",12),
        )
        self.Calories_entry.config(
            font = ("Open Sans Condensed",12),
        )
    

        #BUTTONS
        self.calculate_button.config(
            font = ("Open Sans Condensed SemiBold",12),
            padx=25,
            bg="#32612D",
            fg='white',
            text="CALCULAR"
        )
        self.clean_button.config(
            font = ("Open Sans Condensed SemiBold",12),
            padx=35,
            bg="#32612D",
            fg='white',
            text="LIMPIAR" 
        )

        #RADIO BUTTONS
        self.begginer_Button.config(
            font = ("Open Sans Condensed",15),
            padx=105,
        )
        self.intermediate_Button.config(
            font = ("Open Sans Condensed",15),
            padx=105,
        )
        self.advance_Button.config(
            font = ("Open Sans Condensed",15),
            padx=105,
        )
        self.label_infoAboutExperince.config(
            font = ("Open Sans Condensed",11),
        )
       
    def place_elements_GainMuscle_LostWeight(self):
       
        #EXPERIENCE LEVEL
        self.experience_frame.place(x=8,y=80)
        self.label_experience.place(x=73,y=0)
        self.begginer_Button.place(x=0,y=33)
        self.intermediate_Button.place(x=0,y=74)
        self.advance_Button.place(x=0,y=112)
        self.label_infoAboutExperince.place(x=35,y=165)

        #CALORIES AND WEIGHT
        self.Calories_frame.place(x=383,y=80)
        self.label_calories.place(x=85,y=0)
        self.label_calories_info.place(x=45,y=70)
        self.label_weight.place(x=65,y=100)
        self.weight_entry.place(x=150,y=100)
        self.label_calories_info2.place(x=50,y=40)
        self.Calories_entry.place(x=150,y=40)
        self.calculate_button.place(x=20,y=140)
        self.clean_button.place(x=190,y=140)
        
        #CALORIES TO EAT 
        self.CaloriesToEat_frame.place(x=8,y=290)
        self.label_caloriesToEat1.place(x=85,y=10)
        self.label_caloriesToEat2.place(x=90,y=70)
        self.label_caloriesToEat3.place(x=20,y=130)

        #MACROS INFO
        self.MacroNutrients_frame.place(x=383,y=290)
        self.label_macros_info.place(x=10,y=10)
        self.label_proteingrames.place(x=40,y=60)
        self.label_proteininfo.place(x=110,y=60)
        self.label_carbogrames.place(x=40,y=105)
        self.label_carboinfo.place(x=110,y=105)
        self.label_fatsgrames.place(x=40,y=150)
        self.label_fatsinfo.place(x=110,y=150)
        
        
        
        
    def calculate(self,objective):
        if objective == 0:
            try:
                if self.calories.get() <= 0 or self.calories.get() > 5550:
                    messagebox.showerror("CALORIAS INVALIDAS" , "INGRESE UN GASTO CALORICO VALIDO")
                else:
                    if self.weight.get() <= 0 or self.weight.get() > 650:
                        messagebox.showerror("PESO INVALIDO" , "INGRESE UN PESO VALIDO")
                    else:
                        self.user = objectives.Objective(self.weight.get(),self.experience.get(),self.calories.get())
                        self.user.Gain_Muscle()
                        self.calories_to_eat.set(str(round(self.user.superavit,2)) + " CALORIAS")
                        self.proteinGrames.set(round(self.user.proteinGrames,2))
                        self.carbosGrames.set(round(self.user.carbos_grames,2))
                        self.fatsGrames.set(round(self.user.fatsGrames,2))
            except:
                messagebox.showerror("DATOS VACIOS O INCORRECTOS","VERIFICA QUE HAYAS SELECCIONADO UN NIVEL EN TUS ENTRENAMIENTOS, Y QUE LA INFORMACIÓN INGRESADA SEA CORRECTA, PUEDES HABER TIPEADO UNA LETRA O SIMBOLO EN TU PESO O GASTO CALÓRICO.")
        else:
            try:
                if self.calories.get() < 0 or self.calories.get() > 5550:
                    messagebox.showerror("CALORIAS INVALIDAS" , "INGRESE UN GASTO CALORICO VALIDO")
                else:
                    if self.weight.get() < 0 or self.weight.get() > 650:
                        messagebox.showerror("PESO INVALIDO" , "INGRESE UN PESO VALIDO")
                    else:
                        self.user = objectives.Objective(self.weight.get(),self.experience.get(),self.calories.get())
                        self.user.Lost_Weight()
                        self.calories_to_eat.set(str(round(self.user.deficit,2)) + " CALORIAS")
                        self.proteinGrames.set(round(self.user.proteinGrames,2))
                        self.carbosGrames.set(round(self.user.carbos_grames,2))
                        self.fatsGrames.set(round(self.user.fatsGrames,2))
            except:
                messagebox.showerror("DATOS VACIOS U INCORRECTOS","VERIFICA QUE TU PESO Y TU GASTO CALÓRICO SEA CORRECTO, PUEDES HABER TIPEADO UNA LETRA O SÍMBOLO")
       
    def clean(self):
        self.experience.set(None)
        self.weight.set("")
        self.calories.set("")
        self.proteinGrames.set("")
        self.fatsGrames.set("")
        self.carbosGrames.set("")
        self.calories_to_eat.set("")
        self.label_calories.focus()