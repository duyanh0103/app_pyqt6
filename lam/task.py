import datetime
from plyer import notification
import schedule
import time
class Task:
    def __init__(self, topic, deadlineDate, description, completed = False):
        self.topic = topic
        self.deadlineDate = deadlineDate
        self.description = description
        self.completed = completed
    def doneTask(self):
        self.completed = True
        
def createTask(topic, deadlineDate, description):
    return Task(topic, deadlineDate, description)

# task1 = createTask("Học toán",datetime.datetime.now(),"",)

# print(f"Tiêu đề: {task1.topic}")

# print(f"Ngày hết hạn: {task1.deadlineDate.strftime('%d/%m/%Y')}")

# print(f"Mô tả: {task1.description}")

def notify_task(task):
    notification.notify(
        title=f"Deadline for {task.topic}",
        message=f"Due Date: {task.deadlineDate.strftime('%d/%m/%Y')}\nDescription: {task.description}",
        timeout=10
    )

# currentTime = datetime.datetime.now()



# notification.notify(
# title = "Sample Notification",
# message = "This is a sample notification",
# timeout = 10
# )

# def schedule_task_notification(task):
#     notify_task(task)  # Notify immediately
#     # Schedule future notifications if needed
#     schedule.every().day.at(datetime.datetime.now().strftime("%H:%M")).do(notify_task, task=task)

# # Create a task
# task1 = createTask("Học toán", datetime.datetime.now(), "")

# # Print task details
# print(f"Tiêu đề: {task1.topic}")
# print(f"Ngày hết hạn: {task1.deadlineDate.strftime('%d/%m/%Y')}")
# print(f"Mô tả: {task1.description}")

# # Schedule the notification to run immediately
# schedule_task_notification(task1)

# # Keep the script running to check for scheduled tasks
# while True:
#     schedule.run_pending()
#     time.sleep(1)