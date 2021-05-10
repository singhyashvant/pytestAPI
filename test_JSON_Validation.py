from jsonschema import validate
import requests


def test_json_schema_validation(base_url):
    schema = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$ref": "#/definitions/Welcome9",
    "definitions": {
        "Welcome9": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "integer"
                },
                "meta": {
                    "$ref": "#/definitions/Meta"
                },
                "data": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Datum"
                    }
                }
            },
            "required": [
                "code",
                "data",
                "meta"
            ],
            "title": "Welcome9"
        },
        "Datum": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                },
                "gender": {
                    "$ref": "#/definitions/Gender"
                },
                "status": {
                    "$ref": "#/definitions/Status"
                },
                "created_at": {
                    "type": "string",
                    "format": "date-time"
                },
                "updated_at": {
                    "type": "string",
                    "format": "date-time"
                }
            },
            "required": [
                "created_at",
                "email",
                "gender",
                "id",
                "name",
                "status",
                "updated_at"
            ],
            "title": "Datum"
        },
        "Meta": {
            "type": "object",
            "properties": {
                "pagination": {
                    "$ref": "#/definitions/Pagination"
                }
            },
            "required": [
                "pagination"
            ],
            "title": "Meta"
        },
        "Pagination": {
            "type": "object",
            "properties": {
                "total": {
                    "type": "integer"
                },
                "pages": {
                    "type": "integer"
                },
                "page": {
                    "type": "integer"
                },
                "limit": {
                    "type": "integer"
                }
            },
            "required": [
                "limit",
                "page",
                "pages",
                "total"
            ],
            "title": "Pagination"
        },
        "Gender": {
            "type": "string",
            "enum": [
                "Male",
                "Female"
            ],
            "title": "Gender"
        },
        "Status": {
            "type": "string",
            "enum": [
                "Active",
                "Inactive"
            ],
            "title": "Status"
        }
    }


    }
    url = base_url + '/public-api/users'
    data = requests.get(url).json()
    validate(data, schema)
