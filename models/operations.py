
def iterate_dictionary():
    users = dict({
        "Prince": "1234",
        "Mercy": "2345",
        "Clinton": "3456"
    })
    for key in users:
        print(key+" : "+users[key])
    return users

def check(name, password):
    new_users = iterate_dictionary()

    exists = name in new_users.keys()

    print("User exists?: "+ str(exists))
    if exists == True:
        print("Username and Password match?: "+str(password == new_users[name] ))
