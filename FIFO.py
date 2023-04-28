queue = []
arrival_time=[]
burst_time=[]
Turnaround_time=[]
waiting_time=[]
Total_Turnaround_time=0
Total_waiting_time=0
completion_time=[]

#user will tell the prcessor
n=int(input("Enter number of Proccesor :"))

#Loop so we can apped the value of arrival and burst time
for i in range (n):
    arrival_time.append(int(input("Enter your arrival time :{}".format(i+1))))
    burst_time.append(int(input("Enter your burst time :{}".format(i+1))))
    queue.append(i)

#now main part turaroundtime,waiting time,completiontime

for i in range (n):
    Process_id=queue[i]
    if (i==0):
        completion_time.append(arrival_time[Process_id]+burst_time[Process_id])
    else:
        completion_time.append(completion_time[i-1]+burst_time[Process_id])
    Turnaround_time.append(completion_time[i]-arrival_time[Process_id])
    waiting_time.append(Turnaround_time[i]-burst_time[Process_id])
    Total_Turnaround_time += Turnaround_time[i]
    Total_waiting_time += waiting_time[i]



#printing part
print("Process \t Arrivalt \t Burst \t Waiting time \t Turnaround")
for i in range(n):
    print("{} \t \t \t {} \t \t \t {} \t \t \t {} \t \t \t {}".format(queue[i]+1,arrival_time[i],burst_time[i],waiting_time[i],Turnaround_time[i]))
print("Total turn Around time : {}".format(Total_Turnaround_time))
print("Total waiting time : {}".format(Total_waiting_time))
