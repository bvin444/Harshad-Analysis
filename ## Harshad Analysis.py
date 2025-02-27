## Harshad Analysis
import PySimpleGUI as sg
class Harshad:
    def __init__(self):
        pass
    def Executable(self):
        self.window = self.create_main_window()
        while True:
            event, values = self.window.read()
            if event == (sg.WIN_CLOSED): break
            if self.Input_Validation(values["USER_INPUT"]): continue
            elif event == "SUBMIT": self.Harshad_Test_Function(int(values["USER_INPUT"]))
        self.window.close()
    def create_main_window(self):
        layout = [
                    [sg.Text("Please enter an integer"), sg.Input("", key = "USER_INPUT")],
                    [sg.Button("Submit", key = "SUBMIT")],
                    [sg.Button("", key = "LED", button_color = 'white')],
                    [sg.Text("        ", key = "SUPER_HARSHAD_MESSAGE")]
                 ]
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

    def Input_Validation(self, User_Input_Val):
        if User_Input_Val == '':
            sg.popup("Input cannot be blank!")
            return True
        else:
            return False
if __name__ == "__main__":
    Test = Harshad() # class instantiation
    Test.Executable()