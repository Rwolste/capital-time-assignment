
# Capital Time API

The Capital Time API is a lightweight Flask-based service that returns the current local time and UTC offset for a specified capital city. It’s designed for demonstration purposes and includes simple token-based authentication.

## Base URL

```
http://34.41.135.123:5000
```

## Authentication

Requests must include an `Authorization` header with a valid token. The current token is:

```
mysecrettoken123
```

## Endpoint

### GET /api/time

This endpoint returns the current local time and UTC offset for the capital city provided in the query parameters.

### Query Parameters

- `capital` (string, required): The name of the capital city. This parameter is case-sensitive.

### Request Example

Using `curl`:

```
curl -X GET "http://34.41.135.123:5000/api/time?capital=London" \
     -H "Authorization: mysecrettoken123"
```

### Success Response

Returns a JSON object with the requested capital’s current local time and UTC offset.

```json
{
  "capital": "London",
  "local_time": "2025-04-20 18:15:23",
  "utc_offset": "UTC+1"
}
```

### Error Responses

**Missing Token**
```json
{
  "error": "Unauthorized access. Valid token required."
}
```

**Invalid Capital**
```json
{
  "error": "Capital 'Atlantis' not found in database."
}
```

**Missing Parameter**
```json
{
  "error": "Missing 'capital' parameter."
}
```

## Supported Capital Cities

The following are some of the supported capital cities:

- Washington
- London
- Paris
- Tokyo
- Delhi
- Canberra
- Ottawa
- Brasilia
- Beijing
- Moscow
- Berlin
- Rome
- Cairo
- Seoul
- Bangkok
- Madrid
- Tehran
- Jakarta
- and others...

## Notes

- This API is intended for academic or testing purposes.
- All time calculations are based on static IANA timezone mappings.
- For any request to succeed, the `Authorization` token must be correct.
