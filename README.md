# DCRM - Django Customer Relationship Management

## Description

A simple Django-based CRM (Customer Relationship Management) application for managing customer records. This web application allows users to register accounts, log in, and perform CRUD (Create, Read, Update, Delete) operations on customer records. Each record includes details such as name, email, phone, address, city, state, and zipcode.

## Features

- **User Authentication**: Register new accounts, login, and logout functionality
- **Customer Records Management**:
  - View all customer records on the home page
  - Add new customer records
  - View individual customer record details
  - Update existing customer records
  - Delete customer records
- **Responsive Web Interface**: Built with Django templates and Bootstrap for a clean, user-friendly experience and minimal design.
- **Security**: User authentication required for sensitive operations

## Requirements

- Python 3.x
- Django 6.0.4
- mysql-connector-python 9.7.0
- mysql 0.0.3





## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd dcrm
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/`

## Usage

- **Registration**: Create a new account using the registration form
- **Login**: Use your credentials to log in
- **Home Page**: View all customer records (requires login)
- **Add Record**: Click "Add Record" to create a new customer entry
- **View Record**: Click on a record to view its details
- **Update Record**: Edit existing customer information
- **Delete Record**: Remove customer records as needed
- **Logout**: Securely log out of your account



## Contributing

Contributions are welcome! If you'd like to contribute to this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Support

If you encounter any issues or have questions about this project, please open an issue on the GitHub repository.
