#!/usr/bin/python

import pexpect
import sys
import time

def send_command(child, cmd, host):
        fout = file('{0}.log'.format(host),'w')
        command = open(cmd,"r")
        child.logfile = fout
        for i in command.readlines():
                child.sendline(i)
		child.expect(':~#')
        fout.close()
        command.close()

def connect(user, host, password, enapass):
        ssh_newkey = "Are you sure you want to continue connecting"
        connStr = 'ssh ' + user + '@' + host
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
        if ret == 0 :
                print '[-] Error Connecting to ' + host
                return
        if ret == 1 :
                child.sendline('Yes')
                ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
                if ret == 0:
                        print '[-] Error Connecting to ' + host
                        return
        child.sendline(password)
        child.expect(':~#')
        return child

def main():
	ipList = "ip.txt"
	cmdList = "cmd.txt"
	if len(sys.argv) < 3:
		print "enter user name password"
		return
        user = sys.argv[1]
        password = sys.argv[2]
        IP = open(ipList,"r")
        for host in IP.readlines():
                host = host.strip("\n")
                print host
                child = connect(user,host,password,"1234")
                send_command(child,cmdList,host)

if  __name__ == '__main__':
        main()
