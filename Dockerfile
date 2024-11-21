FROM python:3.11


WORKDIR /src
RUN pip install -r requirements.txt

# Copy all source code
COPY . .

# Run the server on port 80
CMD ["fastapi", "run", "main.py"]