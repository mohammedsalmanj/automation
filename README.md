#########################fabric automation#######################################
###########################################################################################################################################################
###########################################################################################################################################################

#install fabric
#pip install fabric
#mkdir fabric_project

#Create a Python virtual environment :Set up a virtual environment to isolate your project's dependencies. Replace myenv with your desired environment name.
#python -m venv myenv
#source myenv/bin/activate
#curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#python get-pip.py
#curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py


remote server:
#useradd devops
#passwd devops
#visudo
add the user and NOPASSWD: ALL
#vi /etc/ssh/sshd_config
PasswordAUth Yes
#cat /etc/ssh/sshd_config
#systemctl restart sshd
from master to other remote ip's
#ssh-keygen
#ssh-copy-id devops@192.168.56.62


#Test
cd /opt/pyscript/fabric
./fabfile.py
fab -l
vim fabfile.py
script
fab -l
fab system_info
fab remote_exec
fab -H 192.168.56.62 -u devops web_setup:https://bootstrapmade.com/content/templatefiles/NiceAdmin/NiceAdmin.zip,NiceAdmin
fab -H remoteip -username web_setup:url,unzipname


###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################

