# Example CI/CD Project - Brief C18 / C19

This project demonstrates a complete automated integration (CI) and delivery (CD) pipeline.

## 🛠 C18: Automated Testing
- **CI Tool**: GitHub Actions (`.github/workflows/ci-cd-brief.yml`).
- **Chain of Execution**:
    1. **Environment**: Setup Python 3.11.
    2. **Dependencies**: `pip install -r requirements.txt`.
    3. **Execution**: Automatic triggering on `push` to `main` and `develop`.
- **Quality Indicators**:
    - `pytest --cov`: Generates a coverage report (metrics).
    - `upload-artifact`: Stores test results for traceability.
- **Versioning**: All pipeline configuration is versioned in Git.

## 🚀 C19: Continuous Delivery
- **Packaging**:
    - **Docker Implementation**: `Dockerfile` is used to create a reproducible artifact.
    - **Validation**: The pipeline builds the image and runs a health check to ensure zero errors during packaging.
- **Delivery Steps**:
    - **Artifact Generation**: Container image is built.
    - **Automatic Release**: On `push` to `main`, a GitHub Release is automatically created (versioned artifact publication).
- **Traceability**: GitHub Actions provides full logs, execution history, and status tracking.

## 🐳 Docker Usage (C19: Packaging)

To package and run the application locally as an artifact:

### 1. Build the image
```bash
docker build -t fastapi-app:latest .
```

### 2. Run the container
```bash
# Basic run mapping port 8000 on host to 80 in container
docker run -d --name my-fastapi-app -p 8000:80 fastapi-app:latest

# Run with environment variables (using your .env file)
docker run -d --name my-fastapi-app -p 8000:80 --env-file .env fastapi-app:latest
```

### 3. Verify
Access the app at `http://localhost:8000` or check the logs:
```bash
docker logs -f my-fastapi-app
```
