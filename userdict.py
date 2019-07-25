#%%
userdict={'admin':'1234','avig':'1234','rishabh':'9999','rohan':'888'}
user=open('username.txt','w+')
password=open('password.txt','w+')
user.writelines(['admin\n','avig\n','rishabh\n','rohan\n'])
password.writelines(['1234\n','1234\n','9999\n','888\n'])

#%%
def create_userdict():
    global userdict
    userdict={}
    user=open('usernames.txt')
    password=open('passwords.txt')
    userlist=user.readlines()
    passlist=password.readlines()
    print(userlist,passlist)
    for i in range(len(userlist)):
       userlist[i]=userlist[i][:len(userlist[i])-1]
       passlist[i]=passlist[i][:len(passlist[i])-1]
    print(userlist,passlist)
    user.close()
    password.close()
    userdict={userlist[i]:passlist[i] for i in range(len(userlist))}
create_userdict()
print(userdict)    