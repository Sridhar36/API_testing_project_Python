# paramiko python:
# we make ssh connection from Python to server


# we need:host, uname, pwd
# (server should be password enabled)

# 1. launch AWS instance - setting up serever
# 2. update configs on server to accept SSH connections.
# 3. Build Paramika SSH connection.

# paramiko library helps in connecting to server.

import paramiko as parami

#to start connection
# ssh = paramiko.SSHClient() - too create a stream of connection.
#
# ssh.connect(ip, port, uname, pwd) - connects with linux server.
#
# # By default it tries to authenticate with public or private keys, if we dont have those we can suppress that check by using one step..
# #
# shh.set_missing_host_key_poolicy(paramiko.AutoPolicy) -- add this before calling connect
#
#
# #to run commands:
# stdin, stdout, stderr = ssh.exec_command("ls -a")  #to execute command
# #return type is 3 variables.
#
# stdout.readlines = to read the lines.
#
# ssh.close()  - to close the connection
#
#
# to upload file from local system to server.

# SFTP protocal to upload or download the files from server.


sftp = ssh.open_sftp() # to open sftp connection
destinationpath = "script.py"
localpath = "relative path of file"

#to upload file
sftp.put(localpath, destinationPath)

# once uploaded the files trigger the ccommand to exe batch jojb.

ssh.exec_command("python script.py") #this script should be present on AWS server.

# here python name.py is the command to run Python, which by default installed in AWS server.  script is something we uploaded.

# to download file to local system:

sftp.get("destination path", "where you want it to be placed")
