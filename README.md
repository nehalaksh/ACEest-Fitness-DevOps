# ACEest Fitness & Gym

ACEest Fitness & Gym is a Flask web application for browsing workout schedules and nutrition plans for different training goals. It provides a browser-based program selector and a JSON API for program information and service health.

## Features

- Browse Fat Loss, Muscle Gain, and Beginner programs
- View weekly workout schedules and daily nutrition guidance
- Retrieve program data through a JSON API
- Check service status with a health endpoint

## Requirements

- Python 3.12 or newer
- pip
- Docker (optional, for container builds and runs)

The CI configurations currently use Python 3.15. The Docker image is based on Python 3.12.

## Local Setup and Execution

From the repository root, create and activate a virtual environment. In Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install application and development dependencies:

```shell
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Start the development server:

```shell
python app.py
```

Open [http://localhost:5000](http://localhost:5000). Stop the server with `Ctrl+C`.

## Manual Tests

With the virtual environment active and development dependencies installed, run the full test suite from the repository root:

```shell
python -m pytest -v
```

The tests use Flask's built-in test client and do not require the web server to be running. To run a specific test module:

```shell
python -m pytest -v tests/test_app.py
```

Optional checks matching the CI validation steps:

```shell
python -m compileall -q app.py tests
ruff check app.py tests
```

## API

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Web interface and program selector |
| `GET` | `/health` | Returns `{"status":"healthy"}` while the service is available |
| `GET` | `/api/programs` | Returns all available programs |
| `GET` | `/api/programs/<program_name>` | Returns a named program or a 404 response |


## Docker

Build and run the production runtime image:

```shell
docker build --target runtime -t aceest-fitness:latest .
docker run --rm -p 5000:5000 aceest-fitness:latest
```

To run the test suite inside the Docker test image:

```shell
docker build --target test -t aceest-fitness:test .
docker run --rm aceest-fitness:test
```

## Continuous Integration

The project has two CI integrations that validate changes and build Docker images:

- **GitHub Actions** — `.github/workflows/main.yml` runs on pushes and pull requests. It checks out the repository, sets up Python 3.15, installs `requirements-dev.txt`, compiles the app and tests, runs Ruff and pytest, then builds and runs the Docker test image and builds the runtime image.
- **Jenkins** — `Jenkinsfile` defines a declarative pipeline that checks out the configured SCM source, checks syntax, installs application dependencies, runs Flake8 and pytest, and builds the Docker image. The pipeline uses Windows `bat` steps and Python 3.15; Jenkins agents therefore need those tools available. It reports success or failure in the post-build step.

## Project Structure

- `app.py` - Flask application, program data, and routes
- `templates/` - HTML template for the web interface
- `static/` - Stylesheets and static assets
- `tests/` - Automated application tests
- `requirements.txt` - Runtime dependencies
- `requirements-dev.txt` - Runtime and development/test dependencies
- `Dockerfile` - Test and runtime container targets
- `Jenkinsfile` - Jenkins pipeline
- `.github/workflows/main.yml` - GitHub Actions workflow

## License

No license file is currently included in this repository as its test/demo project .
