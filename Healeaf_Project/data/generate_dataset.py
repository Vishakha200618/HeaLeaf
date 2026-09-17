import pandas as pd
import random

data = []

moods = ["Happy", "Neutral", "Sad", "Anxious"]
pressure = ["Low", "Medium", "High"]
meditation = ["Yes", "No"]
genders = ["Male", "Female"]

for i in range(1, 201):

    age = random.randint(18, 25)
    study_hours = random.randint(1, 10)
    sleep_hours = random.randint(3, 9)
    screen_time = random.randint(2, 12)
    physical_activity = random.randint(0, 3)
    social_interaction = random.randint(0, 5)

    stress = random.randint(1, 10)
    anxiety = random.randint(1, 10)

    mood = random.choice(moods)
    academic_pressure = random.choice(pressure)
    meditate = random.choice(meditation)
    gender = random.choice(genders)

    mental_health_score = (
        sleep_hours * 10
        + physical_activity * 10
        + social_interaction * 5
        - stress * 5
        - anxiety * 5
    )

    data.append([
        i,
        age,
        gender,
        study_hours,
        sleep_hours,
        screen_time,
        physical_activity,
        social_interaction,
        academic_pressure,
        mood,
        stress,
        anxiety,
        meditate,
        mental_health_score
    ])

columns = [
    "Student_ID",
    "Age",
    "Gender",
    "Study_Hours",
    "Sleep_Hours",
    "Screen_Time",
    "Physical_Activity",
    "Social_Interaction",
    "Academic_Pressure",
    "Mood",
    "Stress_Level",
    "Anxiety_Level",
    "Meditation",
    "Mental_Health_Score"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("healeaf_dataset.csv", index=False)

print("Dataset Created Successfully!")