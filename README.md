# 🎓 Student Performance Predictor

This is a simple machine learning application that predicts whether a student will pass or fail based on their **study hours** and **attendance rate**. It uses a **Decision Tree Classifier** and provides a user-friendly **Tkinter GUI** for interaction.

## 🚀 Features

- Predicts student performance using a trained ML model
- Interactive GUI built with Tkinter
- Real-time prediction with visual feedback (green for pass, red for fail)

## 📁 Dataset

The app uses a CSV file named `student_performance.csv` with the following columns:

| StudyHours | AttendanceRate | Passed |
|------------|----------------|--------|
| 5.0        | 0.85           | 1      |
| 2.5        | 0.60           | 0      |
| ...        | ...            | ...    |

- `StudyHours`: Number of hours the student studied (float)
- `AttendanceRate`: Attendance percentage (float between 0 and 1)
- `Passed`: Target label (1 for pass, 0 for fail)

## 🧠 Model Training

The model is trained using scikit-learn's `DecisionTreeClassifier`:

```python
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)
