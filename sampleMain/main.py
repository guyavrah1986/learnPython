import paramiko


def sshTest2():
    ip = '172.30.82.111'
    port = 22
    username = 'admin'
    password = 'admin1'
    #cmd = 'cd /config \n rm -rf device.conf* \n ls \n '
    cmd = "lsh \n run show system status \n"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    outlines = stdout.readlines()
    resp = ''.join(outlines)

    #print("after deleting all configuration files from ACTIVE MCP, the /config folder has:")
    #print("-------------------------------------------------------------------------------")
    print(resp)


def main():
    print("main - start")
    sshTest2()

    print("main - end")
if __name__ == "__main__":
    main()
