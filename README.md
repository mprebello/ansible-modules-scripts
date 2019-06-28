This script contain some technics used in ansible to make a google report and take some decisions

to begin create the files below:

copy code/CommonTasks to /etc/ansible/roles

-> set the default varaibles

mv /etc/ansible/roles/CommonTasks/scripts/Information/openticket.csv.example /etc/ansible/roles/CommonTasks/scripts/Information/openticket.csv

mv /etc/ansible/roles/CommonTasks/scripts/ManageHostDetails/config_vars_host_details.py.example /etc/ansible/roles/CommonTasks/scripts/ManageHostDetails/config_vars_host_details.py

mv /etc/ansible/roles/CommonTasks/scripts/ManageReport/report_config_vars.py.example /etc/ansible/roles/CommonTasks/scripts/ManageReport/report_config_vars.py

mv /etc/ansible/roles/CommonTasks/scripts/ManageWarpTicket/config_vars.py.example /etc/ansible/roles/CommonTasks/scripts/ManageWarpTicket/config_vars.py

mv /etc/ansible/roles/CommonTasks/scripts/Sendmail/config_vars.py.example /etc/ansible/roles/CommonTasks/scripts/Sendmail/config_vars.py

mv /etc/ansible/roles/CommonTasks/tasks/main.yml /etc/ansible/roles/CommonTasks/tasks/main.yml.example

#install dependencies
pip install prettytable ansible mysql-connector-python prettytable pykerberos pywinrm requests
