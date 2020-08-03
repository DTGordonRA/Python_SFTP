import configparser
import pysftp
import sys
import os
import venv

venv_dir = os.path.join(os.path.dirname(__file__), 'sftp_env')
venv.create(venv_dir)
# TODO change bin to Scripts an activate_this.py to activate.bat in windows version
exec(open(os.path.join(venv_dir, 'bin', 'activate_this.py')).read())

config = configparser.ConfigParser()
config.read('config.txt')

# Use this line if you're using a username and password rather than an ssh key
# with pysftp.Connection( host = config['host']["hostname"], username = config['user']['username'], password = config['user']['password']) as sftp:
with pysftp.Connection( host = config['host']["hostname"], private_key = config['key']['location'], private_key_pass = config['key']['pass']) as sftp:
    # Go to directory specified in command line
    with sftp.cd('{}'.format(sys.argv[1])):
        # Upload file specified in command line
        sftp.put('{}'.format(sys.argv[2]))