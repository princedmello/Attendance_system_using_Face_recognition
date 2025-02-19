# 🚨 Attendance System using Face Recognition

## 📌 Overview

The **Attendance System using Face Recognition** project is an advanced solution that automates the traditional manual attendance process by utilizing facial recognition technology. The system captures and stores the facial features of students, and upon detecting them in a classroom video feed, it automatically records their attendance. This approach significantly improves the efficiency and accuracy of attendance management, eliminating the need for manual intervention.

The system leverages **OpenCV** and the **face_recognition API** for face detection and recognition, enabling real-time identification of students. Faculty members can generate reports, track attendance, and search records easily, while a superuser manages administrative tasks such as adding new users and assigning roles.

---

## 🚀 Features

- 📹 **Real-time Attendance Tracking** – Automatically marks attendance based on face detection from live video.
- 🧑‍🏫 **Admin Privileges** – Superuser can grant access and manage records for both students and faculty.
- 👥 **Face Recognition** – Uses **OpenCV** and **face_recognition API** for accurate face detection and recognition.
- 🗂 **Attendance Database** – Stores attendance records and allows faculty to generate reports and search student data.
- 💻 **Web Interface** – Built with the **Django** framework for easy interaction and access by authorized users.
- 🔒 **Role-based Authentication** – Different user roles (student, faculty, admin) with specific access levels.
- 🔄 **Attendance Updates** – Automatically updates the attendance database when students are detected in the video feed.
  
---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🖥 **Python** | Backend logic and face recognition processing |
| 🎯 **Django** | Web framework for user interaction and attendance management |
| 👁 **OpenCV** | Real-time computer vision for face detection |
| 🧑‍🏫 **face_recognition API** | Accurate face recognition technology |
| 📊 **SQLite/MySQL** | Database for storing attendance records |
| 🔐 **Role-based Authentication** | User role management for admin, faculty, and students |
| 📹 **IP Camera/Webcam** | Video input for live classroom feed |

---

## 📥 Installation & Setup

### 🔹 Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **Django** (for web framework)
- **OpenCV** (for face detection)
- **face_recognition API** (for facial recognition functionality)
- **MySQL or SQLite** (for database setup)
- **Camera or Webcam** (for live video feed)

### 🔹 Clone the Repository
```sh
git clone https://github.com/princedmello/attendance-system-face-recognition.git
cd attendance-system-face-recognition
