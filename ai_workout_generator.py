import gradio as gr
import openai
import json
import random
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


with open('all_exercises.json', 'r') as f:
    exercise_list = json.load(f)


def generate_workout(goal, level, equipment, days):
    sample = random.sample(exercise_list, min(10, len(exercise_list)))
    sample_names = [ex['name'] for ex in sample]

    prompt = f"""
        Create a {level} workout plan for someone who wants to {goal}.
        They have: {', '.join(equipment)}.
        Use exercises like: {', '.join(exercise_names)}.
        Make a {days}-day-per-week schedule with sets and reps.
        Format it as: Day 1, Day 2, etc.
        """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']

