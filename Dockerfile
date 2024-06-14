
# Starting image
FROM python:3.12

# Opening port
EXPOSE 5000

# Setting working directory
WORKDIR /usr/src/app

# Copy files over
COPY . .

# Install requirements
RUN pip install -r requirements.txt

# Run the flask server
CMD ["python3","app.py"]
