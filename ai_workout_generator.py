import gradio as gr

def generate_workout(goal, level, equipment, days_per_week):
 
    return f"Generated workout for {goal}, {level} level, {days_per_week} days a week."

with gr.Blocks() as demo:
    goal = gr.Dropdown(["Build Muscle", "Lose Weight", "Increase Flexibility"])
    level = gr.Dropdown(["Beginner", "Intermediate", "Advanced"])
    equipment = gr.CheckboxGroup(["Dumbbells", "Barbell", "Bodyweight"])
    days_per_week = gr.Slider(1, 7, value=3)
    output = gr.Textbox(label="Generated Workout Plan")
    submit = gr.Button("Generate Plan")

    submit.click(generate_workout, [goal, level, equipment, days_per_week], output)

demo.launch(share=True)