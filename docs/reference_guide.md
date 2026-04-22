# Requests Library Reference Guide

This document provides a quick reference for using the Python `requests` library in this weather CLI project.

## Overview

**Requests** is a simple, elegant, and widely-used Python HTTP library that makes sending HTTP requests incredibly easy. It supports features like connection pooling, authentication, and automatic content decompression.

- **Library ID**: `/websites/requests_readthedocs_io_en`
- **Source Reputation**: High
- **Documentation**: [requests.readthedocs.io](https://requests.readthedocs.io/)

## Making GET Requests

### Basic GET Request

The most common HTTP verb for fetching data from APIs:

```python
import requests

# Make a GET request to an API endpoint
r = requests.get('https://api.example.com/data')

# Check if the request was successful
if r.status_code == requests.codes.ok:
    print("Request successful!")
else:
    print(f"Request failed with status code: {r.status_code}")
```

### Accessing Response Data

```python
# Status code
print(r.status_code)  # 200

# Headers
print(r.headers['content-type'])  # 'application/json; charset=utf-8'

# Encoding
print(r.encoding)  # 'utf-8'

# Raw text content
print(r.text)  # '{"key": "value"}'
```

## Working with JSON Responses

### Parsing JSON Data

The `requests` library makes it easy to work with JSON APIs:

```python
import requests

# Fetch data from a JSON API
r = requests.get('https://api.github.com/events')

# Parse JSON response automatically
data = r.json()

# Access the parsed data
print(data)  # Returns a Python dictionary or list
```

### Complete Example with Error Handling

```python
import requests

# Example GET request to GitHub API
r = requests.get('https://api.github.com/repos/psf/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')

# Check if the request was successful
if r.status_code == requests.codes.ok:
    # Print the content type
    print(r.headers['content-type'])
    
    # Parse the JSON response
    commit_data = r.json()
    
    # Access and print specific data
    print(commit_data.keys())
    print(commit_data['committer'])
    print(commit_data['message'])
else:
    print(f"Request failed with status code: {r.status_code}")
```

## Error Handling

### JSON Decode Errors

Be aware of potential exceptions when parsing JSON:

```python
import requests

try:
    r = requests.get('https://api.example.com/data')
    data = r.json()
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON response")
```

### HTTP Status Validation

Always check the status code or use `raise_for_status()`:

```python
import requests

r = requests.get('https://api.example.com/data')

# Option 1: Manual check
if r.status_code == 200:
    data = r.json()
else:
    print(f"Error: {r.status_code}")

# Option 2: Raise exception for bad status
r.raise_for_status()  # Raises HTTPError for 4xx/5xx responses
```

## Best Practices for Weather API Integration

### 1. Check Status Codes

Always verify the response was successful before processing:

```python
if r.status_code == requests.codes.ok:
    weather_data = r.json()
```

### 2. Handle Exceptions

Wrap API calls in try-except blocks:

```python
try:
    r = requests.get(api_url)
    r.raise_for_status()
    data = r.json()
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
```

### 3. Validate JSON Content

Successful JSON decoding doesn't guarantee a successful HTTP response:

```python
r = requests.get(api_url)
if r.status_code == 200:
    try:
        data = r.json()
    except requests.exceptions.JSONDecodeError:
        print("Invalid JSON response")
```

## Common HTTP Status Codes

- **200 OK**: Request succeeded
- **204 No Content**: Request succeeded but no content returned
- **400 Bad Request**: Invalid request parameters
- **401 Unauthorized**: Authentication required
- **404 Not Found**: Resource not found
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Server error

## Additional Resources

- [Requests Documentation](https://requests.readthedocs.io/en/latest/)
- [Requests Quickstart Guide](https://requests.readthedocs.io/en/latest/user/quickstart)
- [Advanced Usage](https://requests.readthedocs.io/en/latest/user/advanced)

---

*This reference guide is based on the official Requests library documentation and Context7 documentation snippets.*
