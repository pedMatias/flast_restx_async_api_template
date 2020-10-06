# flast_restx_async_api_template

To set up the environment, set the the "Environment" var as "LOCAL" or
 "PRODUCTION". 
 
 TODO:
- queues;
- workers;
- pririties;

Create virtual env:
```sh
python3 -m venv <virtual env name>
```

Activate virtual env:
```sh
source <path dir virtual env>/bin/activate
```

Download the repo:
```sh
git clone <https url>;
```

Install requirements:
```sh
pip install -r requirements;
```

Then, create symbolic links to the nginx and supervisor configuration files in this repository:

```sh
$ ln -s /opt/aptoide/app_whitelister/conf/production/etc/supervisor/app_whitelister_api.conf /etc/supervisor/conf.d/app_whitelister_supervisord.conf
$ ln -s /opt/aptoide/app_whitelister/conf/production/etc/nginx/app_whitelister_api.conf /etc/nginx/conf.d/app_whitelister_nginx.conf
```

Lastly, before starting the app whitelister, create the directory used for logging purposes:

```sh
$ mkdir /var/log/supervisor/app_whitelister
```

Then, add the configuration file to supervisord and update it:

```sh
$ supervisorctl reread
$ supervisorctl update
```

The process group can be started with:

```sh
$ supervisorctl start whitelister:
```

