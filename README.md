
## HRConnect
HRConnect is a user-friendly Django app for efficient HR management. It simplifies CRUD operations for employee records, supports basic data storage, leave management, and generates essential reports. Streamline HR processes effortlessly with HRConnect..

## Features

- **Employee Management**: Perform CRUD operations on employee records, including creating new profiles, updating existing information, and managing employee details.

- **Data Storage**: Store and manage basic employee information such as personal details, employment history, and contact information.

- **Leave Management**: Track and manage employee leave requests, including approving or rejecting requests and maintaining a record of leave history.

## Installation

1. Clone the repository:
`https://github.com/Adil-A-Rahman/HRConnect/`

2. Install the required dependencies:
`pip install -r requirements.txt`

3. Configure the database settings in `settings.py`.
4. Make a migration folder
`python manage.py makemigrations api`
5. Apply database migrations:
`python manage.py migrate`

6. Start the development server:
`python manage.py runserver`

7. Access the application at [http://localhost:8000](http://localhost:8000).
8. Make an admin using command
`python manage.py createsuperuser`
9. Access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin).

## Usage

1. Register as an HR administrator in the application.

2. Log in with your credentials and start managing employee records.

3. Create, update, or delete employee profiles as needed.

4. Track and manage employee leave requests using the provided functionalities.

## License

This project is licensed under the [MIT License](LICENSE).
