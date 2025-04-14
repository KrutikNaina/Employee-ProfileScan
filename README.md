# 📇 Employee QR Code ID System

A simple, web-based employee management system built with **Django** and **SQLite**, where each employee is assigned a unique **QR code** embedded on their ID card. Scanning the code via a smartphone or the in-app **QR Scanner Page** redirects to a mobile-friendly **profile page** displaying key employee details.

---

## 🚀 Features

- ✅ Unique QR Code for each employee
- ✅ Profile details include:
  - Employee ID  
  - Employee Name  
  - Address  
  - Salary  
  - City  
  - Profile Photo
- ✅ 📷 **QR Scanner Page** – Scan directly from your device camera on the website
- ✅ Admin Dashboard for HR/Admin to:
  - Create, update, and manage employee profiles
  - Automatically generate unique QR codes
- ✅ Mobile-Friendly profile view
- ✅ Optional access control for secure data handling

---

## 🔧 Technologies Used

- 🐍 Python (Django Framework)
- 🗃 SQLite (Default Django Database)
- 📦 qrcode (Python package)
- 🖼 Pillow (For image handling)
- 🌐 HTML, CSS (Bootstrap for responsive design)
- 📱 Javascript QR Scanner using `html5-qrcode.js`

---

## 💡 Use Cases

- ✔ Corporate Employee ID System  
- ✔ Small to Medium Business HR Tools  
- ✔ Secure Contactless Employee Information Display  
- ✔ On-site Visitor or Employee QR Scanning via Web App

---
## ⚙️ How It Works

1. **Admin Login** → Access admin panel to manage employees.
2. **Create Profile** → Add employee info and upload profile photo.
3. **QR Code Generated** → Automatically linked to their profile page.
4. **Scan the Code** →  
   - Option 1: Use a regular smartphone camera  
   - Option 2: Use the built-in **QR Scanner Page** (`/scan/`)
5. **Employee Profile Opens** → View employee information instantly

---

## 🖥️ QR Scanner Page

The system includes a built-in QR scanner using the device camera:

**URL:** `/scan/`

## 🛠 Installation

# Clone the repo
git clone [https://github.com/KrutikNaina/Employee-ProfileScan.git](https://github.com/KrutikNaina/Employee-ProfileScan.git) <br>
cd QR_Employee_Scanner

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver

## 🔐 Access Control
- Profile pages can be public or protected with Django login.
- Admin dashboard is secured with Django's authentication system.

## **License**  
This project is open-source under the **MIT License**. 

## 👨‍💻 Author
Built with ❤️ by Krutik Naina


Let me know if you also want:
- `urls.py` and view setup for the `/scan/` route
- Sample QR generation and profile template
- Docker support or deployment tips

Happy coding! 💻✨


