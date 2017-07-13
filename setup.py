sudo apt-get -y install ruby
sudo apt-get -y install ruby-dev
sudo gem install fluentd -v "~> 0.12.0"
sudo gem install fluent-plugin-elasticsearch
sudo gem install fluent-plugin-grep
sudo gem install fluent-plugin-record-modifier
sudo gem install fluent-plugin-grok-parser
sudo apt-get -y install dnsmasq
sudo service dnsmasq restart
sudo update-rc.d dnsmasq defaults
sudo nohup fluentd -c fluentd.conf >/dev/null 2>&1 &

