Setup:
1) CD into Python_SFTP directory
2) Run command {python -m venv sftp_venv}
3) Run command {sftp\Scripts\activate.bat}
4) Run command {pip install -r requirements.txt}
	If you intend to use this script after setup skip
	Use step 1.

Use:  
1) Activate venv: {sftp_venv\Scripts\activate.bat}
2) Use the command: {python python_sftp.py [arg1] [arg2]}
	Repeat for all files you wish to upload
3) Deactivate venv: {deactivate}

arg1: Path to target directory in remote destination
arg2: Path to local file to upload