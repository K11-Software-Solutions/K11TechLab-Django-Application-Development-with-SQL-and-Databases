# Django First Project with Docker

This project demonstrates how to set up a Django project with Docker support for containerized development and deployment.

## How the App is Built

This Django application is structured for both local and containerized (Docker) development. The project was created using the following steps:

1. **Django Project Initialization:**
	- The Django project was started with:
	  ```sh
	  django-admin startproject firstproject
	  ```
	- The main app was created with:
	  ```sh
	  python manage.py startapp firstapp
	  ```
	- All core settings and URLs are managed in the `firstproject/` directory, while application logic resides in `firstapp/`.

2. **Requirements and Configuration:**
	- All Python dependencies are listed in `requirements.txt` for easy installation.
	- Environment variables are managed via a `.env` file (see `.env.example`).

3. **Docker Integration:**
	- The `Dockerfile` defines how to build a container image for the Django app, including installing dependencies and running migrations.
	- The app can be built and run in a container using standard Docker commands, making it portable and cloud-ready.

4. **Cloud Deployment Ready:**
	- Scripts and environment variables are included for IBM Cloud Code Engine deployment, but the app can be deployed to any Docker-compatible environment.

This structure allows for easy local development, testing, and seamless transition to production or cloud environments.

## Structure
- `manage.py`: Django management script
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker configuration
- `firstapp/`: Main Django app
- `firstproject/`: Project settings

## Setup
1. Create a virtual environment: `python -m venv djangoenv`
2. Install dependencies: `pip install -r requirements.txt`
3. Build and run Docker container: `docker build -t django-app .` and `docker run -p 8000:8000 django-app`
4. Run locally: `python manage.py runserver`

## Notes
- Includes scripts for IBM Cloud deployment.
- Uses SQLite3 by default.

## Detailed Explanation: App Setup and Docker

### App Setup
1. **Clone the repository** and navigate to this project folder.
2. **Create a virtual environment** (recommended for local development):
	```sh
	python -m venv djangoenv
	```
3. **Activate the virtual environment**:
	- On Windows:
	  ```sh
	  djangoenv\Scripts\activate
	  ```
	- On macOS/Linux:
	  ```sh
	  source djangoenv/bin/activate
	  ```
4. **Install dependencies**:
	```sh
	pip install -r requirements.txt
	```
5. **Apply migrations** to set up the database:
	```sh
	python manage.py makemigrations
	python manage.py migrate
	```
6. **Run the development server**:
	```sh
	python manage.py runserver
	```
	Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

### Docker Usage
This project includes a `Dockerfile` for containerized development and deployment.

**Build the Docker image:**
```sh
docker build -t django-app .
```

**Run the Docker container:**
```sh
docker run -p 8000:8000 django-app
```
This will start the Django app inside a container, accessible at [http://localhost:8000/](http://localhost:8000/).

**Environment Variables:**
You can use a `.env` file to provide environment variables (see `.env.example` for required keys). For production, set `DEBUG=False` and configure allowed hosts and database settings as needed.

**IBM Cloud Deployment:**
Scripts and environment variables are provided for deploying to IBM Cloud Code Engine. See the included `.env.example` and deployment scripts for details.

### Testing
- Run Django tests with:
  ```sh
  python manage.py test
  ```
- Or use pytest (after installing `pytest` and `pytest-django`):
  ```sh
  pytest
  ```