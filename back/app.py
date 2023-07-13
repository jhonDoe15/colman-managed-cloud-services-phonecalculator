import json
import psycopg2
import psycopg2.extras
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

app = Flask(__name__)
con = psycopg2.connect('')
cursor = con.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

@app.route("/phone/all", methods=['get'])
@cross_origin(origin='*')
def fetch_all_phones():
    cursor.execute("select * from phone")
    result = cursor.fetchall()
    return jsonify(result), 200


@app.route("/phone", methods=['post'])
@cross_origin(origin='*')
def add_phone():
    cursor.execute("select count(*) from phone")
    current_count = cursor.fetchone()
    print(request.data)
    device_object = json.loads(request.data)
    device_object['id'] = current_count['count']
    print(device_object)
    cursor.execute("""INSERT INTO phone 
            VALUES (%(id)s,
            %(device_name)s, 
            %(battery_life)s, 
            %(price)s, 
            %(year)s, 
            %(image_url)s, 
            %(screen_size)s, 
            %(phone_url)s, 
            %(has_nfc)s, 
            %(has_headphone_jack)s, 
            %(has_dual_sim)s, 
            %(has_ir)s, 
            %(antutu_score)s)""", device_object)
    con.commit()
    return "record inserted", 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
