task=[]
n=int(input("Enter the number of tasks you want to add:"))
for i in range(0,n):
    enter_task=input("Enter task:")
    task.append(enter_task)
    print("Task added!!!")
def update_task():
    print("\n1.Replace Task\n2.Mark Task as Done")
    choice=int(input("Which operation do you need to perform?"))
    if(choice==1):
               upd_task=input("Enter task to be updated:")
               pos=int(input("Enter the task position to update:"))
               task[pos]=upd_task
               print("Successfully updated")
    elif(choice==2):
        ctask=int(input("Enter the task position to mark as done:"))
        t=input("Enter task to be marked as done")
        if 0<=ctask<=len(task):
            task[ctask]=(t+"-Done")
            print("Task marked as done")
    else:
        print("Invalid choice!!!")
def remove_task():
    rem_task=input("Enter task  to be removed:")
    if rem_task in task:
        task.remove(rem_task)
        print("Task removed!!!")
    else:
        print("Task doesn't exist!!!")
def track_task():
    print(*task,sep='\n')
while(True):
    print("\nMain Menu\n1.update Task\n2.remove Task\n3.Track Tasks\n4.Exit")
    ch=int(input("Enter your choice:")) 
    if ch==1:
        update_task()
    elif ch==2:
        remove_task()
    elif ch==3:
        track_task()
    elif ch==4:
        break
    else:
        print("Invalid choice!!!Try Again.....")
    
          
    
    
    
