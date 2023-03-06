import MySQLdb
from django.contrib import messages
from django.shortcuts import render
from pymysql import Connect


conn = Connect(host="localhost", port=3306, user="root", password="wlm181704", database="test1", charset="utf8")

def search_by_word(request):
    username = request.POST.get('word')
    # cur = conn.cursor()
    # cur.execute("""SELECT distinct user_id,URL FROM log1 where word = %s """,word)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset="utf8")
    with conn.cursor(cursor=MySQLdb.cursors.DictCursor) as cursor:
        # cur = conn.cursor()
        # cursor.execute("""SELECT username,passwd,telephone,email FROM  user  """)
        cursor.execute("""SELECT distinct * FROM apply where name = %s """, [username])
        data = cursor.fetchall()
        print("查询信息为:",data)

        str2 = ""
        str3 = ""
        if len(data) == 0:
            messages.error(request, "没有该用户姓名")
            return render(request, "search_by_word.html")
        else:
            return render(request, "search_result1.html", {'data': data})

# for i in data:
#    print(i[0])
#   # a.append(str1)
#    str1=str(i[0])
#    str2+=str1
#    print(str2)
# return render(request,"search_result1.html",{"msg":str2,"word1":word,"url":i[1]})
