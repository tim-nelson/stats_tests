"""This module contains a GUI for the Section B problem."""

import tkinter as tk
from tkinter import ttk

LARGE_FONT_STYLE = ("Ariel", 28)
SMALL_FONT_STYLE = ("Ariel", 10)
SMALL_FONT_STYLE_BOLD = ("Ariel", 10, "bold")

WHITE = "#FFFFFF"
BLACK = "#000000"


class GUI:
    def __init__(self):
        ## Initital set-up
        self.window = tk.Tk()  # create main window
        self.window.geometry("500x270")
        self.window.resizable(0, 0)  # disable resizing
        self.window.title("")
        self.window.iconbitmap("aspect_capital_logo.ico")

        ## Create frame and adjust grid spacing
        self.display_frame = self.create_display_frame()
        self.display_frame.rowconfigure(7, weight=1)
        self.display_frame.rowconfigure(10, weight=1)

        ## Create labels
        (
            self.title_label,
            self.math_opp_label,
            self.data_label,
            self.info_label,
            self.submit_label,
        ) = self.create_display_labels()

        ## Create dropdowns, textbox and submit button
        self.math_opp_var_temp = tk.StringVar()
        self.data_source_var_temp = tk.StringVar()
        self.math_opp_dropdown, self.data_source_dropdown = self.create_dropdowns(
            self.math_opp_var_temp, self.data_source_var_temp
        )

        ## Create textbox
        self.textbox_var_temp = tk.StringVar()
        self.textbox = self.create_textbox(self.textbox_var_temp)

        ## Create submit button
        self.submit_button = self.create_submit_button()
        
    ## Link with backend
    def extract_gui_vars_run_server(self):
        self.extract_gui_vars()
        self.server.run()

    def link_with_server(self, server):
        self.server = server
        self.submit_button["command"] = self.extract_gui_vars_run_server

    ## Extract variables
    def extract_gui_vars(self):
        self.math_opp_var = self.math_opp_var_temp.get()
        self.data_source_var = self.data_source_var_temp.get()
        self.textbox_var = self.textbox_var_temp.get()

    ## Create display frame functions
    def create_display_frame(self):  # area for title
        frame = tk.Frame(self.window, height=10, bg=WHITE)
        frame.pack(
            expand=True, fill="both"
        )  # allow frame to expand and fill any space around it
        return frame

    ## Create display labels (text) functions
    def create_display_labels(self):

        title_label = tk.Label(
            self.display_frame,
            text="Mathematical Operations",
            bg=WHITE,
            fg=BLACK,
            font=LARGE_FONT_STYLE,
        )
        title_label.grid(row=0, column=0, columnspan=2, sticky="W", padx=10, pady=5)

        math_opp_label = tk.Label(
            self.display_frame,
            text="Choose a mathematical operation:",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE_BOLD,
        )
        math_opp_label.grid(row=2, column=0, sticky="W", padx=15, pady=2)

        data_label = tk.Label(
            self.display_frame,
            text="Choose a data source:",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE_BOLD,
        )
        data_label.grid(row=4, column=0, sticky="W", padx=15, pady=2)

        info_label = tk.Label(
            self.display_frame,
            text="Additional info (e.g., file name, list of numbers):",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE_BOLD,
        )
        info_label.grid(row=6, column=0, sticky="W", padx=15, pady=2)

        submit_label = tk.Label(
            self.display_frame,
            text="Upon clicking submit, assume this calls your code's entry point!",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE,
        )
        submit_label.grid(row=9, column=0, columnspan=2, sticky="W", padx=15, pady=2)

        return title_label, math_opp_label, data_label, info_label, submit_label

    ## Create dropdown menus
    def create_dropdowns(self, var1, var2):
        # Choose a mathematical operation:
        options = ["Mean", "Median", "Mode", "Max", "Min", "Range", "Sum"]
        math_opp_dropdown = ttk.Combobox(
            self.display_frame, state="readonly", value=options, textvariable=var1
        )
        math_opp_dropdown.current(0)
        math_opp_dropdown.grid(row=3, column=0, sticky="W", padx=15, pady=2)

        # Choose a data source:
        options = ["File", "None"]
        data_source_dropdown = ttk.Combobox(
            self.display_frame, state="readonly", value=options, textvariable=var2
        )
        data_source_dropdown.current(0)
        data_source_dropdown.grid(row=5, column=0, sticky="W", padx=15, pady=2)

        return math_opp_dropdown, data_source_dropdown

    ## Create textbox
    def create_textbox(self, text):
        textbox = ttk.Entry(self.display_frame, width=20, textvariable=text)
        textbox.grid(row=6, column=1, sticky=tk.W)
        return textbox

    ## Create submit button
    def create_submit_button(self):
        button = ttk.Button(self.display_frame, text="Submit")
        button.grid(row=8, column=0, sticky=tk.W, padx=15, pady=0)
        # button["command"] = self.ExecuteRequest
        return button

    ## Run programme
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.run()