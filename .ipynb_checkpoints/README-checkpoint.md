# Statistical Tests (for Location)

The aim of this project was to design a GUI with a backend that allows a user to perform statistical tests on data. A further aim was to architect a scalable solution, allowing myself to easily add more tests with little effort. The following tests are currently implemented:
* **One-sample t-test**
* **Wilcoxon signed-rank test**
* **Independent-samples t-test**
* **Wilcoxon rank rum test**
* **Mann-Witney U test**

I have separated my project into three modules: **`server.py`** contains the backend functionality, **`gui.py`** contains the frontend, and **`app.py`** links the two and runs the resulting app. I have also provided a Jupyter Notebook, **`stats_tests_overview.py`**, which contains an overview of all the implemented tests, including examples on some datasets. I have created copies of those datasets, located in the **`example_data`** folder, to be used with the GUI.

## Executing Programme

1. Run the app from the command line and while in the stats_tests directory:

```bash
  python app.py
```

2. Select a test, alternative hypothesis, mean to test (if applicable) and upload datasets (.txt/.csv). Click submit to run the test.

<p align="center">
    <img src="readme_images\gui.jpg" width="300"/>
</p>


## Future Improvements
* Add exception errors to GUI