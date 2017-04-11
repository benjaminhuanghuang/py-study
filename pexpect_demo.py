# https://www.ibm.com/developerworks/cn/linux/l-cn-pexpect2/


import pexpect

def ssh_command(user, host, password, command):

    ssh_newkey = 'Are you sure you want to continue connecting'
    child = pexpect.spawn('ssh %s -l %s %s' % (host, user, command))
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
    if i == 0:  # Timeout
        print('SSH login timeout...')
        print(child.before, child.after)
        return None
    if i == 1:  # SSH has your the public key. Just accept it.
        child.sendline('yes')
        child.expect('password: ')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0:  # Timeout
            print('SSH could not login. Here is what SSH said:')
            print(child.before, child.after)
            return None
    else:
        child.sendline(password)
        return child


try:
    host = "192.168.11.115"
    user = 'hhuang'
    password = 'hhuang'
    command = "ls -l /usr/bin"
    # command = "touch /tmp/aaa.ben"
    child = ssh_command(user, host, password, command)
    child.expect(pexpect.EOF)

    print child.before

except Exception, e:
    print "-----", str(e)
