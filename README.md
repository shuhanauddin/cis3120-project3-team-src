# cis3120-project3-team-src
Workout Routine Builder for CIS 3120 Project 3

For this project we created a web application that collects data from an external source; in this sceneario it was a Ninjas Exercise API. ('https://api.api-ninjas.com/v1/exercises?type=strength&limit=100'). This project uses a generative AI model to provide personalized insights based on user input. Shuhana Uddin collected and organized different types of workout exercises like strength, cardio, and flexibility. She filtered and removed duplicate entries, then saved them all the organized data into a structured JSON file named all_exercises.json. 

The Gradio app was created by Ramsil. It collects user input on fitness goals, experience level, equipment, and workout frequency to generate a simple workout summary. The app provides an interactive interface for customizing basic fitness plans. Ramsil also collected and organized the required Python dependencies in a requirements.txt file.

Chrisleidy created the ai_workout_generator.py file, which connects user input from the web app to the OpenAI API. She also wrote the generate_workout() function that uses ChatGPT to produce personalized workout plans based on fitness goals, level, equipment, and number of workout days.
