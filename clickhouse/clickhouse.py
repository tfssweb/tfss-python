#! /usr/bin/env python
# -*- coding: utf-8 -*-

from clickhouse_driver import Client as CHClient

target = {'destination': '172.18.18.189', 'user': 'default', 'password': 'xxx', 'database': 'aqi_test'}


c = CHClient(target['destination'], user=target['user'], password=target['password'], database=target['database'])

fields_to_read = ("PointName", "PointClass", "ProvinceName", "CityName", "CountyName")

stmt = '''
            SELECT {}
            FROM ass.xxx
            WHERE PointID={}
            ORDER BY DataTime DESC 
            LIMIT 1;
        '''.format(', '.join(fields_to_read), 6625)

res = c.execute(stmt)

print(res)



