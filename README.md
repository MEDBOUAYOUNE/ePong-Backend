# 🛡️ ePong <ft_transcendence> Backend API with PostgreSQL

This project is a 1337-42NETWORK project <ft_transcendence>-Backend.  built with Django REST Framework and PostgreSQL. It supports user authentication, OAuth2 login, JWT token management, 2FA, user profile management, and a friendship system with invitations.

## 📦 Features

### Authentication & JWT
- **POST /signup/** – Register a new user
- **POST /login/** – Log in and receive access/refresh tokens
- **POST /logout/** – Invalidate refresh token
- **POST /token/refresh** – Refresh JWT access token

### OAuth2 with Intra 42
- **GET /oauth2/authorize** – Redirect to 42 API login
- **GET /oauth2/callback** – Handle 42 API login callback

### User Management
- **GET /users/** – List all users
- **GET /user/** – Get current user
- **GET /user/<int:id>** – Get user by ID
- **GET /user/<str:username>** – Get user by username
- **GET /user/search/** – Search users
- **PUT /user/update/** – Update user profile fields
- **PUT /user/update/password** – Change password
- **DELETE /delete-profile/** – Delete user account

### Friends & Invitations
- **POST /invitation/send/<int:id>** – Send friend invitation
- **POST /invitation/accept/<int:id>** – Accept friend request
- **POST /invitation/reject/<int:id>** – Reject friend request
- **GET /invitation/list** – List pending invitations
- **GET /friend/list** – List all friends
- **GET /user/relation/<int:id>** – Check relation with a user
- **DELETE /friend/remove/<int:id>** – Remove a friend

### Two-Factor Authentication (2FA)
- **POST /2fa/enable** – Enable 2FA
- **POST /2fa/disable** – Disable 2FA
- **POST /2fa/verify** – Verify 2FA token

## ⚙️ Tech Stack
- **Framework**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT + OAuth2 (Intra 42)
- **Security**: Two-Factor Authentication (2FA)

## 🔑 Environment Variables
To run this project, set up the following environment variables:

```
# Django Secret Key
SECRET_KEY=your_django_secret_key

# JWT Secrets
ACCESS_SECRET=your_access_secret
REFRESH_SECRET=your_refresh_secret

# Intra 42 OAuth2 Credentials
INTRA_UID=your_intra42_client_uid
INTRA_SECRET=your_intra42_client_secret

# PostgreSQL Database Configuration
DB_NAME=postgres
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost         # Or your DB host
DB_PORT=5432              # Default PostgreSQL port
```

## 🚀 Getting Started
Follow these steps to set up and run the project locally:

1. Clone the repository:
   ```bash
   git clone ePong-Backend
   cd ePong-Backend
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```