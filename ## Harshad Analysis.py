## Harshad Analysis
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np

matplotlib.use("TkAgg")  # Ensures compatibility with PySimpleGUI
class Harshad:
    def __init__(self):
        pass
    def Executable(self):
        self.window = self.create_main_window()
        while True:
            event, values = self.window.read()
            if event == "SUBMIT": 
                if self.Input_Validation(values["USER_INPUT"]): continue
                self.Harshad_Test_Function(int(values["USER_INPUT"]))
            if event == "PLOT":
                if self.Input_Validation(values["MIN"], values["MAX"]): continue
                self.Plot(values["MIN"], values["MAX"])
            elif event == (sg.WIN_CLOSED): break
        self.window.close()
    def create_main_window(self):
        HarshadEvaluation = sg.Frame('IsHarshad', [
            [sg.Text("Please enter an integer"), sg.Input("", key = "USER_INPUT")],
                    [sg.Button("Submit", key = "SUBMIT")],
                    [sg.Button("", key = "LED", button_color = 'white'), sg.Text("        ", key = "SUPER_HARSHAD_MESSAGE")],
                    [sg.Text("Please enter a range you would like to evaluate:"), sg.Input("", key = "MIN"), sg.Input("", key = "MAX")],
                    [sg.Text("Note: 10 - 99 for two digit. 100 - 999 for three digit.")],
                    [sg.Text("Please enter a name for your plot if desired"), sg.Input("", key = "TITLE")],
                    [sg.Button("Plot", key = "PLOT")],
                    [sg.Text("", key = "NUMBER_OF_HARSHADS")]
        ],
        size = (800, 500))
        PlottingArea = sg.Frame("Plotting Area", [
                [sg.Text("")],
            ],
        size = (800, 500), key = "PLOT_FRAME")
        layout = [[HarshadEvaluation, PlottingArea]]
        return sg.Window("My Window", layout, resizable = True)
    def Harshad_Test_Function(self, HarshadTest):
        X = HarshadTest
        TestArray = []
        while HarshadTest != 0:
            TestArray.append(HarshadTest % 10) 
            HarshadTest = HarshadTest // 10
        Sum = 0
        for i in TestArray:
            Sum = Sum + i
        N = X / Sum
        if  X % Sum == 0: 
            runningTotal = 0
            for j in range(0, int(N)):
                runningTotal = runningTotal + (10 ** (j*len(TestArray)))*(X)
            self.window["SUPER_HARSHAD_MESSAGE"].update(f"{X} is a Harshad, and its corresponding Super-Harshad is: {runningTotal} ")
            self.window["LED"].update(button_color = 'green')
        else:
            self.window["SUPER_HARSHAD_MESSAGE"].update(f"Sorry, {X} is not a Harshad")
            self.window["LED"].update(button_color = 'red')
    def Plot(self, MIN, MAX):
        super_Harshad_Array = []
        Harshad_Array = []
        super_Harshad_Array_Log = []

        for Test in range(int(MIN), int(MAX)):
            X = Test
            TestArray = []
            while Test != 0:
                TestArray.append(Test % 10) 
                Test = Test // 10
            Sum = 0
            for i in TestArray: # get sum of individual digits.
                Sum = Sum + i
            if  X % Sum == 0 and X % 10 != 0: # 18 % 9 == 0 (True: remainder == 0) and 18 % 10 != 0 (True: remainder == 8)
                N = X / Sum # Divisibility Count.
                runningTotal = 0
                for j in range(0, int(N)):
                    runningTotal = runningTotal + (10 ** (j*len(TestArray)))*(X)
                super_Harshad_Array.append(runningTotal)
                super_Harshad_Array_Log.append(np.log10(runningTotal))
                Harshad_Array.append(X)
        fig, ax = plt.subplots() 
        ax.plot(Harshad_Array, super_Harshad_Array_Log, marker='o')
        ax.set_title("Harshad vs. Super_Harshad")
        ax.set_xlabel("Harshad")
        ax.set_ylabel("Super Harshads")
        # Ensure the plot is shown **without blocking PySimpleGUI**
        fig.canvas.manager.show()
        plt.gcf().canvas.manager.set_window_title({self.window["TITLE"]})
        self.window["NUMBER_OF_HARSHADS"].update(f"You have exactly {len(Harshad_Array)} Super-Harshads on this interval")

    def Input_Validation(self, *argv):
        for value in argv:
            if value == '':
                sg.popup("Input cannot be blank!")
                return True
        return False      
if __name__ == "__main__":
    Test = Harshad() # class instantiation
    Test.Executable()