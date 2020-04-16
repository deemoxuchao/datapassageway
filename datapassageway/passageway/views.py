import json
import datetime

from django.shortcuts import render, HttpResponse
from django.db import connection

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from .models import ImportExport

import logging

logger = logging.getLogger('sql')


def get(request):
    if request.method == 'GET':
        sql = request.GET.get('sql', '')
        # print(sql)
        logger.info('sql:{}'.format(sql))
        if sql.startswith('select'):
            print('select')
            cursor = connection.cursor()
            cursor.execute(str(sql))
            raws = cursor.fetchall()
            result = []
            # 如果有查询结果
            if raws:
                col_name = [d[0] for d in cursor.description]
                result = [dict(zip(col_name, raw)) for raw in raws]
                print(type(result))
            print(cursor.rowcount)
            if len(result) != 0:
                print(result[0])
                cursor.close()
                # print('here')
                logger.info('sql:{},查询成功'.format(sql))
                return HttpResponse(result)
            else:
                cursor.close()
                logger.info('sql:{},查询失败'.format(sql))
                return HttpResponse('no data!')

        elif sql.startswith('update'):
            cursor = connection.cursor()
            cursor.execute(str(sql))
            print(cursor.rowcount)
            raws = cursor.fetchall()
            print(raws)
            rowcount = cursor.rowcount
            cursor.close()
            if cursor.rowcount:
                logger.info('sql:{},插入成功，影响{}行'.format(sql, rowcount))
                return HttpResponse('插入成功，影响{}行'.format(rowcount))
            else:
                logger.info('sql:{},插入失败'.format(sql))
                return HttpResponse('插入失败！')
        else:
            logger.info('sql:{},执行失败失败，只允许select和update！'.format(sql))
            return HttpResponse('只允许select和update！')


