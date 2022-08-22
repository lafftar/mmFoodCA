##Save Github Passwd
```bash
git config --global credential.helper store
```

##Pull, CD in, set some basis
```bash
alias cls=clear;\
 yes | sudo add-apt-repository ppa:deadsnakes/ppa;\   
 yes | sudo apt-get update;\
 yes | sudo apt install python3.10;\
 yes | sudo apt install python3.10-venv;\
 alias py=python3.10;\
 git config --global credential.helper store;\
 git clone https://github.com/lafftar/mmFoodCA;\
 cd mmFoodCA;\
 python3.10 -m venv venv;\
 source venv/bin/activate;\
 pip install -r requirements.txt;
```

##Install cerbot, gen new certificate
```bash
sudo apt-get remove certbot;\
sudo snap install core; sudo snap refresh core;\
sudo snap install --classic certbot;\
sudo ln -s /snap/bin/certbot /usr/bin/certbot;\
sudo ufw allow 80; sudo ufw allow 443;\
yes | sudo certbot certonly --standalone --agree-tos --non-interactive -m admin@mmfood.ca -d mmfood.ca
```


###Happening in diff tmux windows. Need to set aliases and venv again.
##Startup https
```bash
sudo lsof -t -i tcp:443 -s tcp:listen | sudo xargs kill;\
alias cls=clear;\
alias py=python3.10;\
source venv/bin/activate;\
uvicorn server.api:app\
 --ssl-certfile=/etc/letsencrypt/live/mmfood.ca/fullchain.pem\
 --ssl-keyfile=/etc/letsencrypt/live/mmfood.ca/privkey.pem\
 --host 0.0.0.0 --port 443 --workers 4
```

##Startup http
```bash
sudo lsof -t -i tcp:80 -s tcp:listen | sudo xargs kill;\
alias cls=clear;\
alias py=python3.10;\
source venv/bin/activate;\
uvicorn server.api:app --host 0.0.0.0 --port 80 --workers 4
```