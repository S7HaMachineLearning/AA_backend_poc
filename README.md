




pip install fastapi "uvicorn[standard]"


# Run the server
`python -m uvicorn main:app`

# Run local server, but accessible over network
`python -m uvicorn main:app --host 0.0.0.0 --port 8000`