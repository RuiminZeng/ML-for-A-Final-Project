# base image
FROM python:3.7.3-stretch

# Set the working directory
WORKDIR /app

# Copy source code to working directory
COPY  app.py /app/
COPY  requirements.txt /app/
COPY  insurance.py /app/
COPY  insurance_prediction.joblib /app/
RUN   mkdir  /app/templates/
COPY  templates/template.html /app/templates/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run app.py at container launch
CMD ["python", "app.py"]
