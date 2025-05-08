# User Guide

## Navigation
This is an API-based application with no frontend UI. Users interact through tools like Postman, curl, or frontend integration.

## Example Endpoints
- `GET /api/items/` - View all items
- `POST /api/items/` - Create an item
- `PUT /api/items/{id}/` - Update an item
- `DELETE /api/items/{id}/` - Delete an item

## Sample JSON Payload
```json
{
  "name": "Notebook",
  "description": "College ruled",
  "price": "3.99"
}
```

## Troubleshooting
- **403 Forbidden**: Ensure you're logged in or authenticated
- **500 Error**: Check the request format and server logs
