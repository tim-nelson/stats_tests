"""A back-end for the Section B problem.

This module contains the class Server, which links to a GUI.

The GUI takes a mathematical operation variable, data source variable,
and textbox variable (additional information).

If the data source variable is "File", the user is prompted to select
.txt and/or .csv files. Numbers are extracted from all selected files
and the additional information variable. The selected mathematical
operation is then applied to those numbers and presented in a .txt file.
The file name is extracted from the textbox variable and set to
"untitled" if the user does not type a filename.

Uncomment print(self.file_text), found at the bottom of this file,
to view the textfile's contents in the terminal.
"""

import os
import re
import statistics
from tkinter import filedialog as fd


class Server:
    ## GUI entry
    def link_with_gui(self, gui):
        """Create GUI object in order to extract variables."""
        self.gui = gui

    def extract_gui_vars(self):
        """"Extract variables from GUI object."""
        self.math_opp_var = self.gui.math_opp_var
        self.data_source_var = self.gui.data_source_var
        self.textbox_var = self.gui.textbox_var

    ## Information extraction
    @staticmethod
    def select_files() -> tuple:
        """Opens File Explorer for the user to select files"""
        filetypes = (("Files", "*.txt .csv"),)
        filepaths = fd.askopenfilenames(filetypes=filetypes)
        return filepaths
    
    @staticmethod
    def extract_numbers_from_string(string: str) -> list:
        numbers = re.findall(r"(?<![a-zA-Z_])-?[-+.]?\d+\.?\d*", string)
        return numbers

    def extract_file_numbers(self) -> list:
        """Returns all numbers from all user selected files."""
        numbers = []
        if self.data_source_var == "File":
            filepaths = self.select_files()
            files_and_extensions = [
                {"filepath": filepath, "file_extension": os.path.splitext(filepath)[1]}
                for filepath in filepaths
            ]
            for file in files_and_extensions:
                with open(file["filepath"], "r") as file:
                    lines = file.readlines()
                for line in lines:
                    numbers += self.extract_numbers_from_string(line)
                    
        return numbers

    def extract_textbox_numbers(self) -> list:
        """Returns all numbers from the textbox variable"""
        numbers = self.extract_numbers_from_string(self.textbox_var)
        return numbers

    def concatenate_numbers(self) -> list[float]:
        """Combine all numbers and return the list of floats"""
        return list(
            map(float, self.extract_file_numbers() + self.extract_textbox_numbers())
        )

    def extract_textbox_filename(self) -> str:
        """Combines all letters/letters directly followed by numbers into a filename."""
        new_filename = "".join(re.findall(" ?[a-zA-Z_]+\d*", self.textbox_var))
        if new_filename == "":
            return "unititled"
        else:
            return new_filename

    ## Mathematical operations
    def apply_math_opp(self) -> float:
        if self.numbers != []:
            match self.math_opp_var:
                case "Mean":
                    return statistics.mean(self.numbers)
                case "Median":
                    return statistics.median(self.numbers)
                case "Mode":
                    return statistics.mode(self.numbers)
                case "Max":
                    return max(self.numbers)
                case "Min":
                    return min(self.numbers)
                case "Range":
                    return max(self.numbers) - min(self.numbers)
                case "Sum":
                    return sum(self.numbers)

    ## Create text file
    def create_text_file(self):
        file = open(f"{self.filename}.txt", "w")
        file.write(self.file_text)

    ## Run server
    def run(self):
        self.extract_gui_vars()
        self.numbers = self.concatenate_numbers()
        self.math_opp_result = self.apply_math_opp()

        self.filename = self.extract_textbox_filename()
        self.file_text = (
            f"Mathematical operation: {self.math_opp_var}\n"
            f"Numbers: {self.numbers}\n\n"
            f"{self.math_opp_var} of numbers = {self.math_opp_result}"
        )

        print(self.file_text)
        self.create_text_file()