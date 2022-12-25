"""A GUI placeholder for the Section B problem.

This module contains the class GUI. A GUI object provides an input for
the server (backend). The __init__ and extract_gui_variables methods
simulate the users input. Please change the user inputs as desired.
"""

class GUI:
    def __init__(self):
        """Set temporary variables that update while the user selects inputs.
        
        The server accepts the following inputs:
        self.math_opp_var_temp = ["Mean", "Median", "Mode", "Max", "Min", "Range", "Sum"]
        self.data_source_var_temp = ["File", "None"]
        """
        self.math_opp_var_temp = "Mean"
        self.data_source_var_temp = "None"
        self.textbox_var_temp = "test_file123 0.1 .2 3,4 -5"

    def extract_gui_vars(self):
        """Set final variables (to be called after Submit button is clicked.)"""
        self.math_opp_var = self.math_opp_var_temp
        self.data_source_var = self.data_source_var_temp
        self.textbox_var = self.textbox_var_temp
        
    ## Link with backend
    # We do not set a command as there is no submit button. Below is a
    # commented example for setting a tkinter button command.
    def link_with_server(self, server):
        """"Create a server object and set a command for the Submit button."""
        self.server = server
        #self.submit_button["command"] = self.extract_gui_vars_run_server
        
    def extract_gui_vars_run_server(self):
        """Submit button command: set final variables then run server (backend)."""
        self.extract_gui_vars()
        self.server.run()
        
    ## Run GUI
    # As we do not have a GUI, we instead immediately call the Submit button command.
    def run(self):
        """Function to run the GUI."""
        self.extract_gui_vars_run_server()