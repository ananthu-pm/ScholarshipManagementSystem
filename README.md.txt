# Scholarship Management System 🎓

A full-stack application for managing scholarships, featuring a web-based administration panel and a mobile application for students.

## 🚀 Features
* **Web Portal:** Built with Flask for admins to manage scholarship listings and applications.
* **Mobile App:** Android application (Java) for students to browse and apply.
* **Database:** Centralized MySQL database to sync data between web and mobile.

---

## 🛠️ Tech Stack
* **Backend:** Python (Flask)
* **Frontend (Web):** HTML, CSS, Bootstrap
* **Mobile:** Android Studio (Java, XML)
* **Database:** MySQL
* **API:** RESTful JSON responses for Android connectivity

---

## 📁 Project Structure
```text
├── web-backend/          # Flask application files
│   ├── app.py            # Main entry point
│   ├── templates/        # HTML files
│   └── static/           # CSS/JS files
├── android-app/          # Android Studio Project (Java)
└── database/             # Contains scholarship_db.sql schema