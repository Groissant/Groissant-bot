import unittest
from app import app


class FlaskTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_post_data(self):
        response = self.app.post('/', json={
            'action': 'edited',
            'changes': {
                'body': {'from': 'Edit issue comment'}
            },
            'issue': {
                'url': 'https://api.github.com/repos/wxharry/playground/issues/1',
                'repository_url': 'https://api.github.com/repos/wxharry/playground',
                'labels_url': 'https://api.github.com/repos/wxharry/playground/issues/1/labels{/name}',
                'comments_url': 'https://api.github.com/repos/wxharry/playground/issues/1/comments',
                'events_url': 'https://api.github.com/repos/wxharry/playground/issues/1/events',
                'html_url': 'https://github.com/wxharry/playground/issues/1',
                'id': 2069548051,
                'node_id': 'I_kwDOLB_yMM57WswT',
                'number': 1,
                'title': 'First issue',
                'user': {
                    'login': 'wxharry',
                    'id': 39271899,
                    'node_id': 'MDQ6VXNlcjM5MjcxODk5',
                    'avatar_url': 'https://avatars.githubusercontent.com/u/39271899?v=4',
                    'gravatar_id': '',
                    'url': 'https://api.github.com/users/wxharry',
                    'html_url': 'https://github.com/wxharry',
                    'followers_url': 'https://api.github.com/users/wxharry/followers',
                    'following_url': 'https://api.github.com/users/wxharry/following{/other_user}',
                    'gists_url': 'https://api.github.com/users/wxharry/gists{/gist_id}',
                    'starred_url': 'https://api.github.com/users/wxharry/starred{/owner}{/repo}',
                    'subscriptions_url': 'https://api.github.com/users/wxharry/subscriptions',
                    'organizations_url': 'https://api.github.com/users/wxharry/orgs',
                    'repos_url': 'https://api.github.com/users/wxharry/repos',
                    'events_url': 'https://api.github.com/users/wxharry/events{/privacy}',
                    'received_events_url': 'https://api.github.com/users/wxharry/received_events',
                    'type': 'User',
                    'site_admin': False
                },
                'labels': [],
                'state': 'open',
                'locked': False,
                'assignee': None,
                'assignees': [],
                'milestone': None,
                'comments': 1,
                'created_at': '2024-01-08T03:22:03Z',
                'updated_at': '2024-01-09T02:55:13Z',
                'closed_at': None,
                'author_association': 'OWNER',
                'active_lock_reason': None,
                'body': 'This is an issue',
                'reactions': {
                    'url': 'https://api.github.com/repos/wxharry/playground/issues/1/reactions',
                    'total_count': 0,
                    '+1': 0,
                    '-1': 0,
                    'laugh': 0,
                    'hooray': 0,
                    'confused': 0,
                    'heart': 0,
                    'rocket': 0,
                    'eyes': 0
                },
                'timeline_url': 'https://api.github.com/repos/wxharry/playground/issues/1/timeline',
                'performed_via_github_app': None,
                'state_reason': None
            },
            'comment': {
                'url': 'https://api.github.com/repos/wxharry/playground/issues/comments/1882265574',
                'html_url': 'https://github.com/wxharry/playground/issues/1#issuecomment-1882265574',
                'issue_url': 'https://api.github.com/repos/wxharry/playground/issues/1',
                'id': 1882265574,
                'node_id': 'IC_kwDOLB_yMM5wMRfm',
                'user': {
                    'login': 'wxharry',
                    'id': 39271899,
                    'node_id': 'MDQ6VXNlcjM5MjcxODk5',
                    'avatar_url': 'https://avatars.githubusercontent.com/u/39271899?v=4',
                    'gravatar_id': '',
                    'url': 'https://api.github.com/users/wxharry',
                    'html_url': 'https://github.com/wxharry',
                    'followers_url': 'https://api.github.com/users/wxharry/followers',
                    'following_url': 'https://api.github.com/users/wxharry/following{/other_user}',
                    'gists_url': 'https://api.github.com/users/wxharry/gists{/gist_id}',
                    'starred_url': 'https://api.github.com/users/wxharry/starred{/owner}{/repo}',
                    'subscriptions_url': 'https://api.github.com/users/wxharry/subscriptions',
                    'organizations_url': 'https://api.github.com/users/wxharry/orgs',
                    'repos_url': 'https://api.github.com/users/wxharry/repos',
                    'events_url': 'https://api.github.com/users/wxharry/events{/privacy}',
                    'received_events_url': 'https://api.github.com/users/wxharry/received_events',
                    'type': 'User',
                    'site_admin': False
                },
                'created_at': '2024-01-09T02:53:37Z',
                'updated_at': '2024-01-09T02:55:13Z',
                'author_association': 'OWNER',
                'body': 'Edit issue comment 1',
                'reactions': {
                    'url': 'https://api.github.com/repos/wxharry/playground/issues/comments/1882265574/reactions',
                    'total_count': 0,
                    '+1': 0,
                    '-1': 0,
                    'laugh': 0,
                    'hooray': 0,
                    'confused': 0,
                    'heart': 0,
                    'rocket': 0,
                    'eyes': 0
                },
                'performed_via_github_app': None
            },
            'repository': {
                'id': 740291120,
                'node_id': 'R_kgDOLB_yMA',
                'name': 'playground',
                'full_name': 'wxharry/playground',
                'private': True,
                'owner': {
                    'login': 'wxharry',
                    'id': 39271899,
                    'node_id': 'MDQ6VXNlcjM5MjcxODk5',
                    'avatar_url': 'https://avatars.githubusercontent.com/u/39271899?v=4',
                    'gravatar_id': '',
                    'url': 'https://api.github.com/users/wxharry',
                    'html_url': 'https://github.com/wxharry',
                    'followers_url': 'https://api.github.com/users/wxharry/followers',
                    'following_url': 'https://api.github.com/users/wxharry/following{/other_user}',
                    'gists_url': 'https://api.github.com/users/wxharry/gists{/gist_id}',
                    'starred_url': 'https://api.github.com/users/wxharry/starred{/owner}{/repo}',
                    'subscriptions_url': 'https://api.github.com/users/wxharry/subscriptions',
                    'organizations_url': 'https://api.github.com/users/wxharry/orgs',
                    'repos_url': 'https://api.github.com/users/wxharry/repos',
                    'events_url': 'https://api.github.com/users/wxharry/events{/privacy}',
                    'received_events_url': 'https://api.github.com/users/wxharry/received_events',
                    'type': 'User',
                    'site_admin': False
                },
                'html_url': 'https://github.com/wxharry/playground',
                'description': None,
                'fork': False,
                'url': 'https://api.github.com/repos/wxharry/playground',
                'forks_url': 'https://api.github.com/repos/wxharry/playground/forks',
                'keys_url': 'https://api.github.com/repos/wxharry/playground/keys{/key_id}',
                'collaborators_url': 'https://api.github.com/repos/wxharry/playground/collaborators{/collaborator}',
                'teams_url': 'https://api.github.com/repos/wxharry/playground/teams',
                'hooks_url': 'https://api.github.com/repos/wxharry/playground/hooks',
                'issue_events_url': 'https://api.github.com/repos/wxharry/playground/issues/events{/number}',
                'events_url': 'https://api.github.com/repos/wxharry/playground/events',
                'assignees_url': 'https://api.github.com/repos/wxharry/playground/assignees{/user}',
                'branches_url': 'https://api.github.com/repos/wxharry/playground/branches{/branch}',
                'tags_url': 'https://api.github.com/repos/wxharry/playground/tags',
                'blobs_url': 'https://api.github.com/repos/wxharry/playground/git/blobs{/sha}',
                'git_tags_url': 'https://api.github.com/repos/wxharry/playground/git/tags{/sha}',
                'git_refs_url': 'https://api.github.com/repos/wxharry/playground/git/refs{/sha}',
                'trees_url': 'https://api.github.com/repos/wxharry/playground/git/trees{/sha}',
                'statuses_url': 'https://api.github.com/repos/wxharry/playground/statuses/{sha}',
                'languages_url': 'https://api.github.com/repos/wxharry/playground/languages',
                'stargazers_url': 'https://api.github.com/repos/wxharry/playground/stargazers',
                'contributors_url': 'https://api.github.com/repos/wxharry/playground/contributors',
                'subscribers_url': 'https://api.github.com/repos/wxharry/playground/subscribers',
                'subscription_url': 'https://api.github.com/repos/wxharry/playground/subscription',
                'commits_url': 'https://api.github.com/repos/wxharry/playground/commits{/sha}',
                'git_commits_url': 'https://api.github.com/repos/wxharry/playground/git/commits{/sha}',
                'comments_url': 'https://api.github.com/repos/wxharry/playground/comments{/number}',
                'issue_comment_url': 'https://api.github.com/repos/wxharry/playground/issues/comments{/number}',
                'contents_url': 'https://api.github.com/repos/wxharry/playground/contents/{+path}',
                'compare_url': 'https://api.github.com/repos/wxharry/playground/compare/{base}...{head}',
                'merges_url': 'https://api.github.com/repos/wxharry/playground/merges',
                'archive_url': 'https://api.github.com/repos/wxharry/playground/{archive_format}{/ref}',
                'downloads_url': 'https://api.github.com/repos/wxharry/playground/downloads',
                'issues_url': 'https://api.github.com/repos/wxharry/playground/issues{/number}',
                'pulls_url': 'https://api.github.com/repos/wxharry/playground/pulls{/number}',
                'milestones_url': 'https://api.github.com/repos/wxharry/playground/milestones{/number}',
                'notifications_url': 'https://api.github.com/repos/wxharry/playground/notifications{?since,all,participating}',
                'labels_url': 'https://api.github.com/repos/wxharry/playground/labels{/name}',
                'releases_url': 'https://api.github.com/repos/wxharry/playground/releases{/id}',
                'deployments_url': 'https://api.github.com/repos/wxharry/playground/deployments',
                'created_at': '2024-01-08T03:20:56Z',
                'updated_at': '2024-01-08T03:20:57Z',
                'pushed_at': '2024-01-08T03:20:57Z',
                'git_url': 'git://github.com/wxharry/playground.git',
                'ssh_url': 'git@github.com:wxharry/playground.git',
                'clone_url': 'https://github.com/wxharry/playground.git',
                'svn_url': 'https://github.com/wxharry/playground',
                'homepage': None,
                'size': 0,
                'stargazers_count': 0,
                'watchers_count': 0,
                'language': None,
                'has_issues': True,
                'has_projects': True,
                'has_downloads': True,
                'has_wiki': True,
                'has_pages': False,
                'has_discussions': False,
                'forks_count': 0,
                'mirror_url': None,
                'archived': False,
                'disabled': False,
                'open_issues_count': 1,
                'license': None,
                'allow_forking': True,
                'is_template': False,
                'web_commit_signoff_required': False,
                'topics': [],
                'visibility': 'private',
                'forks': 0,
                'open_issues': 1,
                'watchers': 0,
                'default_branch': 'main'
            },
            'sender': {
                'login': 'wxharry',
                'id': 39271899,
                'node_id': 'MDQ6VXNlcjM5MjcxODk5',
                'avatar_url': 'https://avatars.githubusercontent.com/u/39271899?v=4',
                'gravatar_id': '',
                'url': 'https://api.github.com/users/wxharry',
                'html_url': 'https://github.com/wxharry',
                'followers_url': 'https://api.github.com/users/wxharry/followers',
                'following_url': 'https://api.github.com/users/wxharry/following{/other_user}',
                'gists_url': 'https://api.github.com/users/wxharry/gists{/gist_id}',
                'starred_url': 'https://api.github.com/users/wxharry/starred{/owner}{/repo}',
                'subscriptions_url': 'https://api.github.com/users/wxharry/subscriptions',
                'organizations_url': 'https://api.github.com/users/wxharry/orgs',
                'repos_url': 'https://api.github.com/users/wxharry/repos',
                'events_url': 'https://api.github.com/users/wxharry/events{/privacy}',
                'received_events_url': 'https://api.github.com/users/wxharry/received_events',
                'type': 'User',
                'site_admin': False
            },
            'installation': {
                'id': 45869656,
                'node_id': 'MDIzOkludGVncmF0aW9uSW5zdGFsbGF0aW9uNDU4Njk2NTY='
            }
        })
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()