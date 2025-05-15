The file Dashboard using powerbi.pbix is the simple Dashboard crated with the sample data set of a educational center (the data set is generated using Chat Gpt)

The file educational_center_large_sample.xlsx is the Sample data set used to create that power bi dashboard

TO RUN THE PYTHON DASHBOARD

step 1: download the files to your required location(dashboard.py,educational_center_python_sample.xlsx,requirements.txt)

step2: open the folder in the VS Code app and open dashboard.py

step3: open terminal and type the following "python -m venv venv" to create a virtual environment

step4: once the venv is created activate the venv by typing the following in the terminal ".\venv\scripts\activate"

step5: now to install the required libraries just type this in terminal "pip install -r requirements.txt"
this will install all the required libraries in he virtual environment

step6: now if the venv is activated type the following in the terminal to run the dashboard "streamlit run Dashboard.py"

step7: if the venv is not activated or any error is shown then type ".\venv\scripts\activate" and then type try the step6.
