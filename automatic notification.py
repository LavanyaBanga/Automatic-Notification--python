import pyttsx3
import time
from datetime import datetime

def speak(text, voice_id):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.say(text)
    engine.runAndWait()

def remind_task(task, voice_id):
    speak(f"It's time to {task}", voice_id)

def reminder_schedule(task_list, voice_id):
    while task_list:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        for task, task_time in task_list:
            if current_time == task_time:
                remind_task(task, voice_id)
                task_list.remove((task, task_time))
        time.sleep(30)
def get_tasks():
    tasks = []
    n = int(input("How many task do u want to add"))
    for _ in range(n):
        task = input("Name the task: ")
        task_time = input("Enter the time of task: ")
        tasks.append((task, task_time))
    return tasks
tasks = get_tasks()
voice_id = 1  
reminder_schedule(tasks, voice_id)
