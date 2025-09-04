import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import tkinter as tk

df = pd.read_csv("student_performance.csv")
features = ['StudyHours', 'AttendanceRate']
X = df[features]
y = df.Passed

X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42)

classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)

#Interface
root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=400)
canvas1.pack()

label1 = tk.Label(root, text="Study Hours: ")
canvas1.create_window(100, 100, window=label1)
entry1 = tk.Entry(root)
canvas1.create_window(250, 100, window=entry1)

label2 = tk.Label(root, text="Attendance Rate: ")
canvas1.create_window(100, 140, window=label2)
entry2 = tk.Entry(root)
canvas1.create_window(250, 140, window=entry2)

result_label = tk.Label(root, text="")
canvas1.create_window(200, 260, window=result_label)

def values():
    global StudyHours
    StudyHours = float(entry1.get())
    global AttendanceRate
    AttendanceRate = float(entry2.get())

    new_df = pd.DataFrame({
        'StudyHours': [StudyHours],
        'AttendanceRate': [AttendanceRate]
    })
    pred = classifier.predict(new_df)
    if pred[0] == 1:
        result_label.configure(text="Pass", bg="green")
    else:
        result_label.configure(text="Failed", bg="red")


button1 = tk.Button(root, text="Submit", command=values)
canvas1.create_window(200, 190, window=button1)

root.mainloop()