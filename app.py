from flask import Flask, render_template_string, request, jsonify, g, redirect
import random
import names
app = Flask(__name__)



@app.route('/randomCatchall')
def randomCatchall():
    amount = request.args.get('AMOUNT')
    catchall = request.args.get('CATCHALL')
    NAMES = []
    for i in range(int(amount)):
        NAMES.append(f'{names.get_first_name()}{names.get_last_name()}{random.randint(10,100)}@{catchall}<br>')
    return ''.join(NAMES)


if __name__ == "__main__":
    app.run()