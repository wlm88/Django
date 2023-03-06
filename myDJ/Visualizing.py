import random

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pymysql import Connect
import pandas as pd
from pyecharts.charts import Bar, Line, Page, Grid, WordCloud, Pie
from pyecharts import options as opts
import itertools
# conn = Connect(host="localhost", port=3306, user="root", password="", database="yjw", charset="utf8")
from django.contrib import messages
from django.shortcuts import render
from pymysql import Connect
from pyecharts.charts import Map
from pyecharts import options as opts

conn = Connect(host="localhost", port=3306, user="root", password="wlm181704", database="test1", charset="utf8")
# word = request.POST.get('word')

cur = conn.cursor()


# def bs(re)


def hour_sum(request):
    cur.execute("""SELECT * FROM  hour_sum  """)
    a = cur.fetchall()
    hour = []
    total = []
    for i in a:
        hour.append(i[0])
        total.append(i[1])
        print("++++++++++++++++", i[0])

    line = Line(init_opts=opts.InitOpts(width='100%')).set_global_opts(
        yaxis_opts=opts.AxisOpts(name="点击数", axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color="red"))),
        xaxis_opts=opts.AxisOpts(name="h", axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color="red"))),
        title_opts=opts.TitleOpts(title="各时段校庆管理系统网站点击量"), toolbox_opts=opts.ToolboxOpts(is_show=True,
                                                                                         feature=opts.ToolBoxFeatureOpts(
                                                                                             data_zoom=opts.ToolBoxFeatureDataZoomOpts(
                                                                                                 is_show=False))))
    line.add_xaxis(xaxis_data=hour)
    line.add_yaxis("点击量", y_axis=total, color="green")

    page = Page()
    page.add(line)
    return HttpResponse(page.render_embed())


# ***************************************************************************
def hour_people(request):
    cur.execute("""SELECT * FROM  hour_people  """)
    a = cur.fetchall()
    hour = []
    total = []
    for i in a:
        hour.append(i[0])
        total.append(i[1])
    cur.execute("""SELECT * FROM  hour_sum  """)
    a1 = cur.fetchall()

    total1 = []
    for i in a1:
        total1.append(i[1])
    line = Line(init_opts=opts.InitOpts(width='50%')).set_global_opts(
        yaxis_opts=opts.AxisOpts(name="人数", axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color="blue"))),
        xaxis_opts=opts.AxisOpts(name="h", axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color="blue"))),
        title_opts=opts.TitleOpts(title="各时段校庆管理系统网站访问人数"), toolbox_opts=opts.ToolboxOpts(is_show=True,
                                                                                          feature=opts.ToolBoxFeatureOpts(
                                                                                              data_zoom=opts.ToolBoxFeatureDataZoomOpts(
                                                                                                  is_show=False))))
    line.add_xaxis(xaxis_data=hour)
    line.add_yaxis("访问人数", y_axis=total, color="purple")
    bar = (
        Bar(init_opts=opts.InitOpts(width="50%"))
            .add_xaxis(hour)
            .add_yaxis("点击人数", y_axis=total, color="green")
            .add_yaxis("点击量", y_axis=total1, color="blue")
            .set_global_opts(title_opts=opts.TitleOpts(title="各时间段点击量与人数对比"),
                             yaxis_opts=opts.AxisOpts(name="个/次", axisline_opts=opts.AxisLineOpts(
                                 linestyle_opts=opts.LineStyleOpts(
                                     color="red"))), xaxis_opts=opts.AxisOpts(name="h"))
    )

    page = Page(layout=Page.SimplePageLayout)
    page.add(line, bar)
    return HttpResponse(page.render_embed())


# *************************************************
# def every_top(request):
#     cur.execute("""SELECT * FROM  every_url_sum  """)
#     a = cur.fetchall()
#     user1 = []
#     total = []
#     for i in a:
#         user1.append(i[0])
#         total.append(i[1])
#     bar = (
#         Bar(init_opts=opts.InitOpts(width="100%"))
#             .add_xaxis(user1)
#
#             .add_yaxis("访问url个数", y_axis=total, color="blue")
#             .set_global_opts(
#             title_opts=opts.TitleOpts(title="用户浏览不同网址个数排名", subtitle="一天中用户访问不同网站个数"),
#             yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
#             xaxis_opts=opts.AxisOpts(name="用户ID", axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
#                                      ))
#     )
#     page = Page(layout=Page.SimplePageLayout)
#     page.add(bar)
#     return HttpResponse(page.render_embed())


# ************************************************
def word_colund(request):
    cur.execute("""SELECT * FROM  total  """)
    a = cur.fetchall()
    word = []
    total = []
    for i in a:
        word.append(i[0])
        total.append(i[1])
    print("&&&&&&&&&&&&&&&&&&&", word, total)
    cloud = list(itertools.zip_longest(word, total))
    wordcount1 = WordCloud(init_opts=opts.InitOpts(width="50%")).set_global_opts(
        title_opts=opts.TitleOpts(title="前20专业返校预约词云图"))
    wordcount1.add("", cloud, shape="")
    return HttpResponse(wordcount1.render_embed())


