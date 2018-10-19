import jenkins

## In this line i am logining as jenkins user and my passord is jenkinspass
server = jenkins.Jenkins('http://jenkinsserver:8080', username='jenkins', password='jenkinspass')

# In this line I am confirming who I am
user = server.get_whoami()

# In this line I geting version of the jenkins
version = server.get_version()

# In this line I am geting my job (api-interview)
my_job = server.get_job_config('api-interview')

# This line will build the job with PARAM1 and PARAM2 with required message
server.build_job('api-interview', {'PARAM1': 'And all that glitters is gold', 'PARAM2': 'Only shooting stars bre&k the m@ld'})

# This line will print all information about me and version of thew jenkins
print('My full_name %s Version of the jenkins %s' % (user['fullName'], version))
