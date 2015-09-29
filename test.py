# import pygal                                                       # First import pygal
# bar_chart = pygal.Line()                                            # Then create a bar graph object
# bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])  # Add some values
# bar_chart.render_to_png('bar_chart.png')

# from urllib import urlopen
# data = urlopen('http://peak.telecommunity.com/dist/ez_setup.py')
# with open('ez_setup.py', 'wb') as f:
#     f.write(data.read())

# import os
# file_name = 'ez_setup.py'
# from urllib import urlopen
# data = urlopen('http://peak.telecommunity.com/dist/ez_setup.py')
# with open(file_name, 'wb') as f:
#     f.write(data.read())
# os.system("D:\\Python\\\new peanuts\\24\\ez_setup.py")
import var
from collections import *
a = {'tx2gClear': ['50.9'], 'rx2gTkip': ['17.8', '17.6'], 'tx5gAes': ['92.8', '93.5', '93.5'],
     'rx2gAes': ['38.8', '40.7', '37.8'], 'tx5gTkip': ['26.2', '26.6'], 'rx2gClear': ['42.4'],
     'tx5gClear': ['93.6'], 'tx2gAes': ['47.7', '48.0', '47.8'],'rx5gTkip': ['20.9', '18.7'],
     'rx5gAes': ['47.0', '42.9', '66.7'], 'tx2gTkip':['26.8', '26.1'], 'rx5gClear': ['57.4']}

for key, value in a.iteritems():
    if len(value) is not 0:
        ave = float(reduce(lambda i, j: float(i)+float(j), value)) / len(value)
        print ave