# ************************************************
def word_apply(request):
    cur.execute("""SELECT * FROM  active_apply  """)
    a = cur.fetchall()
    active = []
    total = []

    for i in a:
        active.append(i[0])
        total.append(i[1])
    total1 = total[:10]
    active1=active[:10]
    print("total数:",total1)
    bar = (
        Bar(init_opts=opts.InitOpts(width="100%"))
            .add_xaxis(active1)

            .add_yaxis("各院系活动用户预约数", y_axis=total1, color="green")
            .set_global_opts(title_opts=opts.TitleOpts(title="同一院系活动的不同用户预约数", subtitle="前10的院系活动预约"),
                             yaxis_opts=opts.AxisOpts(
                                 splitline_opts=opts.SplitLineOpts(is_show=True), ),
                             xaxis_opts=opts.AxisOpts(name="活动预约专业", axislabel_opts={"rotate": 10},
                                                      axisline_opts=opts.AxisLineOpts(
                                                          linestyle_opts=opts.LineStyleOpts(
                                                              color="blue"))),
                             toolbox_opts=opts.ToolboxOpts(is_show=True, feature=opts.ToolBoxFeatureOpts(
                                 data_zoom=opts.ToolBoxFeatureDataZoomOpts(is_show=False))))
    )
    page = Page(layout=Page.SimplePageLayout)
    page.add(bar)
    return HttpResponse(page.render_embed())


# *********************************************
def word_top(request):
    cur.execute("""SELECT * FROM  active_apply  """)
    a = cur.fetchall()
    active = []
    total = []
    for i in a:
        active.append(i[0])
        total.append(i[1])
    total1 = total[:10]
    active1 = active[:10]

    # 饼图用的数据格式是[(key1,value1),(key2,value2)]，所以先使用 zip函数将二者进行组合
    data_pair = [list(z) for z in zip(active1, total1)]
    pie = (
        # 初始化配置项，内部可设置颜色
        Pie(init_opts=opts.InitOpts(width="50%"))
            .add(
            # 系列名称，即该饼图的名称
            series_name="院系活动预约频率占比分析",
            # 系列数据项，格式为[(key1,value1),(key2,value2)]
            data_pair=data_pair,
            # 通过半径区分数据大小 “radius” 和 “area” 两种
            rosetype="radius",
            # 饼图的半径，设置成默认百分比，相对于容器高宽中较小的一项的一半
            radius="55%",
            # 饼图的圆心，第一项是相对于容器的宽度，第二项是相对于容器的高度
            center=["50%", "50%"],
            # 标签配置项
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            # 全局设置
            .set_global_opts(
            # 设置标题
            title_opts=opts.TitleOpts(
                # 名字
                title="院系活动预约占比图",
                # 组件距离容器左侧的位置
                pos_left="center",
                # 组件距离容器上方的像素值
                pos_top="20",
                # 设置标题颜色
                title_textstyle_opts=opts.TextStyleOpts(color="black"),
            ),
            # 图例配置项，参数 是否显示图里组件
            legend_opts=opts.LegendOpts(is_show=False),
        )
            # 系列设置
            .set_series_opts(
            # tooltip_opts=opts.TooltipOpts(
            #     trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            # ),
            # 设置标签颜色
            label_opts=opts.LabelOpts(color="black"),
        )

    )
    page = Page()
    page.add(pie)
    return HttpResponse(page.render_embed())


# *********************************************
def shuju(request):
    cur.execute("""SELECT * FROM  sum  """)
    a = cur.fetchall()

    for i in a:
        total = int(i[0])
    cur.execute("""SELECT * FROM  sum_people  """)
    a1 = cur.fetchall()
    # 总人数
    for i in a1:
        total1 = int(i[0])
    cur.execute("""SELECT * FROM  sum_apply  """)
    a2 = cur.fetchall()
    # 总注册
    for i in a2:
        total2 = int(i[0])
    cur.execute("""SELECT * FROM  sum_register  """)
    a3 = cur.fetchall()

    for i in a3:
        total3 = int(i[0])
    avg_pv = total / total1  # 人均访问量

    return render(request, "shuju.html",
                  {"total": total, "total1": total1, "total2": total2, "total3": total3, "avg_pv": avg_pv})


def location(request):
    # locate = ['北京', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
    #           '湖南', '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '陕西', '甘肃', '青海', '宁夏', '新疆']
    cur.execute("""SELECT boarding FROM  reach  """)
    a = cur.fetchall()
    locate1 = []
    for i in a:
        locate1.append([i[0],0])

    print("抵达地点信息：", locate1)

    cur.execute("""SELECT boarding1 FROM  leave1  """)
    a1 = cur.fetchall()
    locate2 = []
    for i in a1:
        print("+++",i[0])
        # lst = [list(row) for row in i]
        # lst = list(map(list, i))
        locate2.append([i[0],0])

    def data_filling(array):
        '''
         作用：给数组数据填充随机数
        '''
        for i in array:
            i[1] = random.randint(1, 1000)
            print(i)

    data_filling(locate1)
    data_filling(locate2)

    def create_china_map():
        '''
         作用：生成中国地图
        '''
        (
            Map()
                .add(
                series_name="返校乘车地点",
                data_pair=locate1,
                maptype="china",
            )
                .add(
                series_name="离校乘车地点",
                data_pair=locate2,
                maptype="china",
            )
                # 设置标题
                .set_global_opts(title_opts=opts.TitleOpts(title="中国地图"))
                # 生成本地html文件
                .render('map1.html')
        )

    create_china_map()
    return render(request, 'map1.html')


