# Self-Notify Dynamic IP

A script that checks the current WAN IP and send myself an email when it's different from the previous one.

* This idea is from this [reddit comment](https://www.reddit.com/r/HomeNetworking/comments/ahdw4f/how_can_i_find_my_home_ip_address_remotely/eedpcx2/).
* [Getting external IP address in Python](https://stackoverflow.com/questions/2311510/)

## Setup

```sh
cd /path/to/self-notify-dynamic-ip
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Cron Job

```sh
# Edit cron.sh to cd to /path/to/your/self-notify-dynamic-ip
chmod +x cron.sh
# Add /path/to/your/self-notify-dynamic-ip/cron.sh to your crontab, e.g.:
crontab -l | { cat; echo "0 * * * * /path/to/your/self-notify-dynamic-ip/cron.sh"; } | crontab -
```
