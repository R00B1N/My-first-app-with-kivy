#!/usr/bin/python3

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import  GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class BlackGrid(GridLayout):
    def __init__(self, **kwargs):
        super(BlackGrid, self).__init__()
        self.add_widget(Label(text= "Nombre del estudiante: "))
        self.cols = 2
        self.s_name = TextInput(multiline=False)
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Nota del estudiante: "))
        self.s_score = TextInput(multiline=False)
        self.add_widget(self.s_score)

        self.add_widget(Label(text= "Genero del estudiante: "))
        self.s_gender = TextInput(multiline=False)
        self.add_widget(self.s_gender)


        self.press = Button(text= "Guardar")
        self.press.bind(on_press = self.click_me)
        self.add_widget(self.press)

    def click_me(self,instance):
        print("Tu has introducido valores nuevos\nTus valores son: \n")
        print("El nombre del estudiante es " + self.s_name.text)
        print("La nota del estudiante es " + self.s_score.text)
        print("El genero del estudiante es " + self.s_gender.text)



class BlackApp(App):
    def build(self):
        return BlackGrid()

if __name__=="__main__":
    BlackApp().run()