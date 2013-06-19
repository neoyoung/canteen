#A samll canteen demo

Deploy on freebsd
------------------
Here we will use Nginx+Gunicorn+Supervisord to deploy our canteen demo.If you are not fimiliar with some of these,
it's maybe necessary for you to do some google , and read the wiki or tuts.

Note that this tut is based on freebsd.You may need to find other tuts to deploy it.

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
     /etc/
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
