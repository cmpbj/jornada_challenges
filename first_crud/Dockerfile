# Specifies the base image for the container
FROM python:3.12

# Installs poetry
RUN pip install poetry

# Copies files from the jornada_challenges/first_crud directory to the container
COPY . /src

# Set the working directory for subsequent commands in the Dockerfile
WORKDIR /src

# Install all dependencies defined in the pyproject.toml
RUN poetry install --no-root

# Indicates that the application will run on port 8501
EXPOSE 8501

# Specifies the command to run whe the container starts
ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8501"]