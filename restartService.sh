systemctl stop testaerospike.service
systemctl disable testaerospike.service
systemctl daemon-reload
systemctl enable testaerospike.service
systemctl start testaerospike.service
systemctl status testaerospike.service