from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def get_info():
    # Get query parameters
    name = request.args.get('name')
    id = request.args.get('id')

    # Calculate current day of the week and UTC time
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Construct GitHub URLs
    github_file_url = f'https://github.com/username/repo/blob/main/{id}.ext'
    github_repo_url = 'https://github.com/username/repo'

    # Prepare JSON response
    response_data = {
        'slack_name': name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': 'backend',
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
