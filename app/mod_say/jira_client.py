"""
JIRA Client 
"""

from config import JIRA_SERVER
import os
import requests

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
