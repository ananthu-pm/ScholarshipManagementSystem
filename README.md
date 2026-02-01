# Scholarship Management System

A comprehensive Scholarship Management System that allows students to view and apply for scholarships, and enables various administrative bodies (University, College, School, School Board) to manage scholarship requests and notifications.

## 🚀 Tech Stack

### Web Backend
- **Framework**: Python Flask
- **Database**: MySQL
- **Dependencies**: `mysql-connector-python`, `flask`, `qrcode`, `pillow` (for QR generation)
- **Architecture**: Blueprint-based modular structure

### Android Application
- **Language**: Java
- **UI**: XML Layouts
- **Network**: `HttpURLConnection` (Custom `JsonReq` for API calls)
- **Minimum SDK**: 21 (Lollipop)
- **Target SDK**: 32 (Android 12)

---

## 📂 Project Structure

- `web-backend/`: Contains the Flask server, blueprints, and database logic.
- `android-app/`: Android Studio project for the student/user application.
- `database/`: Contains the SQL schema file (`scholarship_db.sql`).

---

## 🛠️ Setup Instructions

### Backend Setup
1. **Database Configuration**:
   - Import the `database/scholarship_db.sql` file into your MySQL server.
   - Adjust database credentials in `web-backend/database.py` if necessary.
2. **Install Dependencies**:
   ```bash
   pip install -r web-backend/requirements.txt
   ```
3. **Run the Server**:
   ```bash
   python web-backend/main.py
   ```
   The server will run on `http://0.0.0.0:5008`.

### Android App Setup
1. Open the `android-app/` folder in **Android Studio**.
2. Update the IP address in the `Ipsettings` class (if applicable) to point to your machine's local IP where the backend is running.
3. Build and run the app on an emulator or a physical device.

---

## 🔌 API Connections

The Android app communicates with the backend via JSON over HTTP. Major endpoints include:

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/logins` | GET | User authentication |
| `/api/viewscholarship` | GET | List available scholarships |
| `/api/sendrequest` | GET | Apply for a scholarship |
| `/api/Viewrequest` | GET | Check application status |
| `/api/Viewnotification` | GET | View system notifications |
| `/api/complaint` | GET | Send student complaints |

---

## 📱 Android App Features
- **Student Login**: Secure authentication for students.
- **Scholarship Browsing**: View various scholarships with categories.
- **Application Tracking**: Real-time status updates on scholarship requests.
- **Notifications**: Stay updated with the latest scholarship news.
- **Complaint Management**: Direct communication channel for issues.
