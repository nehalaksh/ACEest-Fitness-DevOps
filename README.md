# ACEest Fitness & Gym

ACEest Fitness & Gym is a lightweight Flask application that lets users explore different fitness programs, review weekly workout plans, and view daily nutrition guidance. The app includes both a browser interface and JSON API endpoints for program data.

## Features

- Select from multiple training programs
- View weekly workout schedules and nutrition plans
- Browse a simple, responsive fitness landing page
- Access program data through API endpoints
- Health check endpoint for service monitoring

## Project Structure

- `app.py` - Flask app and route definitions
- `templates/index.html` - user-facing fitness dashboard
- `static/style.css` - application styling
- `tests/test_app.py` - automated tests covering home page, API, and health checks
- `Dockerfile` - container configuration
- `Jenkinsfile` - CI pipeline configuration

## Available Programs

- Fat Loss (FL)
- Muscle Gain (MG)
- Beginner (BG)

## Requirements

- Python 3.10+
- Flask 3.1+
- Gunicorn 23+

## Local Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open the app in a browser:

   ```text
   http://localhost:5000
   ```

## Docker

Build the container image:

```bash
docker build -t aceest-fitness .
```

Run the app in a container:

```bash
docker run -p 5000:5000 aceest-fitness
```

## API Endpoints

- `GET /` - Home page with the program selection form
- `GET /health` - Health status endpoint
- `GET /api/programs` - Lists all available fitness programs
- `GET /api/programs/<program_name>` - Returns details for a single program


```

## Testing

Run the test suite:

```bash
pytest
```

## License

This project does not currently include a dedicated license file, so it should be treated as internal or demo usage unless otherwise specified.
