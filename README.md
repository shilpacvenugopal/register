# User Management System

## Installation

Follow these steps to set up the User Management System project on your local machine.

### Prerequisites

- [Python](https://www.python.org/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)

### Steps

1. **Clone the Repository:**

   ```bash
git clone https://github.com/shilpacvenugopal/register.git 
cd registeruser
   ```

2. **Create a Virtual Environment:**

   ```bash
   virtualenv venv
   ```

3. **Activate the Virtual Environment:**

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser (Admin User):**

   ```bash
   python manage.py createsuperuser
   ```


7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   The project will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

8. **Access the  Interface:**

   Visit [http://127.0.0.1:8000/dashboard/register/](http://127.0.0.1:8000/dashboard/register/) and register a user. After successfull registeration it will redirect to login page
   [http://127.0.0.1:8000/dashboard/login/](http://127.0.0.1:8000/dashboard/login/)

   
  - username: staff1@gmal.com
  - password - 123456

  - username: editor@gmail.com
  - password:123456

## Technology Stack

- **Backend:** Python – Django
- **Frontend:** Django Templates

