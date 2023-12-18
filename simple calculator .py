import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # the Entry widgets for display:-
        self.display_var = tk.StringVar()
        self.display_entry = tk.Entry(root, textvariable=self.display_var, font=('Helvetica', 18), justify='right')
        self.display_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky='nsew')

        #the Buttons:-
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('.', 4, 4), ('A', 1, 4)
        ]

        # Configuring the grid rows and columns to expand with  the window size:-
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

        # Button styling :-
        button_style = {'font': ('Helvetica', 16), 'width': 4, 'height': 2}

        # Creation of the  buttons:-
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, command=lambda t=text: self.on_button_click(t), **button_style)
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

    def on_button_click(self, value):
        current_display = self.display_var.get()

        if value == 'C':
            self.display_var.set('')
        elif value == '=':
            try:
                result = eval(current_display)
                self.display_var.set(str(result))
            except Exception as e:
                self.display_var.set('Error')
        elif value == 'A':
            if current_display:
                self.display_var.set(current_display[:-1])
        else:
            self.display_var.set(current_display + value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
