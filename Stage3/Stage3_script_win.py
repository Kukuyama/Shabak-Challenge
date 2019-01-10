pid_list = []
known_attackers = open('Known_attackers.txt','a')

def create_log_files():
    global pid_list
    f = open('log.csv','r')
    ip_list = f.readlines()
    a = open('hint.txt','r')
    hints = a.readlines()
    for i in hints:
        pids = i.split('\r\n')
        pid_list.append(pids[0])
    for pid in pid_list:
        new_file = open(str(pid)+'.txt','a')
        for ip in ip_list:
            split = ip.split(',')
            if split[0] == str(pid):
                new_file.write(str(split)+'\n')

def most_common_ip(log_file):
    global success
    f = open(log_file,'r')
    parse = f.readlines()
    ips_list = []
    already_checked = []
    ip_count = []
    sum_of_ip = []
    for i in parse:
        ips = i.split(',')
        ips_list.append(ips[1])
    for i in ips_list:
        sum = ips_list.count(i)
        if i in already_checked:
            pass
        else:
            already_checked.append(i)
            b = [i,sum]
            ip_count.append(b)
            sum_of_ip.append(sum)

    maxi_sum = 0
    maxi_ip = ''
    for i in range(0,len(already_checked)):
        if sum_of_ip[i] > maxi_sum:
            maxi_sum = sum_of_ip[i]
            maxi_ip = already_checked[i]
        else:
            pass
    known_attackers.write('IP: '+maxi_ip+'\nTotal count: '+str(maxi_sum)+'\n')

create_log_files()
for filename in pid_list:
    most_common_ip(filename+'.txt')

