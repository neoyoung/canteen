#A samll canteen demo

Deploy on freebsd
------------------
Here we will use Nginx+Gunicorn+Supervisord to deploy our canteen demo.If you are not fimiliar with some of these,
it's maybe necessary for you to do some google , and read the wiki or tuts.

Note that this tut is based on freebsd.You may need to find other tuts to deploy it.

- prepare database

```mysql
CREATE DATABASE canteen CHARACTER SET utf8;
CREATE USER 'canteen'@'localhost' IDENTIFIED BY 'canteen';
GRANT ALL ON canteen.* TO 'canteen'@'localhost';
```  

- prepare the virtual env

   install virtualenvwrapper

   ```shell
   cd /usr/ports/devel/py-virtualenv
   make install clean
   # And virtualenvwrapper..
   cd /usr/ports/devel/py-virtualenvwrapper
   make install clean
   ```

   After installation, make sure you have the following in your shell config file (~/.bashrc if your using Bash, ~/.zshrc if your using ZSH):
   ```shell
      # Virtualenvwrapper
      if [ -e /usr/local/bin/virtualenvwrapper.sh ]; then
          export WORKON_HOME=$HOME/.virtualenvs
          source /usr/local/bin/virtualenvwrapper.sh
      fi
   ```

   Next time you will login with this user, you will see a message that the ~/.virtualenvs directory is created and the scripts are placed there.

   We will install our Django project in the ~/codeRep/ directory. Let’s start by pulling our django project.
   ```shell
   cd ~/codeRep
   mkvirtualenv --no-site-packages demoproject
   git clone https://github.com/zhkzyth/canteen.git
   ```

   This will install a virtual environment in ~/.virtualenvs/demoproject and clone our project with git into the ~/apps/demoproject directory.

- install the python eggs

   ```shell
   cd ~/codeRep/canteen
   pip install -r requirments.rt
   ```

- edit your /etc/hosts 

   add the `127.0.0.1 canteen.com`

- [Nginx](http://wiki.nginx.org/Main)

   * suppose your have such structures:

   ```
      /usr/local/etc/nginx/ 
         |-nginx.conf
         |-site-enabled/
            |- *.conf
   ```

   * add below sentence to your `/etc/nginx.conf` or `/usr/local/etc/nginx/nginx.conf`:
         `include /usr/local/etc/nginx/site-enabled/*`

   * copy the `canteen-nginx-product.conf` in `cantenn/conf/`.

   * modify it to suite your need.

- [Gunicorn](http://docs.gunicorn.org/en/0.17.4/)

    Gunicorn s a communicator between our app and web server like nginx,since our app cannot read input from web server directly,
    so we need it.And you can replace it with diff tools like uwsgi/fastcgi/... and so on.
    
    You need to do serveral things:
    
    * make understand of the configuration file in `canteen/conf/gunicorn-dev.conf`
    * edit the path in it to suite your need.

- [Supervisord](http://supervisord.org/)

    Supervisord is a greate tool to manage diff applications which run in dameon mode.we use it to manage our gunicorn 
    porcess,so we don't need to run the `kill -9 xxx` cmd to restart the gunicorn.
    
    * suppose your have such structures(if not,please make one):
    
    ```
     /usr/local/etc/
     |- supervisord.conf
      - supervisord.conf.d/
    ```

    * copy the `supervisord.conf` in `canteen/conf/supervisord-freebsd.conf` to `/etc/supervisord.conf`,
      edit it to correct the path of your sys.
      
    * copy the `canteen-product.supervisord` to `/etc/supervisord.conf.d/canteen-product.supervisord`.
     And again,edit it to suite your need.
     
    * run the `supervisord` at our app root, you may see the `gunicorn:main-0 Runing` message.And now ,go check `http://cantten.com`


Additional Notes
-----------------
Sorry for the poor deploy notes.You may need to read more articles to understand those things to konw how.

- [Solid FreeBSD Server: the Foundation](http://www.wunki.org/posts/2011-04-05-solid-freebsd-server-foundation.html)
- [A Django setup using Nginx and Gunicorn](http://senko.net/en/django-nginx-gunicorn/)
- [Google nginx+gunicorn+supervisord](https://www.google.com.hk/search?q=django+gunicorn+nginx+supervisor)
