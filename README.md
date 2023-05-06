# Healthcare Django Project

This is a Django project for managing healthcare-related entities such as clinics, doctors, patients, appointments, and medical records.

## Features

- Clinic management: Create, update, and delete clinics. Each clinic has its own set of doctors and patients associated with it.
- Doctor management: Manage doctors, their specialties, and availability. Assign doctors to clinics.
- Patient management: Register patients and maintain their demographic information.
- Appointment scheduling: Schedule appointments between doctors and patients.
- Medical record management: Record and retrieve medical information such as diagnoses, treatments, and prescriptions for patients.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nabeelahmdd/healthcare.git
```
2. Create a virtual environment and activate it:
```bash
cd healthcare
python3 -m venv env
source env/bin/activate
```
3. Install the project dependencies:
```bash
pip install -r requirements.txt
```
4. Set up the database:
```bash
python3 manage.py migrate
```
5. Start the development server:
```bash
python3 manage.py runserver
```
6. Access the application at http://localhost:8000.

## Usage
Create clinics, doctors, and patients through the provided Django admin interface (/admin).
Use the provided API endpoints to perform CRUD operations on clinics, doctors, patients, appointments, and medical records.
Authenticate requests using the provided authentication mechanism (e.g., token-based authentication, OAuth, etc.).
API Endpoints
Clinics

/api/clinics/ (GET, POST): List all clinics or create a new clinic.
/api/clinics/<clinic_id>/ (GET, PUT, PATCH, DELETE): Retrieve, update, or delete a specific clinic.
Doctors

/api/doctors/ (GET, POST): List all doctors or create a new doctor.
/api/doctors/<doctor_id>/ (GET, PUT, PATCH, DELETE): Retrieve, update, or delete a specific doctor.
Patients

/api/patients/ (GET, POST): List all patients or create a new patient.
/api/patients/<patient_id>/ (GET, PUT, PATCH, DELETE): Retrieve, update, or delete a specific patient.
Appointments

/api/appointments/ (GET, POST): List all appointments or create a new appointment.
/api/appointments/<appointment_id>/ (GET, PUT, PATCH, DELETE): Retrieve, update, or delete a specific appointment.
Medical Records

/api/medical-records/ (GET, POST): List all medical records or create a new medical record.
/api/medical-records/<record_id>/ (GET, PUT, PATCH, DELETE): Retrieve, update, or delete a specific medical record.
## License
This project is licensed under the MIT License.
