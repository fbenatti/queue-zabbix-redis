# queue-zabbix-redis

## Install requirements.
 pip install redis protobix

 cd queue-zabbix-redis
 cp -rf scripts/ /etc/zabbix/
 cp -rf zabbix_agentd.conf.d/userparameter_redis_lld_queue.conf /etc/zabbix/zabbix_agentd.conf.d/
 
## Import  template.
 zbx_export_templates.xml
 
 
 - Example:
 <a href="https://ibb.co/b3VFBbr"><img src="https://i.ibb.co/wLq7WcK/fila-redis.png" alt="fila-redis" border="0"></a>
