from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pymysql import Connect
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
import MySQLdb

conn = Connect(host="localhost", port=3306, user="root", password="wlm181704", database="test1", charset="utf8")


# def a(request):
#     data = pd.read_sql("select 查询词, count(用户ID) 访问次数 from sheet1 "
#                        "group by 查询词 "
#                        "order by 访问次数 desc "
#                        "limit 10", conn)
#     # print(data)
#     x = list(data['查询词'])
#     y = list(data['访问次数'])
#     # print(y)
#     conn.close()  # 关闭
#     bar = Bar()
#     # 一般添加
#     bar.add_xaxis(xaxis_data=x, )
#     bar.add_yaxis(y_axis=y, series_name="人数", )
#     bar.set_global_opts(title_opts=opts.TitleOpts(title='柱状图', subtitle='访问次数'))
#     # bar.add("", x, y, is_datazoom_show=True, xaxis_rotate=30)
#     # page = Page(layout=Page.SimplePageLayout)
#     # page.add(bar)
#     return HttpResponse(bar.render_embed())


def bs(request):
    return render(request, "bs.html")


# def index(request):
#     return render(request,"index.html")


def page(request):
    return render(request, "page.html")


def register(request):
    return render(request, "register.html")


def add(request):
    return render(request, "add.html")


def login(request):
    return render(request, "login.html")


# def search(request):
#     return render(request, "search_by_userid.html")


def search1(request):
    return render(request, "search_by_word.html")



def anniversary_news(request):
    return render(request, "anniversary_news.html")


def login1(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print("登录姓名为:", username)
    cur = conn.cursor()
    cur.execute(
        """update current,user set current.username = user.username,current.passwd=user.passwd,current.telephone=user.telephone,current.email=user.email where user.username=%s""",
        (username))
    # cur.execute("""update current set current .username=username and current .passwd=password """)
    # cur.execute("""update current set current.passwd=current.passwd+1 """)
    a1 = cur.fetchall()
    conn.commit()

    cur.execute("""SELECT * FROM user where username = %s and passwd = %s""", (username, password))
    a = cur.fetchall()
    print("登录信息为:", a)
    if len(a) == 1:
        return render(request, "index.html")
    if len(a) == 0:
        messages.error(request, "输入错误！，请重新输入")
        return render(request, "login.html")


def register1(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM user where username = %s and passwd = %s """, (username, password))

    a = cur.fetchall()
    print(len(a))
    print(a)
    if len(a) == 1:
        messages.error(request, "该用户已注册，请重新输入")
        return render(request, "register.html")

    else:
        cur.execute("""insert into user(username,passwd,telephone,email) values(%s, %s,%s,%s)""",
                    (username, password, phone, email))
        conn.commit()
        messages.error(request, "注册成功！")
        return render(request, "login.html")


def order(request):
    t1 = request.POST.get('t1')
    xy = request.POST.get('xy')
    cc = request.POST.get('cc')
    zy = request.POST.get('zy')
    t2 = request.POST.get('t2')
    num = request.POST.get('num')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM yuyue where num = %s """, (num))

    a = cur.fetchall()
    if len(a) == 1:
        messages.error(request, "该用户已预约，请重新输入")
        return render(request, "bs.html")

    else:
        cur.execute("""insert into yuyue(t1,xy,cc,zy,t2,num) values(%s, %s,%s,%s,%s,%s)""",
                    (t1, xy, cc, zy, t2, num))
        conn.commit()

        cur.execute("""SELECT * FROM yuyue where zy = %s """, (zy))
        a1 = cur.fetchall()

        print("=====================================")
        print("======", a1)

        if len(a1) != 1:
            print("++++++++++++++++++++++++++++++++++++++++++")
            cur.execute("""update total set total.total=total.total+1 where zy=%s""", (zy))

            print("测试结果:", zy)
            conn.commit()
        else:
            total = 1
            cur.execute("""insert into total(zy,total) values(%s, %s)""",
                        (zy, total))
            conn.commit()

        messages.error(request, "预约成功！")
        return render(request, "page.html")


def apply(request):
    active = request.GET.get("active")
    return render(request, 'apply.html', {"active": active})


def dp_active(request):
    return render(request, 'dp_active.html')


def schedule(request):
    return render(request, 'schedule.html')


def reach(request):
    return render(request, 'reach.html')


def leave(request):
    return render(request, 'leave.html')


def apply1(request):
    name = request.POST.get('name')
    card = request.POST.get('card')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    college = request.POST.get('college')
    zy = request.POST.get('zy')
    active = request.POST.get('active')
    print("报名活动名称", active)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM apply where card = %s """, (card))

    a = cur.fetchall()
    print("+++++++++++", a)
    if len(a) == 1:
        messages.error(request, "你已报名该活动，请报名其它活动")
        return render(request, "dp_active.html")

    else:
        cur.execute("""insert into apply(name,card,phone,email,college,zy,active) values(%s, %s,%s,%s,%s,%s,%s)""",
                    (name, card, phone, email, college, zy, active))

        conn.commit()

        cur.execute("""SELECT * FROM apply where active = %s """, (active))
        a1 = cur.fetchall()

        print("=====================================")
        print("======", a1)

        if len(a1) != 1:
            print("++++++++++++++++++++++++++++++++++++++++++")
            cur.execute("""update active_apply set active_apply.total=active_apply.total+1 where active=%s""", (active))

            print("测试结果:", active)
            conn.commit()
        else:
            print("活动名称", active)

            total = 1
            cur.execute("""insert into active_apply(active,total) values(%s, %s)""",
                        (active, total))
            conn.commit()

        messages.error(request, "报名成功！")
        return render(request, "dp_active.html")


def reach1(request):
    name = request.POST.get('name')
    card = request.POST.get('card')
    phone = request.POST.get('phone')
    traffic = request.POST.get('traffic')
    boarding = request.POST.get('boarding')
    station = request.POST.get('station')
    time = request.POST.get('time')
    type1 = request.POST.get('type1')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM reach where card = %s """, (card))

    a = cur.fetchall()

    if len(a) == 1:
        messages.error(request, "你已填写该信息！！！")
        return render(request, "reach.html")

    else:
        cur.execute(
            """insert into reach(name,card,phone,traffic,boarding,station,time,type1) values(%s, %s,%s,%s,%s,%s,%s,%s)""",
            (name, card, phone, traffic, boarding, station, time, type1))

        conn.commit()
        messages.error(request, "填写信息成功！")
        return render(request, "schedule.html")


