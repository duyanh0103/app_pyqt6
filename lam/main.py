# from PyQt6 import QtWidgets, QtCore
# from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox
# from PyQt6 import uic
# import sys
# from task import createTask, Task

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('gui/main.ui',self)
#         self.addTaskBtn.clicked.connect(self.showAddTask)
#     def showAddTask(self):
#         self.addTask_window = AddTask()
#         self.addTask_window.task_saved.connect(self.handle_task_saved)
#         addTask_window.show()

#     def handle_task_saved(self, task):
#         # Handle the task data (e.g., add it to a list or display it in the UI)
#         print("Task saved:", task)
#         # Here you could add the task to a list widget or similar in the main window
# class AddTask(QDialog):
#     task_saved = QtCore.pyqtSignal(Task)

#     def __init__(self):
#         super().__init__()
#         uic.loadUi('gui/addTask.ui',self)
#         self.saveBtn.clicked.connect(self.saveTask)
#         self.cancelBtn.clicked.connect(self.close)

#     def saveTask(self):
#         topic = self.topicLineEdit.text()
#         deadline = self.deadlineDateEdit.dateTime().toPyDateTime()
#         description = self.descriptionTextEdit.toPlainText()

#         task = createTask(topic, deadline, description)
#         self.task_saved.emit(task)
#         self.close()
#     def close(self):
#         self.reject()
    
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     main_window = MainWindow()
#     addTask_window = AddTask()
#     main_window.show()
#     sys.exit(app.exec())


from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt6 import uic
import sys
from task import createTask, Task

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/main.ui', self)
        self.addTaskBtn.clicked.connect(self.showAddTask)

    def showAddTask(self):
        self.addTaskWindow = AddTask()
        self.addTaskWindow.task_saved.connect(self.handle_task_saved)
        self.addTaskWindow.show()

    def handle_task_saved(self, task):
        # Handle the task data (e.g., add it to a list or display it in the UI)
        print("Task saved:", task.topic)
        # Here you could add the task to a list widget or similar in the main window

class AddTask(QDialog):
    task_saved = QtCore.pyqtSignal(Task)

    def __init__(self):
        super().__init__()
        uic.loadUi('gui/addTask.ui', self)
        self.saveBtn.clicked.connect(self.saveTask)
        self.cancelBtn.clicked.connect(self.close)

    def saveTask(self):
        topic = self.topicLineEdit.text()
        deadline = self.deadlineDateEdit.dateTime().toPyDateTime()
        description = self.descriptionTextEdit.toPlainText()

        task = createTask(topic, deadline, description)
        self.task_saved.emit(task)
        self.close()

    def close(self):
        self.reject()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
