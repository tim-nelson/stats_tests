"""This module contains a GUI for performing statistical tests."""

import re
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

LARGE_FONT_STYLE = ("Ariel", 28)
SMALL_FONT_STYLE = ("Ariel", 10)
SMALL_FONT_STYLE_BOLD = ("Ariel", 10, "bold")

WHITE = "#FFFFFF"
BLACK = "#000000"
LIGHT_GREY = "#F5F5F5"


class GUI:
    def __init__(self):
        ## Initital set-up
        self.window = tk.Tk()  # create main window
        # self.window.geometry("800x500")#("570x350")
        self.window.configure(background=WHITE)
        self.window.resizable(0, 0)  # disable resizing in both axis
        self.window.title("")
        self.window.iconbitmap("stats.ico")

        ## Create frames
        (
            self.frame_title,
            self.frame_test,
            self.frame_data,
            self.frame_output,
        ) = self.create_frames()

        ## Create variables
        self.var_stats_test_temp = tk.StringVar()
        self.var_alt_hyp_temp = tk.StringVar()
        self.var_output = tk.StringVar()

        ## Create dropdown options
        self.options = {
            "One-sample t-test": (["less", "greater", "two-sided"], "mean"),
            "Wilcoxon signed-rank test": (["less", "greater", "two-sided"], "mean"),
            "Independent-samples t-test": (["less", "greater", "two-sided"], "no_mean"),
            "Wilcoxon rank rum test": (["less", "greater", "two-sided"], "no_mean"),
            "Mann-Witney U test": (["two-sided"], "no_mean"),
        }

        ## Create labels
        (
            self.label_title,
            self.label_stats_test,
            self.label_alt_hyp,
            self.label_mean,
            self.label_data1,
            self.label_data2,
            self.label_test_result,
            self.label_output,
        ) = self.create_labels()

        ## Create dropdowns
        (self.math_opp_dropdown, self.alt_hyp_dropdown) = self.create_dropdowns(
            self.var_stats_test_temp, self.var_alt_hyp_temp
        )

        ## Create textbox
        (
            self.mean_textbox,
            self.data1_textbox,
            self.data2_textbox,
        ) = self.create_textboxes()

        ## Create submit button
        (
            self.submit_button,
            self.data1_upload_button,
            self.data2_upload_button,
        ) = self.create_buttons()

        
    ## Link with backend and display output in GUI
    def extract_gui_vars_run_server(self):
        self.extract_gui_vars()
        output = self.server.run()
        self.var_output.set(output)

    def link_with_server(self, server):
        self.server = server
        self.submit_button["command"] = self.extract_gui_vars_run_server

        
    ## Extract variables
    def extract_gui_vars(self):
        self.math_opp_var = self.var_stats_test_temp.get()
        self.alt_hyp_var = self.var_alt_hyp_temp.get()
        self.mean_var = self.mean_textbox.get("1.0", "end-1c")
        self.data1_var = self.data1_textbox.get("1.0", "end-1c")
        self.data2_var = self.data2_textbox.get("1.0", "end-1c")

        
    ## Create frames functions
    def create_frames(self):
        frame_title = tk.Frame(self.window, bg=WHITE)
        frame_title.grid(row=0, column=0, columnspan=2, sticky=tk.SW)

        frame_test = tk.Frame(self.window, bg=WHITE)
        frame_test.grid(row=1, column=0, columnspan=1)

        frame_data = tk.Frame(self.window, bg=WHITE)
        frame_data.grid(row=1, column=1, columnspan=2)

        frame_output = tk.Frame(self.window, bg=WHITE)
        frame_output.grid(row=2, column=0, columnspan=3)
        
        return frame_title, frame_test, frame_data, frame_output

    
    ## Create labels (text) functions
    def create_labels(self):
        label_title = tk.Label(
            self.frame_title,
            text="Statistical Tests",
            bg=WHITE,
            fg=BLACK,
            font=LARGE_FONT_STYLE,
        )
        label_title.grid(row=0, column=0, columnspan=1, sticky="W", padx=10, pady=5)

        label_stats_tets = tk.Label(
            self.frame_test,
            text="Choose a test:",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE_BOLD,
        )
        label_stats_tets.grid(row=0, column=0, sticky="W", padx=15, pady=2)

        label_alt_hyp = tk.Label(
            self.frame_test,
            text="Choose H1:",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE_BOLD,
        )
        label_alt_hyp.grid(row=2, column=0, sticky="NW", padx=15, pady=2)

        label_mean = tk.Label(
            self.frame_test,
            text="Choose a mean:",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE_BOLD,
        )
        label_mean.grid(row=5, column=0, sticky="W", padx=15, pady=2)

        label_data1 = tk.Label(
            self.frame_data,
            text="Data 1:",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE_BOLD,
        )
        label_data1.grid(row=0, column=0, sticky="W", padx=15, pady=2)

        label_data2 = tk.Label(
            self.frame_data,
            text="Data 2:",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE_BOLD,
        )
        label_data2.grid(row=0, column=1, sticky="W", padx=15, pady=2)

        label_test_result = tk.Label(
            self.frame_output,
            text="Test Result",
            bg=WHITE,
            fg=BLACK,
            font=SMALL_FONT_STYLE_BOLD,
        )
        label_test_result.grid(
            row=2, column=0, columnspan=3, sticky="W", padx=15, pady=0
        )

        # Output
        label_output = tk.Label(
            self.frame_output,
            textvariable=self.var_output,
            anchor=tk.N,
            width=76,
            height=1,
            borderwidth=2,
            bg=WHITE,
            relief="groove",
        )
        label_output.grid(row=3, column=0, columnspan=3, sticky=tk.NW, padx=15, pady=10)

        return (
            label_title,
            label_stats_tets,
            label_alt_hyp,
            label_mean,
            label_data1,
            label_data2,
            label_test_result,
            label_output,
        )

    
    ## Create dropdown menus
    def create_dropdowns(self, var1, var2):
        # Choose a statistical test:
        math_opp_dropdown = ttk.Combobox(
            self.frame_test,
            state="readonly",
            value=list(self.options.keys()),
            textvariable=var1,
        )
        math_opp_dropdown.current(0)
        math_opp_dropdown.bind("<<ComboboxSelected>>", self.update_hyp)
        math_opp_dropdown.grid(row=1, column=0, sticky="W", padx=15, pady=2)

        # Choose a hypothesis:
        alt_hyp_dropdown = ttk.Combobox(
            self.frame_test,
            state="readonly",
            textvariable=var2,
            value=self.options[list(self.options.keys())[0]][0],
        )
        alt_hyp_dropdown.current(0)
        alt_hyp_dropdown.grid(row=3, column=0, sticky="W", padx=15, pady=2)

        return math_opp_dropdown, alt_hyp_dropdown

    
    ## Create textboxes
    def create_textboxes(self):
        # Mean
        textbox_mean = tk.Text(
            self.frame_test, width=10, height=1, borderwidth=2, relief="groove"
        )
        textbox_mean.grid(row=7, column=0, sticky=tk.W, padx=15, pady=2)

        # Data1
        textbox_data1 = tk.Text(
            self.frame_data, width=20, height=6, borderwidth=2, relief="groove"
        )
        textbox_data1.grid(row=2, column=0, sticky=tk.W, padx=15, pady=5)

        # Data2
        textbox_data2 = tk.Text(
            self.frame_data, width=20, height=6, borderwidth=2, relief="groove"
        )
        textbox_data2.grid(row=2, column=1, sticky=tk.W, padx=15, pady=5)

        return textbox_mean, textbox_data1, textbox_data2

    
    ## Create submit button
    def create_buttons(self):
        button_submit = ttk.Button(self.frame_output, text="Submit")
        button_submit.grid(row=1, column=1, sticky=tk.S, padx=15, pady=0)

        button_data1_upload = ttk.Button(self.frame_data, text="Upload file")
        button_data1_upload.grid(row=1, column=0, sticky=tk.W, padx=15, pady=0)
        button_data1_upload["command"] = self.upload_data1

        button_data2_upload = ttk.Button(self.frame_data, text="Upload file")
        button_data2_upload.grid(row=1, column=1, sticky=tk.W, padx=15, pady=0)
        button_data2_upload["command"] = self.upload_data2

        return button_submit, button_data1_upload, button_data2_upload

    
    ## GUI Functionality support functions
    @staticmethod
    def select_file() -> str:
        """Opens File Explorer for the user to select files"""
        filetypes = (("Files", "*.txt .csv"),)
        filepath = fd.askopenfilename(filetypes=filetypes)
        return filepath

    @staticmethod
    def extract_numbers_from_string(string: str) -> list:
        numbers = re.findall(r"(?<![a-zA-Z_])-?[-+.]?\d+\.?\d*", string)
        numbers = list(map(float, numbers))
        return numbers    

    def extract_file_numbers(self) -> list:
        """Returns all numbers from all user selected files."""
        numbers = []
        filepath = self.select_file()
        if filepath != "":
            with open(filepath, "r") as file:
                lines = file.readlines()
            for line in lines:
                numbers += self.extract_numbers_from_string(line)
        return numbers
    
    
    ## GUI Functionality functions
    def update_hyp(self, event):
        test = self.var_stats_test_temp.get()
        self.alt_hyp_dropdown.set(self.options[test][0][0])
        self.alt_hyp_dropdown["values"] = self.options[test][0]

        if self.options[test][1] == "mean":
            self.mean_textbox.config(bg=WHITE, state=tk.NORMAL)
        else:
            self.mean_textbox.config(bg=LIGHT_GREY, state=tk.DISABLED)

    def enable_mean(self):
        mean_textbox.config(state=DISABLED)

    def upload_data1(self):
        numbers = self.extract_file_numbers()
        if numbers != []:
            self.data1_textbox.delete("1.0", "end")
            self.data1_textbox.insert(tk.INSERT, numbers)

    def upload_data2(self):
        numbers = self.extract_file_numbers()
        self.data2_textbox.delete("1.0", "end")
        self.data2_textbox.insert(tk.INSERT, numbers)

        
    ## Run programme
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.run()