# pandas_repo
Pandas Sample Implementation
1. Create a Project Directory.
	For eg: D:\Pandas_Project

2. Use command under the created Project Directory : git clone https://github.com/cpriyaindira/pandas_repo.git

3. Move to pandas_repo directory using : cd pandas_repo

4. Now checkout branch pandas_repo as : git checkout pandas_repo

5. Open the Project directory (for eg D:\Pandas_Project) in Pycharm

6. To setup virtual env in Pycharm : File --> Settings --> Project --> Python Interpreter. Provide virtual env location and click OK. For eg :  D:\Pandas_Project\venv

7. Alternatively use virtualenv venv to create a virtual environment with name "venv" under the Project directory. For eg: virtualenv D:\Pandas_Project\venv.
   Activate the venv created as D:\Pandas_Project\venv\Scripts\activate

8. Once the interpreter is added , to install the python packages needed to run this pandas program :
	8.1 Go to Tools --> Sync Python requirements
	8.2 Select the Package requirements file location. For eg: D:\Pandas_Project\pandas_repo\requirements.txt
	8.3 Select Version in requiremnts --> "Don't specify version"
	8.4 Click OK

9. Now Click on "Install Requirements" displayed on top of the Pycharm Window to install the Package Requirements which are not satisfied.
   Alternatively we can run  pip install -r "path_to_requirements.txt" . For eg : pip install -r D:\Pandas_Project\pandas_repo\requirements.txt
   (Make sure the virtual environment created is activated before running pip install)

10. Now Add Configuration to run the pandas code. Under the Configuration section add a Name and provide the script path. For eg: D:\Pandas_Project\pandas_repo\pandas_sample.py
    Alternatively , in command line interface we can change directory to the script path as : cd D:\Pandas_Project\pandas_repo
	and we can run  as : python "script_name.py". For eg : python pandas_sample.py

11. The output csv files will be created under the Project directory craeted in Step 1. For eg: D:\Pandas_Project\output_csv_files

	11.1 Extract confirmed cases by state wise for each day. --> File name : State_Date_Wise_Confirmed_Cases.csv
	11.2 Create a report of total deaths state wise in the descending order. --> File name : State_Wise_Deaths_Descending.csv
	11.3 Create a report of consolidated data for all states by month. --> File name: All_States_Month_Wise_Consolidation.csv
