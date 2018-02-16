"""
JIRA Client 
"""

from config import JIRA_SERVER
from collections import Counter
import os
import requests
# Temporal Token
# enIpbGxhbG9iYXNAaXRyc2dyb3VwLmNvbTozNzEyMjR5SVQ3Nys3Nn==
class JiraClient:
  def __init__(self, server=None, token=None):
    self.server = server if server is not None else JIRA_SERVER
    self.token = token if token is not None else os.environ.get('JIRA_TOKEN')
    self.headers = {'Authorization': 'Basic {0}'.format(self.token)}

  def get_remaining_days(self, sprint_id):
    try:
      response = requests.get('{0}/rest/greenhopper/1.0/gadgets/sprints/remainingdays?rapidViewId=53&sprintId={1}'.format(self.server, sprint_id), headers = self.headers)
      return response.json()['days']
    except:
      return None
    
  def get_sprint_info(self, sprint_id):
    try:
      response = requests.get('{0}/rest/agile/1.0/sprint/{1}'.format(self.server, sprint_id), headers = self.headers)
      return response.json()
    except:
      return None
  
  def get_issues_in_sprint(self, sprint_id):
    try:
      response = requests.get('{0}/rest/api/2/search?jql=Sprint={1}'.format(self.server, sprint_id), headers = self.headers)
      return response.json()
    except:
      return None
  
  def get_issue(self, issue_id):
    try:
      response = requests.get('{0}/rest/api/2/issue/STARK-{1}'.format(self.server, issue_id), headers = self.headers)
      return response.json()
    except:
      return None

  def get_issues_number_in_sprint(self, sprint_id):
    try:
      sprint_issues = self.get_issues_in_sprint(sprint_id)
      sprint_total = sprint_issues['total']
      sprint_status_list = [issue['fields']['status']['statusCategory']['name'] for issue in sprint_issues['issues']]
      return {'total': sprint_total, 'status': Counter(sprint_status_list)}
    except:
      return None
