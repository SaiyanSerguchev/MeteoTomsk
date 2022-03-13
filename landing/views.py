from django.http import HttpResponseRedirect
from django.shortcuts import render
import linecache
import csv
import linecache
import pathlib
import pandas as pd
from matplotlib import pyplot
import matplotlib.dates as mdates
import datetime as dt

def landing(request):
    return render(request, 'landing/../static/landing.html', locals())


def news(request):
    return render(request, 'landing/../static/news.html', locals())


def contacts(request):
    return render(request, 'landing/../static/contacts.html', locals())


def aboutus(request):
    return render(request, 'landing/../static/aboutus.html', locals())


def graph(request):
    return render(request, 'landing/../static/graph.html', locals())


def diagram(request):
    return render(request, 'landing/../static/diagram.html', locals())


def temprequest(request):
    date=request.GET["date"]
    coory=request.GET["coory"]
    coorx=request.GET["coorx"]
    d = date.split(".")
    tempn=re_ad(coorx, coory, date)
    data = {"temp" : tempn}
    return render(request, "static/landing.html", context=data)
    # return HttpResponseRedirect("/")


def re_ad(x, y, d):
    data = "C:\\Users\\Сайан\\Desktop\\dm\\Temp\\"
    text = data + d + '.txt'
    line = linecache.getline(text, int(y))
    line.split(" ")
    line = line[0:]
    line = line.split()
    line = line[0:]
    Tempn = line[int(x) - 1]
    return Tempn


def graphiki(request):
    date = request.GET["date"]
    date1 = request.GET["date1"]
    coory = request.GET["coory"]
    coorx = request.GET["coorx"]
    d = date.split(".")
    graphik(coorx, coory, date,date1)
    return HttpResponseRedirect("diagram/")


def dmmaker():
    series = pd.read_csv('C:\\Users\\Сайан\\Desktop\\dm\\Temp\\dm.csv',
                         sep=',', encoding='latin1',
                         parse_dates=['datetime'], dayfirst=True,
                         index_col='datetime')
    series = series.astype(float)
    data = series.plot()

    '''ax = pyplot.axes()'''

    pyplot.grid(True)
    pyplot.title('Температура за заданный промежуток')
    pyplot.xlabel('Год')
    pyplot.ylabel('Градусы в C™')
    pyplot.savefig('C:\\Users\\Сайан\\PycharmProjects\\geo\\static\\img\\pic_dmm.png')

def read(num, x, y, fd):
    data = ["datetime,Temp".split(",")]
    l = 1
    for i in range(num):
        ssilk="C:\\Users\\Сайан\\Desktop\\dm\\Temp\\"
        if(int(fd[2])<9):
            fd[2] = '0'+str(l)
        else:
            fd[2] =str(l)
        text = ssilk + '-'.join(fd) + '.txt'
        line = linecache.getline(text, int(x))
        line.split(" ")
        line = line[0:]
        line = line.split()
        line = line[0:]
        Tempn = line[int(y) - 1]
        value = ['/'.join(fd), Tempn]
        data.append(value)
        l += 1
    return data


def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def graphik(x,y,firstdate,lastdate):
    fd = firstdate.split("-")
    ld = lastdate.split("-")
    n = abs(int(fd[2]) - int(ld[2]))
    data = read(n + 1, x, y, fd)
    path = "C:\\Users\\Сайан\\Desktop\\dm\\Temp\\dm.csv"
    csv_writer(data, path)
    dmmaker()


def example(request):
    return render(request, 'landing/../static/example.html', locals())