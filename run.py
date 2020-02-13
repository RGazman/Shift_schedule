#Shift schedule
import csv
import random

def Open_file():
    i = 0
    Emp_name = ['Nobody']                                                                   #List of employee 
    EmployeeName = open("EmployeeName.txt", "r",encoding="utf-8")                          #Open file with name (First & Last name)
    for Employee in EmployeeName:
        i +=1       
        print(str(i)+ ". " + str(Employee).strip('\n'))                                     #List of employee
        Emp_name.append(str(Employee).strip('\n'))
        Max_emp = Last_emp = i

    print ("Max employees = " + str(Max_emp))
    EmployeeName.close()
    return Emp_name, Last_emp


def Sort_noRule(Emp_name):   
    msg = "Enter the employee number, with a space, not covered by the rules - "            
    id_emp = list(map(str,input(msg).strip().split()))                                      #ID of the employee for whom the rules do not apply
    N_rule = []                                                                             #List of employee for whom the rules do not apply
    i = 0
    print ("You choose: ")
    for i in id_emp:        
        N_rule.append(Emp_name[int(i)])
        print (Emp_name[int(i)])
    return N_rule, id_emp


def Result_nRule(N_rule): 
    Period = ['8-17','9-18','10-19','11-20']
    i = 1
    for P in Period:
        print(str(i)+ ". " + str(P).strip('\n'))
        i +=1
    msg = "What is the period for the selected (1-4) employee? "
    Number_per = int(input(msg))
    print (Period[Number_per-1])
    result_nrule_schedule = dict.fromkeys(N_rule,Period[Number_per-1])
    print ("You choose: %s" %result_nrule_schedule)
    return result_nrule_schedule, Period
    
def Time_Dist_Emp(Period, id_emp, Last_emp):
    j = 1
    Time_dist_emp = {}
    for time in Period:  
        print ("Last employees - " + str(Last_emp-len(id_emp)))          
        print(str(j)+ ". " + str(time).strip('\n'))
        Time_dist_emp[str(time)] = value_emp = input("Enter the count of employees - ")    #A dictionary in which a pair "period and count of employees"
        j +=1 
        Last_emp -= int(value_emp)                                                          #Employee balance       
    print ("Your choose:")
    print (Time_dist_emp)
    return Time_dist_emp

    
def Emp_name_pop(Emp_name, N_rule):
    Emp_name.pop(0)
    for item in Emp_name:
        for item2 in N_rule:
            if item == item2:
                Emp_name.pop(Emp_name.index(item))
            else:
                pass
    return Emp_name

    #print ("DEBUG-1")
    

def Main_fun(result_nrule_schedule, Time_dist_emp, Emp_name):
    #Time_dist_emp = {'8-17': '4', '9-18': '4', '10-19': '2', '11-20': '2'}
    #Period = ['8-17','9-18','10-19','11-20']
    Week = ['Name/Days','Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    
    #Emp_name = ['Employee 1','Employee 2','Employee 3','Employee 4','Employee 5','Employee 6','Employee 7','Employee 8','Employee 9','Employee 10','Employee 11','Employee 12']
    with open('Schedule.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer2 = csv.writer(csvfile, delimiter=";")
        writer2.writerows([Week])
      
        for key, value in result_nrule_schedule.items():
            #                 Name +  Mon  +  Tue  +  Wed  +  Thu  +  Fri
            writer2.writerow ([key]+[value]+[value]+[value]+[value]+[value])

        time_8 = []
        time_9 = []
        time_10 = []
        time_11 = []

        Final_table = {'8-17':time_8,'9-18':time_9,'10-19':time_10,'11-20':time_11}

        for key1, value in Time_dist_emp.items(): 
            for k in range(0,int(value),1):
                #print (k, ' - ', key1, ' - ', value) 
                #print ('emp_name_: ',len(Emp_name))
                rnd_len = random.randint(0, len(Emp_name)-1)
                if k == len(Emp_name):
                    rnd_emp = Emp_name.pop(rnd_len)
                    if key1 == '8-17': time_8.append(rnd_emp); Final_table[key1] = time_8
                    if key1 == '9-18': time_9.append(rnd_emp); Final_table[key1] = time_9
                    if key1 == '10-19': time_10.append(rnd_emp); Final_table[key1] = time_10
                    if key1 == '11-20': time_11.append(rnd_emp); Final_table[key1] = time_11 
                    #Final_table.update([key1, Emp_name.pop(rnd_len)])
                    #Final_table[key1] = Emp_name.pop(rnd_len)
                    #print ('rnd_len: ',str(rnd_len), ' - len: ', len(Emp_name), ' - key1: ', key1, ' - rnd_emp: ',rnd_emp, ' - Final : ', Final_table)
                else:
                    rnd_emp = Emp_name.pop(rnd_len)                       
                    if key1 == '8-17': time_8.append(rnd_emp); Final_table[key1] = time_8
                    if key1 == '9-18': time_9.append(rnd_emp); Final_table[key1] = time_9
                    if key1 == '10-19': time_10.append(rnd_emp); Final_table[key1] = time_10
                    if key1 == '11-20': time_11.append(rnd_emp); Final_table[key1] = time_11   
                    #print ('rnd_len: ',str(rnd_len), ' - len: ', len(Emp_name), ' - key1: ', key1, ' - rnd_emp: ',rnd_emp)

        #print ('Emp_name: ', Emp_name)
        #print ('Final : ', Final_table)
        
        for key, value in Final_table.items():
            for val in range(0,len(value)):
                #                    Name   +   Mon + Tue + Wed + Thu + Fri
                writer2.writerow ([value[val]]+[key]+[key]+[key]+[key]+[key])
    csvfile.close()

if __name__ == "__main__":
    Emp_name, Last_emp = Open_file()
    N_rule, id_emp = Sort_noRule(Emp_name)
    result_nrule_schedule, Period = Result_nRule(N_rule)
    Time_dist_emp = Time_Dist_Emp(Period, id_emp, Last_emp)
    Emp_name = Emp_name_pop(Emp_name, N_rule)
    Main_fun(result_nrule_schedule, Time_dist_emp, Emp_name)