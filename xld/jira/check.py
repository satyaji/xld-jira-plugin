from jira.jiracommunicator import communicator

communicator = communicator.JiraCommunicator(url,username, password)
if not communicator.issue_exists(jira):
    raise ValueError("[%s] Not Found in %s" % (jira, communicator))

print "Done."
