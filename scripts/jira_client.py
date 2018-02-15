
# from jira import JIRA
import os
import requests

class JiraClient:
  def __init__(self, server=None, token=None):
    self.server = server if server is not None else 'http://pebl.itrsgroup.com'
    self.token = token if token is not None else os.environ.get('JIRA_TOKEN')
    self.headers = {'Authorization': 'Basic {0}'.format(self.token)}

  def get_remaining_days(self, sprint_id):
    try:
      response = requests.get('{0}/rest/greenhopper/1.0/gadgets/sprints/remainingdays?rapidViewId=53&sprintId={1}'.format(self.server, sprint_id), headers = self.headers)
      return response.json()['days']
    except:
      return None

  def getIssue(self, id):
    try:
      return self.jira_client.issue(id)
    except:
      return None

  def getSprint(self, id):
    try:
      return self.jira_client.sprint(id)
    except:
      return None

if __name__ == "__main__":
  jira_client = JiraClient("http://pebl.itrsgroup.com")
  # jira_issue = jira_client.getIssue("STARK-1888")
  # jira_sprint = jira_client.getSprint("169")
  # print(vars(jira_issue.fields))
  # print('Summary: {0} \nDescription: {1} \nLabels: {2}\nEstimation: {3}'.format(jira_issue.fields.summary.encode('utf-8').strip(), jira_issue.fields.description.encode(
  #     'utf-8').strip(), ''.join(str(e).encode('utf-8').strip() for e in jira_issue.fields.labels), str(jira_issue.fields.timeestimate).encode('utf-8').strip()))
  # print(dir(jira_issue.fields))
  # print(dir(jira_sprint))
  # print(jira_sprint.startDate)
  # print(jira_sprint.endDate)
  # print(jira_sprint.raw)
  print(jira_client.get_remaining_days("169"))