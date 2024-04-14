from flask import Flask, jsonify, render_template,request
import csv
import random
from datetime import datetime,timedelta

app = Flask(__name__)

workout_schedule = {
        'Monday': 'chest',
        'Tuesday': 'shoulders',
        'Wednesday': 'rest',
        'Thursday': 'arms',
        'Friday': 'rest',
        'Saturday': 'back',
        'Sunday': 'rest'
    }
# Function to get today's exercises
def get_date(day_count):
    today = datetime.now()
    date = today.strftime('%A')
    if day_count:
        date = today - timedelta(day_count)
        date = date.strftime('%A')
    return date

def get_todays_exercises(day_count):
    global workout_schedule
    today = get_date(day_count)
    muscle_group = workout_schedule[today]
    
    # If today is a rest day, return an empty list
    if muscle_group == 'rest':
        return []
    
    # Read exercises from the CSV file
    exercises = []
    with open('csvexercises.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['muscle_group'].lower() == muscle_group:
                exercises.append(row)
    
    # Randomly select 4 exercises for today's muscle group
    return random.sample(exercises, 4) if len(exercises) >= 4 else exercises

def today(day_count=0):
    # Get today's exercises
    exercises = get_todays_exercises(day_count)
    return exercises

@app.route('/',methods=['GET','POST'])
def home():
    data={
        'exercises':False,
        'metadata':{
            'date':datetime.now().strftime('%d-%m-%Y'),
            'day':datetime.now().strftime('%A'),
            'postrequest': False
        }
    }
    if request.method == 'POST':
        print('Post request made.')
        try:
            int(request.form['days'])
        except ValueError as e:
            print("Improper POST request: ValueError FLAGGED "+str(e))
            return render_template('index.html',data=data)
        except Exception as e2:
            print("Improper POST request: Unclassified error FLAGGED "+str(e2))
            return render_template('index.html',data=data)
        
        data['metadata']['postrequest']=True
        data['exercises'] =today(int(request.form['days']))
        date = datetime.now() - timedelta(int(request.form['days']))
        data['metadata']['day'] = date.strftime('%A')
        data['metadata']['date'] = date.strftime('%d-%m-%Y')
        
        return render_template('index.html',data=data)
    data['exercises']=today(0)
    return render_template('index.html',data=data)

if __name__ == '_main_':
    app.run(debug=True)