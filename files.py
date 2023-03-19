#Files

hosts = open('/etc/hosts')
file_contents = hosts.read()
print(file_contents)
#ßhosts.close()

#another example
hosts_file_contents = hosts.read()
print('File closed? {}'.format(hosts.closed))
if not hosts.closed:
    hosts.close()

print('File closed? {}'.format(hosts.closed))
