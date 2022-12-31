# Statistical Tests (for Location)

This project aimed to design a GUI with a backend that allows a user to perform statistical tests on data. Another goal was to design a solution that would let me add more tests with little work. The following tests are currently implemented:
* **One-sample t-test**
* **Wilcoxon signed-rank test**
* **Independent-samples t-test**
* **Wilcoxon rank rum test**
* **Mann-Witney U test**

I have separated my project into three modules: **`server.py`** contains the backend functionality, **`gui.py`** contains the frontend, and **`app.py`** links the two and runs the resulting app. I have also provided a Jupyter Notebook, **`stats_tests_overview.py`**, which contains an overview of the implemented tests, including examples on some datasets. I have created copies of those datasets in the **`example_data`** folder to be used with the GUI.

## Executing Programme

1. Run the app from the command line and while in the stats_tests directory:

```bash
  python app.py
```

2. Select a test, alternative hypothesis, mean to test (if applicable) and upload datasets (.txt/.csv). Click submit to run the test.

<p align="center">
    <img src="readme_images\gui.jpg" width="300"/>
</p>


## Future Additions/Improvements
* Exception errors to GUI
* Confidence Intervals for t-test and Wilcoxon
* Hodges-Lehmann estimator
* Paired samples t-test
* Wilcoxon signed rank test: paired replicates
* Bayes inference