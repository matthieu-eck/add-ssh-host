import os
#Item list you need in your config file
listf = ['host','hostname','port','IdentityFile','user','ForwardAgent']
#Questions the user will be asked
lista = ['hostname','FQDN or ip','port (22)','key','user (Ubuntu)','ForwardAgent (Yes)']
listb =[]#Answers

def multi_choice():
    global chosen
    global path
    path = (os.environ.get('HOME','/home/username/'))
    path=(path+'/.ssh/')
    files = os.listdir(path)
    for item in enumerate(files):
        print (("-%d- %s") % item)
    try:
        idx = int(input("Enter the file's number "))
    except ValueError:
        print ("You fail at typing numbers.")
    try:
        chosen = files[idx]
    except IndexError:
        print ("Try a number in range next time.")
    print (chosen)

for x in lista:
    if x == 'key':
            multi_choice()
            listb.append("%s%s" % (path,chosen))
    else:
        var = input("Please enter %s: " % (x))
        listb.append(var)

configfile = ("%sconfig" % (path))#Find the ssh config file
file = open(configfile, "a") #Append to the config file
f=0
for a,b in zip (listf,listb):
    file.write ("\n")
    if f == 0:
        file.write ("%s %s " % (a,b))
        f = (f + 1)
    else:
        file.write ("    %s %s " % (a,b))

file.close

