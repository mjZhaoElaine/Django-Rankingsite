from django.db import connection
from .models import TimesRank, CWURank, SHJTRank, Univ2Country

def TimesDefault():
    with connection.cursor() as cursor:
        query = "SELECT * FROM ranking_timesrank WHERE rankyear = 2016"
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    return result

def CWUDefault():
    with connection.cursor() as cursor:
        query = "SELECT * FROM ranking_cwurank WHERE rankyear = 2015"
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    return result

def SHJTDefault():
    with connection.cursor() as cursor:
        query = "SELECT * FROM ranking_shjtrank WHERE rankyear = 2015"
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    return result

def TimesNormalSearch(university, fromyear, toyear, limit):
    with connection.cursor() as cursor:
        if (university == "" and fromyear == "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_timesrank WHERE rankyear = 2016"
            cursor.execute(query)
        elif (university != "" and fromyear == "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_timesrank WHERE UnivName = %s"
            param = [university]
            cursor.execute(query, param)
        elif (university == "" and fromyear != "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_timesrank WHERE rankyear = %s"
            param = [fromyear]
            cursor.execute(query, param)
        elif (university == "" and fromyear == "" and toyear == "" and limit != ""):
            query = "SELECT * FROM ranking_timesrank WHERE rankyear = 2016 LIMIT %s"
            param = [limit]
            cursor.execute(query, param)
        elif(university != "" and fromyear != "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_timesrank WHERE UnivName = %s AND rankyear = %s"
            param = [university, fromyear]
            cursor.execute(query, param)
        elif(university == "" and fromyear != "" and toyear == "" and limit != ""):
            query = "SELECT * FROM ranking_timesrank WHERE RankYear = %s LIMIT %s"
            param = [fromyear, limit]
            cursor.execute(query, param)
        elif(university != "" and fromyear != "" and toyear != "" and limit == ""):
            query = "SELECT * FROM ranking_timesrank WHERE UnivName = %s AND rankyear >= %s AND rankyear <= %s"
            param = [university, fromyear, toyear]
            cursor.execute(query, param)
        else:
            return None
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    return result

def CWUNormalSearch(university, fromyear, toyear, limit):
    with connection.cursor() as cursor:
        if (university == "" and fromyear == "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_cwurank WHERE rankyear = 2016"
            cursor.execute(query)
        elif (university != "" and fromyear == "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_cwurank WHERE UnivName = %s"
            param = [university]
            cursor.execute(query, param)
        elif (university == "" and fromyear != "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_cwurank WHERE rankyear = %s"
            param = [fromyear]
            cursor.execute(query, param)
        elif (university == "" and fromyear == "" and toyear == "" and limit != ""):
            query = "SELECT * FROM ranking_cwurank WHERE rankyear = 2016 LIMIT %s"
            param = [limit]
            cursor.execute(query, param)
        elif(university != "" and fromyear != "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_cwurank WHERE UnivName = %s AND rankyear = %s"
            param = [university, fromyear]
            cursor.execute(query, param)
        elif(university == "" and fromyear != "" and toyear == "" and limit != ""):
            query = "SELECT * FROM ranking_cwurank WHERE RankYear = %s LIMIT %s"
            param = [fromyear, limit]
            cursor.execute(query, param)
        elif(university != "" and fromyear != "" and toyear != "" and limit == ""):
            query = "SELECT * FROM ranking_cwurank WHERE UnivName = %s AND rankyear >= %s AND rankyear <= %s"
            param = [university, fromyear, toyear]
            cursor.execute(query, param)
        else:
            return None
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    return result

def SHJTNormalSearch(university, fromyear, toyear, limit):
    with connection.cursor() as cursor:
        if (university == "" and fromyear == "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_shjtrank WHERE rankyear = 2016"
            cursor.execute(query)
        elif (university != "" and fromyear == "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_shjtrank WHERE UnivName = %s"
            param = [university]
            cursor.execute(query, param)
        elif (university == "" and fromyear != "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_shjtrank WHERE rankyear = %s"
            param = [fromyear]
            cursor.execute(query, param)
        elif (university == "" and fromyear == "" and toyear == "" and limit != ""):
            query = "SELECT * FROM ranking_shjtrank WHERE rankyear = 2016 LIMIT %s"
            param = [limit]
            cursor.execute(query, param)
        elif(university != "" and fromyear != "" and toyear == "" and limit == ""):
            query = "SELECT * FROM ranking_shjtrank WHERE UnivName = %s AND rankyear = %s"
            param = [university, fromyear]
            cursor.execute(query, param)
        elif(university == "" and fromyear != "" and toyear == "" and limit != ""):
            query = "SELECT * FROM ranking_shjtrank WHERE RankYear = %s LIMIT %s"
            param = [fromyear, limit]
            cursor.execute(query, param)
        elif(university != "" and fromyear != "" and toyear != "" and limit == ""):
            query = "SELECT * FROM ranking_shjtrank WHERE UnivName = %s AND rankyear >= %s AND rankyear <= %s"
            param = [university, fromyear, toyear]
            cursor.execute(query, param)
        else:
            return None
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))
    return result
