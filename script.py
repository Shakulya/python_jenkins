import jenkins

## In this line I am logging in to the Jenkins server
server = jenkins.Jenkins('http://jenkinsserver:8080', username='jenkins', password='jenkinspass')

# In this line I am confirming who I am
user = server.get_whoami()

# Here, it displays the version of Jenkins
version = server.get_version()

# Getting the task (api-interview)
my_job = server.get_job_config('api-interview')

# Building the job with PARAM1 and PARAM2 with the required message
server.build_job('api-interview', {'PARAM1': 'And all that glitters is gold', 'PARAM2': 'Only shooting stars bre&k the m@ld'})

# This will print the information about me and version of the jenkins
print('My full_name %s Version of the jenkins %s' % (user['fullName'], version))
