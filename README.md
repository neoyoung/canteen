#A small canteen demo


Tech stack
-----------
- Front-end
 - Bootstrap
 - Simple OO
 - require JS
 - JQ(offcourse)

- Back-end
 - Django >=1.4
 - MYSQL

Feature
-------
- meal select
- order list
- foods and menu management

TODO
----
- food comment/Tag
- user interaction
- web chatroom
- game?? oh my =.=

INSTALL
-------
- prepare database

```mysql
CREATE DATABASE canteen CHARACTER SET utf8;
CREATE USER 'canteen'@'localhost' IDENTIFIED BY 'canteen';
GRANT ALL ON canteen.* TO 'canteen'@'localhost';
```  
- prepare the virtual env

```shell
cd path/to/project
virtual .
source bin/activate
```
- install the python eggs

```shell
cd path/to/project/
pip install -r requirments.rt
```
- run the code

```shell
cd path/to/prepare/canteen
./manager syncdb
./manager runserver
```
- now,go check the site at [locahost][3]

Additional Message
------------------
It's a demo based on serveral project,go check it if you want to know more.

- The [ecommerce][1], a good book for newbie to master django.
- A similar menu sys,called [canku][2] which based on nodejs.


[1]: http://www.amazon.com/Beginning-Django-E-Commerce-Experts-Development/dp/1430225351
[2]: https://github.com/willerce/aidingcan
[3]: http://localhost:8000
