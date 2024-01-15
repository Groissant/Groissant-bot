from flask import request, jsonify, send_file
from github import Github, Auth

from app import app, gh_integration
from core import get_response

@app.route("/", methods=['POST'])
def bot():
    # Get the event payload
    payload = request.json

    # Should be able to valid if this is a GitHub event
    
    # Check if it is a GitHub PR or Issue
    if not ('action' in payload) or not ('pull_request' in payload or 'issue' in payload):
        return jsonify({'status': 'success', 'message': "no opened PR or Issue detected"}), 200

    owner = payload['repository']['owner']['login']
    repo_name = payload['repository']['name']

    gh_connection = gh_integration.get_repo_installation(owner, repo_name).get_github_for_installation()
    repo = gh_connection.get_repo(f"{owner}/{repo_name}")
    event_type = 'pull_request' if 'pull_request' in payload else 'issue'
    issue = repo.get_issue(number=payload[event_type]['number'])

    # if the last comment @Groissant, get response
    if issue.get_comments().totalCount > 0:
        last_comment = issue.get_comments().reversed[0]
        # last line of comment @Groissant
        if last_comment.user.login != 'Groissant' and \
                last_comment.body.splitlines()[-1].startswith('@Groissant'):
            response = get_response(repo.url, last_comment.body.splitlines()[-1].replace('@Groissant', ''))
            issue.create_comment(response.choices[0].message.content)

    return jsonify({'status': 'success'}), 200
