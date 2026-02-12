# Checklist App ("check")

A robust FastAPI application implementing a simple checklist.

## Application

The `check` app provides REST endpoints to manage items.

### Endpoints

- `GET /` - Welcome message
- `GET /items/` - List all items
- `POST /items/` - Create a new item
- `PUT /items/{item_id}` - Update item status

## Testing

A Selenium-based skill (`test_selenium.py`) is included to verify functionality.

### Running Tests

1. Ensure Selenium and Chrome/ChromeDriver are installed.
2. Run the server: `uvicorn main:app --reload`
3. Execute the test script: `python3 test_selenium.py`

## Deployment

Clone repository and run with Uvicorn.
