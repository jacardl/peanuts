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
import datetime
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Mem tracking"
time = 1.0/2.2
time =  "{:.2%}".format(time)
print time
ws.cell(row=2, column=2).value = time

# save the file
wb.save('new_big_file.xlsx')
