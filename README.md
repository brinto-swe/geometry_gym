# 🏋️ Gym Management System (Django REST Framework + React)

A full-stack Gym Management System built with **Django REST Framework (DRF)** for the backend and **React (Vercel)** for the frontend.  
The system supports three roles — **Admin, Staff, and Member** — with role-based access control, email verification, and JWT authentication.  
Live Link:https://vercel.com/brintos-projects-17ed2514/geometry-gym/ALric1p6BWet62LhyzRoCohFYXQi
---

## ✨ Features

- 🔑 **Authentication & Authorization**
  - JWT authentication with refresh & access tokens
  - Email verification before login
  - Role-based access (Admin, Staff, Member)

- 🏆 **Membership & Subscriptions**
  - Create and manage membership plans
  - Subscription tracking with start/end dates

- 📅 **Fitness Classes & Scheduling**
  - Staff can create and update classes
  - Members can view and book available classes

- 📌 **Bookings & Attendance**
  - Members book classes
  - Staff/Admin track attendance

- 💳 **Payments**
  - Record and track payments
  - Future integration with payment gateways

- ⭐ **Feedback & Reviews**
  - Members submit reviews
  - Admin/Staff can view feedback

- 📊 **Reports & Analytics**
  - Membership growth
  - Class participation
  - Revenue reports

- ☁️ **Media Storage**
  - Profile pictures, class images stored on **Cloudinary**

- ⚙️ **Deployment Ready**
  - Backend: Django REST Framework
  - DB: SQLite (dev) → PostgreSQL on Supabase (prod)
  - Static files: WhiteNoise
  - Frontend: React (Vercel)

---

## 🛠️ Tech Stack

- **Backend**: Django, Django REST Framework  
- **Auth**: Simple JWT, Email Verification  
- **Database**: SQLite (development), PostgreSQL (Supabase - production)  
- **Storage**: Cloudinary for media  
- **Docs**: Swagger / OpenAPI  
- **Frontend**: React (Vercel deployment)  
- **Deployment**: Django + WhiteNoise, Supabase, Vercel  

---

## 🚀 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/gym-management-system.git
cd gym-management-system
```
### 2. Create virtual environment & install dependencies
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

```
### 3. Setup environment variables
Create a .env file in the root:
```ini
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=sqlite:///db.sqlite3
CLOUDINARY_URL=cloudinary://<api_key>:<api_secret>@<cloud_name>
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_email_password
```
### 4. Run migrations
```bash
python manage.py migrate
```
### 5. Create superuser
```bash
python manage.py createsuperuser
```
### 6. Run the server
```bash
python manage.py runserver
```

## 📖 API Endpoints
#### 🔑 Authentication
- POST /api/register/ – Register new user (with email verification)

- GET /api/activate/<uid>/<token>/ – Activate account

- POST /api/token/ – Obtain JWT access/refresh tokens

- POST /api/token/refresh/ – Refresh token

#### 👥 Users & Roles
- GET /api/users/ – List users (Admin only)

- GET /api/users/<id>/ – Retrieve user

- PATCH /api/users/<id>/ – Update user

- DELETE /api/users/<id>/ – Delete user

#### 🏆 Memberships
- GET /api/memberships/ – List memberships

- POST /api/memberships/ – Create membership (Staff/Admin)

- GET /api/memberships/<id>/ – Retrieve membership

- PATCH /api/memberships/<id>/ – Update membership

- DELETE /api/memberships/<id>/ – Delete membership

#### 📅 Classes & Scheduling

- GET /api/classes/ – List classes

- POST /api/classes/ – Create class (Staff/Admin)

- GET /api/classes/<id>/ – Retrieve class

- PATCH /api/classes/<id>/ – Update class

- DELETE /api/classes/<id>/ – Delete class

#### 📌 Bookings & Attendance

- POST /api/bookings/ – Book a class

- GET /api/bookings/ – View bookings

- PATCH /api/bookings/<id>/ – Update booking

- DELETE /api/bookings/<id>/ – Cancel booking

- POST /api/attendance/ – Mark attendance (Staff/Admin)

#### 💳 Payments

- GET /api/payments/ – List payments

- POST /api/payments/ – Record payment

- GET /api/payments/<id>/ – Retrieve payment

#### ⭐ Feedback & Reviews

- GET /api/feedback/ – List feedback

- POST /api/feedback/ – Submit feedback

- GET /api/feedback/<id>/ – Retrieve feedback

#### 📊 Reports & Analytics

- GET /api/reports/memberships/ – Membership stats

- GET /api/reports/revenue/ – Revenue stats

- GET /api/reports/classes/ – Class participation
