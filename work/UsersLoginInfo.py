#!/usr/bin/python3
#coding=utf-8

from common.MyRedisHelper import MyRedisHelper
from common.MysqlHelper import  MysqlHelper

class UsersLoginHelper():

    def get_user_client_login(self,mail_user, redis_ip, redis_port, redis_key):
        myredis = MyRedisHelper(redis_ip, redis_port)
        values = myredis.get(redis_key + mail_user)
        if values is not None:
            strvalues = str(values, 'utf-8')
            return int(strvalues)
        else:
            return None

    def get_user_webmail_login(sele,ip, port, dbname, dbuser, dbpassword, mailuser):
        mysqlhelper = MysqlHelper(ip, port, dbname, dbuser, dbpassword, charset='utf8')
        sql = "select login_time from USER_LOGIN_HISTORY where username='%s' order by login_time desc limit 1" % (mailuser)
        data_tuple = mysqlhelper.get_all(sql)
        if len(data_tuple) != 0:
            for data in data_tuple:
                return data
        else:
            return None
        mysqlhelper.close()