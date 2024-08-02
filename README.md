# Create Dynamic DNS for the hosted zones in Route 53 using python script.
## Installing dependencies:
- boto3 and requests.
  on Ubuntu:
  ```
  sudo apt install python3-boto3
  sudo apt install python3-requests
  ```
- Create script files on you server. You'll find it on the github repo. Paste the script and add your `hosted zone id`, `domain name`, `access key` and `Secrate access key`.
## Set up cronjob to check it every 5 minues to update ips.
- Make file executable:
  ```
  sudo chmod +x ddns.py
  ```
- edit crontab file:
  ```
  crontab -e
  ```
- Add following commnad.
  ```
  */5 * * * * /usr/bin/python3 /home/ubuntu/update_dns.py
  ```
- Enable cron tab:
  ```
  sudo systemctl enable cron
  sudo systemctl start cron
  ```
- check cron status:
  ```
  sudo systemctl status cron
  ```
## INstead of running every 5 miniutes, set up to run at server boot up.
- Create the systemd service file:
  ```
  sudo nano /etc/systemd/system/update-dns.service
  ```
- Add the configuration:
  ```
  [Unit]
  Description=Update Route 53 DNS with Public IP
  After=network.target
  
  [Service]
  ExecStart=/usr/bin/python3 /home/ubuntu/ddns.py
  WorkingDirectory=/home/ubuntu/
  StandardOutput=inherit
  StandardError=inherit
  Restart=always
  User=ubuntu
  
  [Install]
  WantedBy=multi-user.target
  ```
- Reload systemd:
  ```
  sudo systemctl daemon-reload
  ```
- Enable the service:
  ```
  sudo systemctl enable update-dns.service
  ```
- Start the service:
  ```
  sudo systemctl start update-dns.service
  ```
- Check the service status:
  ```
  sudo systemctl status update-dns.service
  ```
