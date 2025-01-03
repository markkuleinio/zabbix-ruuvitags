# Zabbix monitoring for RuuviTags


## Prerequisites

- Raspberry Pi OS 12 (only tested with it)
- Zabbix Agent or Zabbix Agent 2 installed (username "zabbix" is used for running the app,
and `/run/zabbix` is used for saving the RuuviTag data)


## Install instructions

Replace "markku:markku" with your current unprivileged used name and group:

    sudo apt install bluez-hcidump
    sudo mkdir /opt/zabbix-ruuvitags
    sudo chown markku:markku /opt/zabbix-ruuvitags
    cd /opt/zabbix-ruuvitags
    git clone https://github.com/markkuleinio/zabbix-ruuvitags.git .
    python3 -m venv venv
    venv/bin/pip --no-cache-dir install -U pip wheel
    venv/bin/pip --no-cache-dir install ruuvitag-sensor
    echo "zabbix  ALL=(ALL)       NOPASSWD: /usr/bin/hciconfig,/usr/bin/hcitool,/usr/bin/hcidump" | sudo tee /etc/sudoers.d/ruuvitags
    sudo chmod 0440 /etc/sudoers.d/ruuvitags
    sudo cp ruuvitags.service /etc/systemd/system
    sudo systemctl daemon-reload
    sudo systemctl enable ruuvitags.service --now

- Import the template in Zabbix and add it to your Raspberry Pi host
- Modify the inherited `{$RUUVITAGS}` macro to contain your RuuviTag MAC addresses and names
(note that the macro value must be a valid JSON key-value object)


## Troubleshooting

    sudo systemctl status ruuvitags.service
    ls -l /run/zabbix
    tail -f /run/zabbix/ruuvitags.log
    sudo less /var/log/zabbix/zabbix_agentd.log
    sudo less /var/log/zabbix/zabbix_agent2.log

