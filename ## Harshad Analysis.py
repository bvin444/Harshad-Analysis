## Harshad Analysis
import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Harshad:
    def __init__(self):
        self.canvas_agg = None  # Keep track of the plot
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
                    [sg.Button("Plot", key = "PLOT")]
        ],
        size = (800, 500))
        PlottingArea = sg.Frame("Plotting Area", [
                [sg.Canvas(key="PLOT_FRAME")],  # Corrected this line to properly embed the plot
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
        for Test in range(int(MIN), int(MAX)):
            X = Test
            TestArray = []
            while Test != 0:
                TestArray.append(Test % 10) 
                Test = Test // 10
            Sum = 0
            for i in TestArray: # get sum of individual digits.
                Sum = Sum + i
            if  X % Sum == 0: 
                N = X / Sum # Divisibility Count.
                runningTotal = 0
                for j in range(0, int(N)):
                    runningTotal = runningTotal + (10 ** (j*len(TestArray)))*(X)
                print(runningTotal)
                super_Harshad_Array.append(runningTotal)
                Harshad_Array.append(X)
            # Create Matplotlib Figure
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(Harshad_Array, super_Harshad_Array, marker='o', linestyle='-')
        ax.set_xlabel("Harshad Numbers")
        ax.set_ylabel("Super Harshad Numbers")
        ax.set_title("Super Harshad Number Plot")

        if self.canvas_agg:
            self.canvas_agg.get_tk_widget().pack_forget()  # Remove previous plot

        # Draw new figure
        self.canvas_agg = self.draw_figure(self.window["PLOT_FRAME"], fig)
    def Input_Validation(self, *argv):
        for value in argv:
            if value == '':
                sg.popup("Input cannot be blank!")
                return True
            return False
    # Function to Draw Matplotlib Figure in PySimpleGUI
    def draw_figure(self, canvas, figure):
        canvas_widget = canvas.Widget()  # Get the TK canvas widget from PySimpleGUI
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas_widget)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
        return figure_canvas_agg  # Keep a reference to prevent garbage collection
                
if __name__ == "__main__":
    Test = Harshad() # class instantiation
    Test.Executable()