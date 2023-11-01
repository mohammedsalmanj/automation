from fabric.api import *
env.user = 'devops'
def greeting(msg):
  print "Good %s" % msg

def system_info():
  print "Disk Space"
  local("df -h")

  print "RAM size"
  local("free -m")

  print "System uptime."
  local("uptime")

def remote_exec():
  print "Get System Info"
  run("hostname")
  run("uptime")
  run("df -h")
  run("free -m")

  sudo("yum install mariadb-server -y")
  sudo("systemctl start mariadb")
  sudo("systemctl enable mariadb")

def web_setup(WEBURL, DIRNAME):
   print "###################################################################################"
   local("yum install zip unzip -y")

   print "###################################################################################"
   print "Installing dependencies"
   print "###################################################################################"
   sudo("yum install httpd wget unzip -y")

   print "###################################################################################"
   print "Start & enable service."
   print "###################################################################################"
   sudo("systemctl start httpd")
   sudo("systemctl enable httpd")

   print "###################################################################################"
   print "Downloading and pushing website to webservers."
   print "###################################################################################"
   #local(("wget -O website.zip %s") % WEBURL)
   local("wget --no-check-certificate -O website.zip %s" % WEBURL)
   local("unzip -o website.zip")
   
   print "###################################################################################"
   with lcd(DIRNAME):
       local("zip -r tooplate.zip * ")
       put("NiceAdmin.zip", "/var/www/html/", use_sudo=True)

   with cd("/var/www/html/"):
      sudo("unzip -o NiceAdmin.zip")

   sudo("systemctl restart httpd")

   print "Website setup is done."


#fab -H 192.168.56.62 -u devops web_setup:https://www.tooplate.com/zip-templates/2121_wave_cafe.zip,2121_wave_cafe
#fab -H 192.168.56.62 -u devops web_setup:https://bootstrapmade.com/content/templatefiles/NiceAdmin/NiceAdmin.zip,NiceAdmin
