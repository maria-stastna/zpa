#6a
txt = "My hobby is {hobby}."
print(txt.format(hobby = 'drawing'))

#6b
date = '2018-11-01'
pieces = date.split('-')
year = pieces[0]
month = pieces[1]
day = pieces[2]
date2 = "{a}/{b}"
print(date2.format(a=day, b=month))
