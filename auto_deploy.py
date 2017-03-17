#!/bin/python3
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from glob import glob
def run_proj():
    run_it = os.system('sbt run')

def git_pull():
    from json import loads
    info = loads(open('project_info.json').read())
    print(" Project name: " + info['project_name'])
    print("Pulling code from " + info['repo'])
    if os.path.exists('.git/'):
        os.system('git pull ' + info['repo'])
    else:
        init = input(" Not a project folder.. To use git you need to inirialize the git project folder. Do you want to run 'git init' now? y/n \n")
        if init == 'y' or init == 'Y' or init == '':
            os.system('git init')
            os.system('git pull ' + info['repo'])
        else:
            print("Please run scropt from a valid git initialized project folder\n")
            os._exit(1)

#    os.chdir(info['project_name'])

pull_status = input("Do you want to pull a new project or deploy an existing project? y/n ")
if pull_status == 'y' or pull_status == 'Y' or pull_status == '':
    git_pull()
elif pull_status == 'n' or pull_status == 'N':
    pass
else:
    print("please select a valid input\n")
    os._exit(1)
    

if not os.path.exists('build.sbt'):
    print("Not a valid project folder")
    os._exit(1)
dist = os.popen('activator dist').read()
exit_status = os.popen('echo $?').read()
exit_status = int(exit_status)
if exit_status == 0:
    print("ready to be deployed")
    try:
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        gauth = GoogleAuth()
        drive = GoogleDrive(gauth)
    except:
        print("File not found... Plese include the file \"client_secrets.json\" ")
    else:
        file1 = drive.CreateFile({'title': 'snapshot.zip'})
        file2 = drive.CreateFile()
        file2.SetContentFile(glob('./target/universal/*[SNAPSHOT]*.zip')[0])
        file2.Upload()
        run_proj()
else:
    print("errors eccored")
    print("error logs stored in error.log")
    f = open('error.log','w')
    f.write(dist)
    f.closed()

