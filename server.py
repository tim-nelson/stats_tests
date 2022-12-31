"""A back-end for the GUI.

This module contains the class Server, which links to a GUI.

The GUI takes a statistical test variable, alternative hypothesis variable,
mean variable (if applicable), dataset 1 variable and dataset 2.

The selected test is applied to the dataset(s) and the output is displayed
in the output box.

Uncomment print(self.output_text), found at the bottom of this file,
to view the output in the terminal.
"""

import os
import re
import statistics
from tkinter import filedialog as fd

from scipy.stats import mannwhitneyu, t, ttest_1samp, ttest_ind, wilcoxon


class Server:
    ## GUI entry
    def link_with_gui(self, gui):
        """Create GUI object in order to extract variables."""
        self.gui = gui

    def extract_gui_vars(self):
        """ "Extract variables from GUI object."""
        self.math_opp_var = self.gui.math_opp_var
        self.alt_hyp_var = self.gui.alt_hyp_var
        self.mean_var = self.gui.mean_var
        self.data1_var = self.gui.data1_var
        self.data2_var = self.gui.data2_var

    ## Information extraction
    @staticmethod
    def extract_numbers_from_string(string: str) -> list:
        numbers = re.findall(r"(?<![a-zA-Z_])-?[-+.]?\d+\.?\d*", string)
        numbers = list(map(float, numbers))
        return numbers

    @staticmethod
    def extract_first_number_from_string(string: str) -> float:
        number = float(re.search(r"(?<![a-zA-Z_])-?[-+.]?\d+\.?\d*", string).group())
        return number

    def extract_datasets_numbers(self) -> list:
        """Returns all numbers from the textbox variable"""
        (data1, data2) = self.extract_numbers_from_string(
            self.data1_var
        ), self.extract_numbers_from_string(self.data2_var)
        return (data1, data2)

    def extract_mean_number(self) -> float:
        """Returns all numbers from the textbox variable"""
        try:
            mean = self.extract_first_number_from_string(self.mean_var)
        except:
            mean = 0
        return mean

    ## Statistical test
    def apply_stats_test(self) -> float:
        if self.data != []:
            match self.math_opp_var:
                case "One-sample t-test":
                    return ttest_1samp(
                        self.data[0], self.mean, alternative=self.alt_hyp_var
                    )
                case "Wilcoxon signed-rank test":
                    return wilcoxon(
                        [x - self.mean for x in self.data[0]],
                        alternative=self.alt_hyp_var,
                    )
                case "Independent-samples t-test":
                    return ttest_ind(
                        self.data[0],
                        self.data[1],
                        equal_var=True,
                        alternative=self.alt_hyp_var,
                    )
                case "Wilcoxon rank rum test":
                    return mannwhitneyu(
                        self.data[1],
                        self.data[0],
                        method="auto",
                        alternative=self.alt_hyp_var,
                    )
                case "Mann-Witney U test":
                    return mannwhitneyu(
                        self.data[1],
                        self.data[0],
                        method="auto",
                        alternative=self.alt_hyp_var,
                    )

    ## Run server
    def run(self):
        self.extract_gui_vars()
        self.data = self.extract_datasets_numbers()
        self.mean = self.extract_mean_number()
        self.stats_test_output = self.apply_stats_test()
        self.output_text = (
            # f"\nStatistical test: {self.math_opp_var}\n"
            # f"Alternative hypothesis: {self.alt_hyp_var} (mean = {self.mean})\n"
            # f"Data 1: {self.data1_var}\n"
            # f"Data 2: {self.data2_var}\n\n"
            f"{self.stats_test_output}"
        )
        # print(self.output_text)
        return self.output_text