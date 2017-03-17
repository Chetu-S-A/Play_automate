# Play_automate
This is a script that can be used to automate the deployment of a play application



Features:
1) pull code from git repository
2) push the snapshot file to Google Drive

Requirments:
venv: All the necessary libraries are in the "env" directory. 
  If you do not have virtual environment, please install it.
Once you install virtualenv, run the following command:

$ sources ./env/bin/activate 

Now, venv is activatd.


To run the script:
Add only your project information in "project_info.json" .
Please do not make any other changes in project_info.json.

Download your google drive credentials and name it as client_secrets.json (please keep the name as "client_secrets.json") and save it in the project folder.

run the script using 

$ ./auto_deploy.py

  
