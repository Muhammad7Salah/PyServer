from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

script_path = "/home/muhammad7salah/py_server/"

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.get_json()
    script_name = data.get('script_name')
    print(script_name)

    if not script_name or not os.path.exists(script_name):
        return jsonify({'error': 'Script not found'}), 404

    try:
        
        result = subprocess.run(['python3', script_name], capture_output=True, text=True)

        if result.returncode == 0:
            return jsonify({'status': 'success', 'output': result.stdout})
        else:
            return jsonify({'output': result.stdout, 'error': result.stderr}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
