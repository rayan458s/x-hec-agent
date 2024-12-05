FROM python:3.11


WORKDIR /src
# Copy all source code
COPY . .

RUN pip install -r requirements.txt
RUN pip install "fastapi[standard]"

# Run the server on port 80
CMD ["fastapi", "run", "main.py"]