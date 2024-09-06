from interface import design,elementsGainAndLose
from calcs import men, women
from tkinter import *
from tkinter import messagebox
window = design.Program(False,760,500,"Contador de Calorias")

class Main_Menu():
    def __init__(self):
        #VENTANA
        self.window = window
        #VARIABLES
        self.gender = StringVar()
        self.gender.set(None)
        self.exercise = IntVar()
        self.exercise.set(None)
        self.activitylevel = StringVar()
        self.activitylevel.set(None)
        self.result = StringVar()
        self.daysExercise = StringVar()
        self.daysExercise.set("1")
        self.age = IntVar()
        self.weight = DoubleVar()
        self.height = DoubleVar()
        self.calories = StringVar()
        self.weightToCalc = self.weight.get()
        #MENU
        self.main_menu = Menu(self.window.window)

        #FRAMES
        self.gender_frame = Frame(self.window.window)
        self.data_frame = Frame(self.window.window)
        self.exercise_frame = Frame(self.window.window)
        self.activitylevel_frame = Frame(self.window.window)
        self.results_frame = Frame(self.window.window)
        #LABELS
        self.label_title = Label(self.window.window,text="CONTADOR DE CALORIAS")
        self.gender_label = Label(self.gender_frame,text="ESCOJE SEXO: ")
        self.data_label = Label(self.data_frame,text="INGRESA TUS DATOS:")
        self.weight_label = Label(self.data_frame,text="Peso (Kg): ")
        self.height_label = Label(self.data_frame,text="Altura (cm): ")
        self.age_label = Label(self.data_frame,text="Edad: ")
        self.exercise_label = Label(self.exercise_frame,text="¿REALIZA EJERCICIO FÍSICO?")
        self.exerciseInfo_label = Label(self.exercise_frame, text='¿CUANTOS DÍAS A LA SEMANA?')
        self.activitylevel_label = Label(self.activitylevel_frame,text="ESCOJA NIVEL DE ACTIVIDAD EN EL DÍA")
        self.result1_label = Label(self.results_frame,text="SU CUERPO GASTA: ")
        self.result2_label = Label(self.results_frame)
        self.result3_label = Label(self.results_frame,text=" KILO CALORIAS EN UN DIA")
        #Check Buttons
        self.male_button = Radiobutton(
            self.gender_frame,
            text="HOMBRE",
            value="male",
            variable=self.gender,
            )
        self.female_button = Radiobutton(
            self.gender_frame,
            text="MUJER",
            value="female",
            variable=self.gender,
            )
        self.yes_button = Radiobutton(
            self.exercise_frame,
            text="SI",
            value=1,
            variable=self.exercise,
            command=self.getDataExercise)
        self.no_button = Radiobutton(
            self.exercise_frame,
            text="NO",
            value=0,
            variable=self.exercise,
            command=self.getDataExercise)
        self.sedentary_button = Radiobutton(
            self.activitylevel_frame,
            text="SEDENTARIO",
            value="sedentary",
            variable=self.activitylevel,
            #command=self.getActivity
        )
        self.lightActive_button = Radiobutton(
            self.activitylevel_frame,
            text="POCO ACTIVO",
            value="lightactive",
            variable=self.activitylevel,
            #command=self.getActivity
        )
        self.Active_button = Radiobutton(
            self.activitylevel_frame,
            text="ACTIVO",
            value="active",
            variable=self.activitylevel,
            #command=self.getActivity
        )
        self.hardActive_button = Radiobutton(
            self.activitylevel_frame,
            text="MUY ACTIVO",
            value="hardactive",
            variable=self.activitylevel,
            #command=self.getActivity
        )
        #ENTRYS
        self.weight_entry = Entry(self.data_frame,textvariable=self.weight)
        self.height_entry = Entry(self.data_frame,textvariable=self.height)
        self.age_entry = Entry(self.data_frame,textvariable=self.age)
        #BUTTONS
        self.calculate_button = Button(self.activitylevel_frame,text="CALCULAR",command=self.calculate)
        self.clean_button = Button(self.activitylevel_frame,text="LIMPIAR",command=self.clean)
        #OPTION MENU
        self.days_OpMenu = OptionMenu(self.exercise_frame,self.daysExercise,
                               "1",
                               "2",
                               "3",
                               "4",
                               "5",
                               "6",
                               "7",)
        #GAIN MUSCLE OR LOST WEIGHT ELEMENTS
        self.GainOrLose_elements = elementsGainAndLose.Gain_Muscle_Lost_Weight(self.window)
        self.experience_frame = self.GainOrLose_elements.experience_frame
        self.calories_frame = self.GainOrLose_elements.Calories_frame
        self.caloriesToEat_frame = self.GainOrLose_elements.CaloriesToEat_frame
        self.Macros_frame = self.GainOrLose_elements.MacroNutrients_frame
        
    #Functions
    

    def getDataExercise(self):
        if int(self.exercise.get()) ==1:
            self.days_OpMenu.place(x=110,y=100)
            self.exerciseInfo_label.place(x=60,y=70)
        else:
            self.days_OpMenu.place_forget()
            self.exerciseInfo_label.place_forget()

   
    def calculate(self):
        try:
            if self.gender.get() =="male":
                self.user = men.Men(self.weight.get(),self.height.get(),self.age.get(),self.activitylevel.get(),self.daysExercise.get())
                if self.age.get() <= 0 or self.age.get() >= 90:
                    messagebox.showerror("EDAD ERRONEA","INGRESE UNA EDAD VALIDA")
                else:
                    if self.weight.get() <= 0 or self.weight.get() > 650:
                        messagebox.showerror("PESO ERRONEO","INGRESE UN PESO VALIDO")
                    else:
                        if self.height.get() <= 80 or self.height.get() > 255:
                            
                            messagebox.showerror("ALTURA ERRONEO","INGRESE UNA ALTURA VALIDA")
                        else:
                            self.user.Exercise(self.exercise.get())
                            self.user.Calc()
                            self.calories.set(round(self.user.Total_Calories,2))
                            self.result2_label.config(
                                textvariable=self.calories
                            )
                            
                
            elif self.gender.get() == "female":
                if self.age.get() <= 0 or self.age.get() >= 90:
                    messagebox.showerror("EDAD ERRONEA","INGRESE UNA EDAD VALIDA")
                else:
                    if self.weight.get() <= 0 or self.weight.get() > 650:
                        messagebox.showerror("PESO ERRONEO","INGRESE UN PESO VALIDO")
                    else:
                        if self.height.get() <= 80 or self.height.get() > 255:
                            
                            messagebox.showerror("ALTURA ERRONEO","INGRESE UNA ALTURA VALIDA")
                        else:
                            self.user.Exercise(self.exercise.get())
                            self.user.Calc()
                            self.calories.set(round(self.user.Total_Calories,2))
                            self.result2_label.config(
                                textvariable=self.calories
                            )  
            else:
                messagebox.showinfo("SELECCIONE SEXO","DEBE SELECCIONAR UN SEXO PARA QUE EL PROGRAMA PUEDA CALCULAR SUS CALORIAS")
        except:
            messagebox.showerror("DATOS VACIOS","VERIFIQUE QUE HAYA LLENADO TODOS LOS DATOS Y QUE ESTOS ESTEN CORRECTOS PUDO HABER TIPEADO UNA LETRA O SIMBOLO POR ACCIDENTE EN SUS DATOS PERSONALES U OLVIDO SELECCIONAR ALGUNA CASILLA")
          
    #MENUS
    def AddMenu(self):
        self.window.window.config(
        menu=self.main_menu
        )
        self.main_menu.add_command(label="Gasto Calorico",command=self.home)
        self.main_menu.add_command(label="Ganar Masa Muscular",command=self.gain_muscle)
        self.main_menu.add_command(label="Perder Grasa",command=self.lost_weight)
        self.main_menu.add_command(label="Salir",command=window.window.destroy)
    #SETTINGS
    def config_elements_HOME(self):
        #LABELS
        self.label_title.config(
            bg="#32612D",
            padx=220,
            pady=15,
            font=("Open Sans Condensed SemiBold",20),
            fg='White',
            text="CONTADOR DE CALORIAS"
            
        )
        self.gender_label.config(
            font = ("Open Sans Condensed SemiBold",15),
            padx=25
        )
        self.data_label.config(
           font = ("Open Sans Condensed SemiBold",15),
           padx=15 
        )
        self.exercise_label.config(
           font = ("Open Sans Condensed SemiBold",13),
           padx=5
        )
        self.weight_label.config(
            font = ("Open Sans Condensed",11),  
        )
        self.height_label.config(
            font = ("Open Sans Condensed",11), 
        )
        self.age_label.config(
            font = ("Open Sans Condensed",11), 
        )
        self.activitylevel_label.config(
            font = ("Open Sans Condensed SemiBold",13),
            padx=8
        )
        self.result1_label.config(
            font = ("Open Sans Condensed SemiBold",13),
            padx=7
        )
        self.result2_label.config(
            font = ("Open Sans Condensed SemiBold",16),
            padx=8
        )
        self.result3_label.config(
            font = ("Open Sans Condensed SemiBold",11),
        )
        #FRAMES
        self.gender_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=200,
            height=200,
            
        )
        self.data_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=265,
            height=200,
        )
        self.exercise_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=250,
            height=200,
        )
        self.activitylevel_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=350,
            height=200,
        )
        self.results_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=380,
            height=200,
        )
        #RADIO BUTTON
        self.male_button.config(
            font = ("Open Sans Condensed",17),
            padx=25
        )
        self.female_button.config(
            font = ("Open Sans Condensed",17),
            padx=25
        )
        self.sedentary_button.config(
            font = ("Open Sans Condensed",12),
            padx=25,
        )
        self.lightActive_button.config(
            font = ("Open Sans Condensed",14),
            padx=25,
        )
        self.Active_button.config(
            font = ("Open Sans Condensed",14),
            padx=25,
        )
        self.hardActive_button.config(
            font = ("Open Sans Condensed",14),
            padx=25,
        )
        self.yes_button.config(
            font = ("Open Sans Condensed",17), 
        )
        self.no_button.config(
            font = ("Open Sans Condensed",17),  
        )

       #ENTRYS
        self.weight_entry.config(
           font = ("Open Sans Condensed",9), 
        )
        self.age_entry.config(
           font = ("Open Sans Condensed",9), 
        )
        self.height_entry.config(
           font = ("Open Sans Condensed",9), 
        )

        #BUTTONS
        self.calculate_button.config(
            font = ("Open Sans Condensed SemiBold",15),
            padx=20,
            bg="#32612D",
            fg='white',
            #state='disabled'
        )
        self.clean_button.config(
            font = ("Open Sans Condensed SemiBold",15),
            padx=30,
            bg="#32612D",
            fg='white',
            
        )

    

    def place_elements_HOME(self):
        #GENDER AND TITLE
        self.label_title.place(x=0,y=0)
        self.gender_frame.place(x=10,y=80)
        self.gender_frame.pack_propagate(FALSE)
        self.gender_label.place(x=9,y=0)
        self.male_button.place(x=18,y=50)
        self.female_button.place(x=18,y=100)

        #PERSONAL DATA
        self.data_label.place(x=0,y=0)
        self.data_frame.place(x=230,y=80)
        self.data_frame.pack_propagate(FALSE)
        self.weight_label.place(x=10,y=50)
        self.height_label.place(x=10,y=100)
        self.age_label.place(x=10,y=150)
        self.weight_entry.place(x=97,y=50)
        self.height_entry.place(x=97,y=100)
        self.age_entry.place(x=97,y=150)
        #EXERCISE INFO
        self.exercise_label.place(x=0,y=0)
        self.exercise_frame.place(x=500,y=80)
        self.exercise_frame.pack_propagate(FALSE)
        self.yes_button.place(x=2,y=50)
        self.no_button.place(x=2,y=100)
        
        #ACTIVITY LEVEL INFO
        self.activitylevel_label.place(x=0,y=0)
        self.activitylevel_frame.place(x=10,y=290)
        self.activitylevel_frame.pack_propagate(FALSE)
        self.results_frame.place(x=370,y=290)
        self.activitylevel_frame.pack_propagate(FALSE)
        self.sedentary_button.place(x=0,y=40)
        self.lightActive_button.place(x=150,y=40)
        self.Active_button.place(x=0,y=80)
        self.hardActive_button.place(x=150,y=80)
        self.calculate_button.place(x=10,y=130)
        self.clean_button.place(x=175,y=130)
        
        #RESULTS
        self.result1_label.place(x=95,y=0)
        self.result2_label.place(x=140,y=60)
        self.result3_label.place(x=85,y=125)
    def gain_muscle(self):
        self.GainOrLose_elements.experience.set(None)
        self.GainOrLose_elements.clean()
        self.label_title.config(
            text="CALORIAS PARA GANAR MASA MUSCULAR",
            padx=100
        )
        self.GainOrLose_elements.label_caloriesToEat3.config(
            text="PARA GANAR MASA MUSCULAR SANAMENTE",
            padx=0
        )
        self.eraseFrames()
        self.GainOrLose_elements.objective = 0
        self.GainOrLose_elements.config_elements_GainMuscle_Lost_Weight()
        self.GainOrLose_elements.place_elements_GainMuscle_LostWeight()
        self.GainOrLose_elements.label_infoAboutExperince.place_forget()
        

    def lost_weight(self):
        self.GainOrLose_elements.clean()
        self.label_title.config(
            text="CALORIAS PARA PERDER GRASA ",
            padx=155
        )
        self.eraseFrames()
        self.GainOrLose_elements.objective = 1
        self.GainOrLose_elements.config_elements_GainMuscle_Lost_Weight()
        self.GainOrLose_elements.label_caloriesToEat3.config(
            text="PARA PERDER GRASA SANAMENTE",
            padx=40
        )
        self.GainOrLose_elements.place_elements_GainMuscle_LostWeight()
        self.experience_frame.place_forget()
        self.GainOrLose_elements.Calories_frame.config(
            bd=.5,
            relief=SUNKEN,
            width=741,
            height=200,
        )
        self.GainOrLose_elements.Calories_frame.place(
            x = 10,
        )
        self.GainOrLose_elements.label_calories.place(x=265,y=0)
        self.GainOrLose_elements.label_calories_info.place(x=225,y=70)
        self.GainOrLose_elements.label_weight.place(x=245,y=100)
        self.GainOrLose_elements.weight_entry.place(x=330,y=100)
        self.GainOrLose_elements.label_calories_info2.place(x=230,y=40)
        self.GainOrLose_elements.Calories_entry.place(x=330,y=40)
        self.GainOrLose_elements.calculate_button.place(x=200,y=140)
        self.GainOrLose_elements.clean_button.place(x=370,y=140)
        
    def home(self):
        self.eraseFramesGainOrLose()
        self.config_elements_HOME()
        self.place_elements_HOME()
    def run(self): 
        self.AddMenu()
        self.home()
        self.window.run_window()
    def eraseFrames(self):
        self.gender_frame.place_forget()
        self.data_frame.place_forget()
        self.exercise_frame.place_forget()
        self.activitylevel_frame.place_forget()
        self.results_frame.place_forget()
    def eraseFramesGainOrLose(self):
        self.calories_frame.place_forget()
        self.experience_frame.place_forget()
        self.Macros_frame.place_forget()
        self.caloriesToEat_frame.place_forget()
    def clean(self):
        self.gender.set(None)
        self.activitylevel.set(None)
        self.exercise.set(None)
        self.weight.set("")
        self.height.set("")
        self.age.set("")
        self.calories.set("")
        self.label_title.focus()
        self.exerciseInfo_label.place_forget()
        self.days_OpMenu.place_forget()


        

    






