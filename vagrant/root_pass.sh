
# enable password authentication
sudo sed -i '/^PasswordAuthentication/ d' /etc/ssh/sshd_config
sudo echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# enable root login
sudo sed -i '/^PermitRootLogin/ d' /etc/ssh/sshd_config
sudo echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config

systemctl restart sshd

# set root password
echo "toor" | sudo passwd --stdin root
