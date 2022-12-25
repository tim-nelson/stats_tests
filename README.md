# Section B - Mathematical Operations

I have separated my answer into three modules: **`server.py`** contains the backend functionality, **`gui_placeholder.py`** substitutes for an actual GUI, and **`app.py`** links the two and runs the resulting app. I have also provided two files containing numbers as example/testing data sources, **`data1.txt`** and **`data2.csv`**.

My solution allows the user to select one of the following mathematical operations: **Mean**, **Median**, **Mode**, **Max**, **Min**, **Range**, and **Sum**. The user can also select **File** or **None** as a data source. (I have not considered exceptions for invalid inputs as, when using a GUI, the user is restricted by the dropdown menu.) If the user selects File, then, upon clicking Submit, they are prompted to select .txt/.csv files from their computer. Then, all the numbers in the selected file(s) are extracted, as well as any numbers provided in the *Additional info* textbox. The selected mathematical operation is applied to those numbers, and the result is outputted as a .txt file. Its file name is extracted from the *Additional info* texbox and is set to "untitled" if no name is given.

## Executing programme

1. Open **`gui_placeholder.py`** in an editor and set the following variables to your desired inputs:
```python
self.math_opp_var_temp = "Mean"
self.data_source_var_temp = "None"
self.textbox_var_temp = "test_file123 0.1 .2 3,4 -5"
```

2. To prevent creating a .txt file or to display the .txt file output in a terminal, comment/uncomment the following code located at the bottom of the server.py file:

```python
#print(self.file_text)
self.create_text_file()
```

3. Run the app from the command line and while in the math_opps directory:

```bash
  python app.py
```

#### Output examples

text file output             |  cmd output
:-------------------------:|:-------------------------:
<img src="readme_images\txt_output_example.jpg" height="100" width="200" >  |  <img src="readme_images\cmd_output_example.jpg" height="100" width="200" >


## Additional Information
This is my first Python project where I design a backend that must integrate with a frontend UI. Therefore, to help me learn, better understand the task and test my backend design, I learned how to create a GUI in tkinter and replicated the GUI pictured in the question (below). As Section B explicitly states not to include UI-generating code, I have omitted the file containing the GUI. However, I will gladly share the file if you want to see it.

<p align="center">
    <img src="readme_images\gui.jpg" width="300"/>
</p>

To run app.py with the GUI, you would only have to place the file in the math_opps directory and change `from gui_placeholder import GUI` to `from gui import GUI` at the top of **`app.py`**.