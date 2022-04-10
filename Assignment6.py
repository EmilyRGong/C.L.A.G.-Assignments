about_me = {'name': 'Emily', 'age': '21', 'hobby': 'art', 'favourite_food': 'blackberries'}

for key, value in about_me.items():
    print('Key: ' + key)
    print('Value: ' + value)

print('My name is' + ' ' + f"{about_me['name']}" + "." + " " + "I am" + " " + f"{about_me['age']}" + " " + "years old, and my favourite food is" + " " + f"{about_me['favourite_food']}" + "!!!")

about_me['favourite_colour'] = 'purple'  #Add dictionary data
about_me.pop('hobby') #Delete dictionary data
about_me_new = {'age': '22'} #Update dictionary data
about_me.update(about_me_new)
about_me.clear() #Clear dictionary data

print(about_me)
