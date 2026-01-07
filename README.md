Office Employee Management System

A comprehensive Django-based web application for managing office employees, departments, and employee-related information within an organization.

🌟 Features

Core Functionality

Employee Management: Add, view, edit, and delete employee records
Department Management: Organize employees into departments
Role-Based Access Control: Different permissions for admin, managers, and regular employees
Attendance Tracking: Monitor employee attendance and working hours
Leave Management: Request and approve employee leave applications
Performance Reviews: Track and evaluate employee performance
Key Modules

Authentication System: Secure login, registration, and password management
Dashboard: Overview of key metrics and statistics
Profile Management: Employee self-service portal
Reporting: Generate various reports (attendance, performance, etc.)
Search & Filter: Quick search and advanced filtering capabilities
🛠️ Technology Stack

Backend

Python 3.8+
Django 4.x - High-level Python web framework
Django REST Framework - For building REST APIs
PostgreSQL/MySQL - Database (configurable)
Frontend

HTML5, CSS3, JavaScript
Bootstrap 5 - Responsive design framework
jQuery - JavaScript library for DOM manipulation
Additional Packages

Pillow - Image processing for profile pictures
Django Crispy Forms - Form styling
Django Filter - Advanced filtering
ReportLab - PDF report generation
📋 Prerequisites

Before you begin, ensure you have installed:

Python 3.8 or higher
pip (Python package manager)
Virtualenv (recommended)
Git
Database (PostgreSQL/MySQL/SQLite)
🚀 Installation & Setup

1. Clone the Repository

bash
git clone https://github.com/yourusername/Office-Employee-Management-System.git
cd Office-Employee-Management-System
2. Create Virtual Environment

bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
3. Install Dependencies

bash
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the project root:

env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/employee_db
ALLOWED_HOSTS=localhost,127.0.0.1
5. Database Setup

bash
python manage.py makemigrations
python manage.py migrate
6. Create Superuser

bash
python manage.py createsuperuser
7. Load Sample Data (Optional)

bash
python manage.py loaddata fixtures/sample_data.json
8. Run Development Server

bash
python manage.py runserver
Visit http://localhost:8000 in your browser.
