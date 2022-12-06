#10
d={'payton':'An interpreted, object-oriented programming language'}
d['python'] = d['payton']
del d['payton']
print(d)

name = ("Spider", "Man")
phone_number_dictionary = {name:489328493}
print(phone_number_dictionary)
print(phone_number_dictionary[name])
print(phone_number_dictionary[("Spider", "Man")])
