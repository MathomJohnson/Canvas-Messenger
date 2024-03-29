import pytextnow as ptn
import requests
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
sid = os.getenv("SID")
csrf = os.getenv("CSRF")
phone = os.getenv("PHONE")
canvas_token = os.getenv("CANVAS_TOKEN")

url = "https://canvas.instructure.com/api/v1/courses"
params = {'access_token': canvas_token, 'include[]': 'total_scores'}

response = requests.get(url, params)
data = response.json()

client = ptn.Client(username, sid_cookie=sid, csrf_cookie=csrf)

message = ""
for course in data:
        if 'enrollments' in course and course['enrollments']:
                if "SP24" in course["name"]:
                        name = course["name"].split(":")[0]
                        message = message + name + ": " + str(course['enrollments'][0].get('computed_current_score')) + "%" + "\n"
client.send_sms(phone, message)
