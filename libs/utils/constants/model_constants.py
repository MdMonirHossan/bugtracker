# Status options for Bug
STATUS_CHOICES = (
  ('Open', 'Open'), 
  ('In Progress', 'In Progress'), 
  ('Resolved', 'Resolved')
)

# Priority options for Bug
PRIORITY_CHOICES = (
    ('Low', 'Low'), 
    ('Medium', 'Medium'), 
    ('High', 'High')
)

# Action options for Activity Log
ACTION_CHOICES = (
    ('bug_created', 'Bug Created'),
    ('bug_updated', 'Bug Updated'),
    ('comment_created', 'Comment Created'),
    ('comment_updated', 'Comment Updated'),
    ('project_created', 'Project Created'),
    ('project_updated', 'Projected Update')
)