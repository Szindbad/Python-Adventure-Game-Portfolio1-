from flask import Flask, request
import main
import screens
import catacomb_functions
import inventory
import sys

app = Flask(__name__)


@app.route('/')
def serve_game():
    return app.send_static_file('game/index.html')


@app.route('/terminal')
def serve_terminal():
    return '''
        <h1>Virtual Terminal</h1>
        <form id="terminal-form">
            <label for="command">Command:</label>
            <input type="text" id="command" name="command">
            <button type="submit">Submit</button>
        </form>
        <div id="output"></div>
        <script>
            document.getElementById("terminal-form").addEventListener("submit", function(event) {
                event.preventDefault();
                var commandInput = document.getElementById("command");
                var command = commandInput.value;
                commandInput.value = "";
                var outputDiv = document.getElementById("output");
                var xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function() {
                    if (xhr.readyState === 4 && xhr.status === 200) {
                        outputDiv.innerHTML += "<p>" + xhr.responseText + "</p>";
                    }
                }
                xhr.open("POST", "/terminal/command");
                xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
                xhr.send("command=" + encodeURIComponent(command));
            });
        </script>
    '''


@app.route('/terminal/command', methods=['POST'])
def process_command():
    command = request.form['command']
    try:
        # Execute the command as Python code
        exec(command)
        response = sys.stdout.getvalue()
    except Exception as e:
        response = str(e)
    return response


if __name__ == '__main__':
    app.run(debug=True)
