
print("---TO DO LIST---")
print(''' 1.Add task 
 2.View task 
 3.Mark task as done 
 4.Exit ''' ) 
tasks=[] 
y="yes"
while y=="yes": 
    n=int(input("choose an option here :"))  
    if n==1: 
        z=input("enter the task :") 
        print("✅ task done")  
        tasks.append(z)
        y=input("do you want to continue here ?") 
        y=y.lower()
    elif n==2: 
        q=1
        if not tasks :
            print("no tasks availaible 😔")  
            y=input("do you want to continue here ?")
            y=y.lower()

        else :
            for i in tasks :
                print(q,i) 
                q+=1
            y=input("do you want to continue here ?")  
            y=y.lower()
    elif n==3: 
        t=1
        if not tasks :
            print("no tasks to mark as done ") 
        else : 
            for j in tasks :
                print(t,j) 
                t+=1 
        z=input("enter the task you want to mark as done :")
        tasks.remove(z)
        print("the task has been marked done ✅") 
    elif n==4 : 
        print("exited from the code come back 😊") 
    else : 
        print("invalid choice choose again broooo 😌") 
        y="yes"  
