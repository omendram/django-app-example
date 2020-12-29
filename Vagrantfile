# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 8000, host: 8080, host_ip: "127.0.0.1"
  config.vm.synced_folder ".", "/home/vagrant/mUtomik"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "1024"
  end
  
  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.

  config.vm.provision "shell", inline: <<-SHELL
    apt-get -y upgrade python3
    echo " ========== python has been installed =========="
    apt-get -y install python3-pip
    echo " ========== pip has been installed =========="
    pip3 install -r mUtomik/requirements.txt
    echo "dependencies are installed"
    python3 mUtomik/manage.py makemigrations
    python3 mUtomik/manage.py migrate
    python3 mUtomik/manage.py runserver 0.0.0.0:8000 &
    echo "server has been started"
  SHELL
end
