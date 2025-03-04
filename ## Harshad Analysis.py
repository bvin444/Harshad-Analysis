## Harshad Analysis
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib
import math 

matplotlib.use("TkAgg")  # Ensures compatibility with PySimpleGUI
class Harshad:
    def __init__(self):
        pass
    def Executable(self):
        self.window = self.create_main_window()
        while True:
            event, values = self.window.read()
            if event == "SUBMIT_0": 
                if self.Input_Validation(values["USER_INPUT"]): continue
                self.Single_Digit_Evaluation(int(values["USER_INPUT"]))
            elif event == "PLOT":
                if self.Input_Validation(values["MIN"], values["MAX"]): continue
                self.Plot(values["MIN"], values["MAX"])
            elif event == "SUBMIT_1":
                if self.Input_Validation(values["MIN"], values["MAX"]): continue
                self.How_Many_Interval(values["MIN"], values["MAX"])
            elif event == "BASIC_STATS":
                if self.Input_Validation(values["MIN"], values["MAX"]): continue
                self.Basic_Statistics(values["MIN"], values["MAX"])
            elif event == (sg.WIN_CLOSED): break
        self.window.close()
    def create_main_window(self):
        HarshadEvaluation = sg.Frame('IsHarshad', [
                    [sg.Text("Please enter an integer you would like to evaluate"), sg.Input("", key = "USER_INPUT", size = (8, 1)), sg.Button("Submit", key = "SUBMIT_0")],
                    [sg.Button("   ", key = "LED", button_color = 'white'), sg.Text("        ", key = "SUPER_HARSHAD_MESSAGE")],
        ],
        size = (800, 500))
        AnalysisArea = sg.Frame("Analysis", [
                    [sg.Text("Please enter a range you would like to evaluate:"), sg.Input("", key = "MIN"), sg.Input("", key = "MAX")],
                    [sg.Text("Determine the number of Harshads on this interval"), sg.Button("Submit", key = "SUBMIT_1"),sg.Text("Number of Harshads: ", key = "NUMBER_OF_HARSHADS")],
                    [sg.Button("Plot this range", key = "PLOT"), sg.Text("Due to computer performance, plotting is doable up to about 9999.")],
                    [sg.Button("Computer Basic Statistics (Mean, STD)", key = "BASIC_STATS"), sg.Text("", key = "BASIC_STATS_OUTPUT")],
            ],
        size = (800, 500), key = "PLOT_FRAME")
        layout = [[HarshadEvaluation, AnalysisArea]]
        return sg.Window("My Window", layout, resizable = True, keep_on_top = True)
    def Compute(self, MIN, MAX):
        self.super_Harshad_Array = []
        self.Harshad_Array = []
        self.super_Harshad_Array_Log = []
        for Test in range(int(MIN), int(MAX)):
            X = Test
            TestArray = []
            while Test != 0:
                TestArray.append(Test % 10) 
                Test = Test // 10
            Sum = 0
            for i in TestArray: # get sum of individual digits.
                Sum = Sum + i
            if  X % Sum == 0 and X % 10 != 0: 
                N = X / Sum 
                runningTotal = 0
                for j in range(0, int(N)):
                    runningTotal = runningTotal + (10 ** (j*len(TestArray)))*(X)
                self.super_Harshad_Array.append(runningTotal)
                self.super_Harshad_Array_Log.append(math.log10(int(runningTotal))) # np uses fixed-integer precision. math uses arbitrary-integer precision.
                self.Harshad_Array.append(X)
    def Basic_Statistics(self, MIN, MAX):
        self.Compute(MIN, MAX)
        super_Total = 0
        for i in self.super_Harshad_Array_Log:
            super_Total = round(super_Total + i, 2)
        self.Mean = round(float(super_Total / len(self.super_Harshad_Array_Log)), 2)
        std_Sum = 0
        for j in self.super_Harshad_Array_Log:
            std_Sum = std_Sum + ((j - self.Mean) ** 2)
        self.std_Post = round((std_Sum / (len(self.super_Harshad_Array_Log))) ** (1/2), 2)
        self.window["BASIC_STATS_OUTPUT"].update(f"Your Mean is {self.Mean} and your Standard-Deviation is {self.std_Post}")
    # Single Digit Test
    def Compute_Z_Score(self):
        self.Z_Score = []
        for x in self.super_Harshad_Array:
            self.Z_Score.append((x - self.Mean) / (self.std_Post))
    def Plot(self, MIN, MAX):
        self.Compute(MIN, MAX)
        self.Harshad_Array.sort()
        fig, ax = plt.subplots() 
        ax.plot(self.Harshad_Array, self.super_Harshad_Array_Log, marker='o')
        ax.set_title("Harshad vs. Super_Harshad")
        ax.set_xlabel("Harshad")
        ax.set_ylabel("Super Harshads")
        # Ensure the plot is shown **without blocking PySimpleGUI**
        fig.canvas.manager.show()
    def How_Many_Interval(self, MIN, MAX) -> None : 
        index = 0
        for Test in range(int(MIN), int(MAX)):
            X = Test
            TestArray = []
            while Test != 0:
                TestArray.append(Test % 10) 
                Test = Test // 10
            Sum = 0
            for i in TestArray: # get sum of individual digits.
                Sum = Sum + i
            if  X % Sum == 0 and X % 10 != 0: 
               index = index + 1
        self.window["NUMBER_OF_HARSHADS"].update(f"Number of Harshads: {index}-Harshads on this interval")
    def Single_Digit_Evaluation(self, HarshadTest):
        X = HarshadTest
        TestArray = []
        while HarshadTest != 0:
            TestArray.append(HarshadTest % 10) 
            HarshadTest = HarshadTest // 10
        Sum = 0
        for i in TestArray:
            Sum = Sum + i
        N = int(X / Sum)
        if  X % Sum == 0: 
            runningTotal = 0
            for j in range(0, int(N)):
                runningTotal = runningTotal + (10 ** (j*len(TestArray)))*(X)
            if N > 30: 
                self.window["SUPER_HARSHAD_MESSAGE"].update(f"{X} is a Harshad, and its corresponding Super-Harshad is: {X}...{X}...{X}. {X} repeats {N}-times.")
                self.window["LED"].update(button_color = 'green')
            else:
                self.window["SUPER_HARSHAD_MESSAGE"].update(f"{X} is a Harshad, and its corresponding Super-Harshad is: {runningTotal}")
                self.window["LED"].update(button_color = 'green')
        else:
            self.window["SUPER_HARSHAD_MESSAGE"].update(f"Sorry, {X} is not a Harshad")
            self.window["LED"].update(button_color = 'red')
    def Input_Validation(self, *argv):
        for value in argv:
            if value == '':
                sg.popup("Input cannot be blank!", keep_on_top = True)
                return True
        return False      
if __name__ == "__main__":
    Test = Harshad() # class instantiation
    Test.Executable()