def leave1(request):
    name1 = request.POST.get('name1')
    card1 = request.POST.get('card1')
    phone1 = request.POST.get('phone1')
    traffic1 = request.POST.get('traffic1')
    boarding1 = request.POST.get('boarding1')
    station1 = request.POST.get('station1')
    time1 = request.POST.get('time1')
    type1 = request.POST.get('type1')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM leave1 where card1 = %s """, (card1))

    a = cur.fetchall()

    if len(a) == 1:
        messages.error(request, "你已填写该信息！！！")
        return render(request, "reach.html")

    else:
        cur.execute(
            """insert into leave1(name1,card1,phone1,traffic1,boarding1,station1,time1,type1) values(%s, %s,%s,%s,%s,%s,%s,%s)""",
            (name1, card1, phone1, traffic1, boarding1, station1, time1, type1))

        conn.commit()
        messages.error(request, "填写信息成功！")
        return render(request, "schedule.html")


def manager(request):
    return render(request, "manager.html")


def manager1(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM manager where username = %s and passwd = %s""", (username, password))
    a = cur.fetchall()
    if len(a) == 1:
        return show(request)
    if len(a) == 0:
        messages.error(request, "输入错误！，请重新输入")
        return render(request, "manager.html")


def show(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset="utf8")
    with conn.cursor(cursor=MySQLdb.cursors.DictCursor) as cursor:
        # cur = conn.cursor()
        cursor.execute("""SELECT username,passwd,telephone,email FROM  user  """)
        a = cursor.fetchall()
        return render(request, 'show.html', {'a': a})


def show1(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset="utf8")
    with conn.cursor(cursor=MySQLdb.cursors.DictCursor) as cursor:
        # cur = conn.cursor()
        cursor.execute("""SELECT username,passwd,telephone,email FROM  current  """)
        a = cursor.fetchall()
        return render(request, 'p_data.html', {'a': a})



def add1(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset="utf8")
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM user where username = %s and passwd = %s """, (username, password))

    a = cur.fetchall()
    if len(a) == 1:
        messages.error(request, "该用户已存在，请重新输入")
        return render(request, "add.html")

    else:
        cur.execute("""insert into user(username,passwd,telephone,email) values(%s, %s,%s,%s)""",
                    (username, password, phone, email))
        conn.commit()
        messages.error(request, "添加成功！")
        # return render(request, "page.html")
        return show(request)


def edit(request):
    if request.method == 'GET':
        username = request.GET.get("username")
        print("修改姓名", username)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset='utf8')
        with conn.cursor(cursor=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("""SELECT * FROM  user where username = %s""", [username])
            student = cursor.fetchall()
            print("===", student)
            return render(request, 'edit.html', {'student': student})
    else:
        username = request.POST.get("username")
        username1 = request.POST.get("username1", '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        print("修改时", username, password, phone, email)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset='utf8')
        with conn.cursor(cursor=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("""UPDATE user set username=%s,passwd=%s,telephone=%s,email=%s WHERE username =%s""",
                           [username1, password, phone, email, username])
            conn.commit()
            print("修改完成后", username, password, phone, email)
            return show(request)


def edit1(request):
    if request.method == 'GET':
        username = request.GET.get("username")
        print("修改姓名", username)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset='utf8')
        with conn.cursor(cursor=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("""SELECT * FROM  current where username = %s""", [username])
            student = cursor.fetchall()
            print("===", student)
            return render(request, 'edit1.html', {'student': student})
    else:
        username = request.POST.get("username")
        username1 = request.POST.get("username1", '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        print("修改时", username, password, phone, email)
        conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset='utf8')
        with conn.cursor(cursor=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("""UPDATE current set username=%s,passwd=%s,telephone=%s,email=%s WHERE username =%s""",
                           [username1, password, phone, email, username])
            cursor.execute("""UPDATE user set username=%s,passwd=%s,telephone=%s,email=%s WHERE username =%s""",
                           [username1, password, phone, email, username])
            conn.commit()
            print("修改完成后", username, password, phone, email)
            return show1(request)



def delete(request):
    username = request.GET.get("username")
    print("删除的用户为", username)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset='utf8')
    with conn.cursor(cursor=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM user WHERE username =%s", [username])
    conn.commit()
    return show(request)


def personal_data(request):
    return render(request,'personal_data.html')



def p_data(request):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="wlm181704", db="test1", charset="utf8")
    with conn.cursor(cursor=MySQLdb.cursors.DictCursor) as cursor:
        # cur = conn.cursor()
        cursor.execute("""SELECT username,passwd,telephone,email FROM  current  """)
        a = cursor.fetchall()
        return render(request, 'p_data.html', {'a': a})















