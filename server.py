from flask import Flask, render_template, request, jsonify, redirect
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN")


@app.route('/reviews', methods=['GET'])
def reviews():
    return render_template('reviews.html')

def main():
    app.run(port=5000, host='127.0.0.1')

if __name__ == '__main__':
    main()