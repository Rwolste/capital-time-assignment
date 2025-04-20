from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# Authorized Token
VALID_TOKEN = "mysecrettoken123"

# Expanded capital city timezone mappings
city_timezones = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Paris": "Europe/Paris",
    "Tokyo": "Asia/Tokyo",
    "Delhi": "Asia/Kolkata",
    "Canberra": "Australia/Sydney",
    "Ottawa": "America/Toronto",
    "Brasilia": "America/Sao_Paulo",
    "Beijing": "Asia/Shanghai",
    "Moscow": "Europe/Moscow",
    "Berlin": "Europe/Berlin",
    "Rome": "Europe/Rome",
    "Madrid": "Europe/Madrid",
    "Cairo": "Africa/Cairo",
    "Bangkok": "Asia/Bangkok",
    "Jakarta": "Asia/Jakarta",
    "Seoul": "Asia/Seoul",
    "Riyadh": "Asia/Riyadh",
    "Mexico City": "America/Mexico_City",
    "Buenos Aires": "America/Argentina/Buenos_Aires",
    "Ankara": "Europe/Istanbul",
    "Nairobi": "Africa/Nairobi",
    "Abuja": "Africa/Lagos",
    "Hanoi": "Asia/Bangkok",
    "Tehran": "Asia/Tehran",
    "Baghdad": "Asia/Baghdad",
    "Kabul": "Asia/Kabul",
    "Damascus": "Asia/Damascus",
    "Lisbon": "Europe/Lisbon",
    "Oslo": "Europe/Oslo",
    "Stockholm": "Europe/Stockholm",
    "Copenhagen": "Europe/Copenhagen",
    "Helsinki": "Europe/Helsinki",
    "Warsaw": "Europe/Warsaw",
    "Athens": "Europe/Athens",
    "Vienna": "Europe/Vienna",
    "Bern": "Europe/Zurich",
    "Brussels": "Europe/Brussels",
    "Amsterdam": "Europe/Amsterdam",
    "Dublin": "Europe/Dublin",
    "Reykjavik": "Atlantic/Reykjavik",
    "Prague": "Europe/Prague",
    "Budapest": "Europe/Budapest",
    "Sofia": "Europe/Sofia",
    "Zagreb": "Europe/Zagreb",
    "Belgrade": "Europe/Belgrade",
    "Skopje": "Europe/Skopje",
    "Tirana": "Europe/Tirane",
    "Podgorica": "Europe/Podgorica",
    "Sarajevo": "Europe/Sarajevo",
    "Vilnius": "Europe/Vilnius",
    "Riga": "Europe/Riga",
    "Tallinn": "Europe/Tallinn"
}

@app.route('/api/time', methods=['GET'])
def get_time():
    token = request.headers.get("Authorization")
    if token != VALID_TOKEN:
        return jsonify({"error": "Unauthorized access. Valid token required."}), 401

    capital = request.args.get('capital')
    if not capital:
        return jsonify({"error": "Missing 'capital' parameter."}), 400

    timezone_name = city_timezones.get(capital)
    if not timezone_name:
        return jsonify({"error": f"Capital '{capital}' not found in database."}), 404

    timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(timezone)
    utc_offset = current_time.strftime('%z')
    formatted_offset = f"UTC{'+' if int(utc_offset) >= 0 else ''}{int(utc_offset) // 100}"

    return jsonify({
        "capital": capital,
        "local_time": current_time.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": formatted_offset
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
