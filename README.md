# Create Dynamic Domain which automatically change ip of domain as it changes on server.
## Why we need it?
- I have one personal Windows server, That I use for personal use and it is costly so keep it on for little amount of time.
- On the new start, it reset the ip address and I have to change it manually each time on 3rd party softwares.
- Can't assign Elastic IP, cause it costs if it is not assiend to running instances.
## Solution:
- We can use noip.com which provides one free dynamic DNS.
- We need to install softeware to our server, and it will automatically update domain ip if it changes.

# Steps:
- Go to: noip.com
- Create account (create account instead of using google login) Do the varification and Add username from profile section.
- Go to Dynamic DNS --> No-IP Hostnames --> Create Hostname --> Select name and domain for the DDNS, Put your server ip as A records..
- Go your serve and then following website: https://www.noip.com/download?page=win
- Donwload application on your server. You can find it for Windows, ubuntu and other servers.
- Install it and open it, Log in usign **USername** and **Password** --> Select your domain from the list --> Save --> Go to Preferances --> Select run auto. on boot up and log on.
- Now it's done. On the start of your server after few minues. your IP will be updated automatically to the domain.
- Now you have to use that configured domain to connect to your server.
