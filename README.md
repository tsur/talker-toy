
# Talker toy

A Talker toy project based on raspberry pi zero. It makes your favourite toy, a talking toy. By using the exposed web interface on the pi, you may interact with the toy, making it to say whatever you want to.

# Set up

Connect the speakers to the pi, uploade this repo sources, run `scripts/setup.sh` and run the server `python run.py`

if do not know how to access your pi, connect it to your local network and to your pc or power source and discover hosts with ssh enabled

```bash
$> nmap -p 22 -sV 192.168.1.0/24
```

Then try with default login/passwd:

```bash
# Enter with default settings
ssh pi@<IP> # i.e. ssh pi@192.168.1.135
# Use raspberry as passwd
```

Once got access into your pi, download this gist to your pi

```bash
git clone https://github.com/tsur/talker-toy.git talker-toy && cd talker-toy
```

Give permissions to setup if neede and run the script to install dependencies:

```bash
chmod +x ./scripts/setup.sh
./scripts/setup.sh
```

After that open a screen session:

```bash
screen -S talker-toy
# use <C-a-d> to come back to main shell and then from main shell use screen -r garage_doors
# to kill, type exit within screen session
```

To run the tests:

```bash
chmod +x ./scripts/tests.sh
./scripts/tests.sh
```

Finally run the process:

```bash
sudo python run.py
```

Note: for connectivity issues, make sure file /etc/network/interfaces is working (i.e `ping google.com`, or if firewall does not accept pinging, then use `curl --silent --head https://google.com`)
