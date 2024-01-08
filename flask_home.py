from flask import Flask, render_template, request, jsonify
from connectDB import connectDB

app = Flask(__name__)

@app.route('/track_click', methods=['POST'])
def track_click():
    data = request.json
    ip = request.remote_addr
    data['user_ip'] = ip
    table = "user_tracking"
    insert_query = f"""INSERT INTO {table} 
                    (user_ip, user_agent, accepted_languages, url, local_time, button_id, click_to_url) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    insert_data = ( data['user_ip'],
                    data['user_agent'],
                    data['accepted_languages'],
                    data['url'],
                    data['local_time'],
                    data['button_id'],
                    data['click_to_url'])
    
    connectDB(table = "user_tracking",query= insert_query ,data=insert_data)
    return jsonify({'status': 'success'})

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
