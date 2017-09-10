# Companies

## Get Companies List

```json--payload
Payload:
```

```json--response
Response:

[
    {
        "company_id": 1,
        "company_name": "entropy technology"
    },
    {
        "company_id": 2,
        "company_name": "aipin job technology"
    }
]
```

This endpoint returns a list of company info the user has access to.

### HTTP Request

`GET http://localhost:8000/api/companies/`

## Create New Company

```json--payload
Payload:

{
    "company_name": "aipin job technology",
    "creator_id": 1
}
```

```json--response
Response:

{
    "company_id": 1
}
```

This endpoint creates a new company. The login user will be the creator and admin of the new company.

### HTTP Request

`POST http://localhost:8000/api/companies/`

### Parameters

Parameter    | Type   | Description
------------ | ------ | ------------------------------
company_name | string | The name of the company.
creator_id   | int    | The creator_id of the company.

## Get Company Detail

```json--payload
Payload:
```

```json--response
Response:

{
    "company_id": 1,
    "company_name": "aipin job technology"
}
```

This endpoint returns company detail information.

### HTTP Request

`GET http://localhost:8000/api/companies/<company_id>`

## Delete Company

```json--payload
Payload:
```

```json--response
Response:
```

This endpoint deletes company.

### HTTP Request

`DELETE http://localhost:8000/api/companies/<company_id>`

# Stages

## Get Stages List

```json--payload
Payload:
```

```json--response
Response:

[
    {
        "stage_id": 1,
        "stage_name": "Phone Screen Round 1",
        "stage_type": "Phone Screen",
        "order": 1
    },
    {
        "stage_id": 2,
        "stage_name": "Phone Screen Round 2",
        "stage_type": "Phone Screen",
        "order": 2
    },
    {
        "stage_id": 3,
        "stage_name": "Offer",
        "stage_type": "Offer",
        "order": 3
    }
]
```

This endpoints returns all recruiting stages for the company.

### HTTP Request

`GET http://localhost:8000/api/companies/<company_id>/stages/`

## Modify Stages Order

```json--payload
Payload:

{
    "orders": [
        {
            "stage_id": 1,
            "order": 1
        },
        {
            "stage_id": 2,
            "order": 2
        },
        {
            "stage_id": 3,
            "order": 3
        }
    ]
}
```

```json--response
Response:

[
    {
        "stage_id": 1,
        "order": 1
    },
    {
        "stage_id": 2,
        "order": 2
    },
    {
        "stage_id": 3,
        "order": 3
    }
]
```

This endpoints modifies the order of all stages under the company.

### HTTP Request

`PUT http://localhost:8000/api/companies/<company_id>/stages/orders`

### Parameters

Parameter       | Type | Description
--------------- | ---- | -----------------------------------------------------------------------------
orders          | list | The list of stage orders. The list must include all stages under the company.
orders.stage_id | int  | The id for single stage.
orders.order    | int  | The order of the that stage. It starts from 1.

## Create New Stage

```json--payload
Payload:

{
    "stage_name": "Phone Screen Round 1",
    "stage_type": 2
}
```

```json--response
Response:

{
    "stage_id": 1
}
```

This endpoint creates new stage under the company. The order filed will be automatic populated for the new stage.

### HTTP Request

`POST http://localhost:8000/api/companies/<company_id>/stages/`

### Parameters

Parameter  | Type   | Description
---------- | ------ | -------------------------------------------------------------------------------------------
stage_name | string | The name of the recruiting stage.
stage_type | int    | The type of the recruiting stage. Please check `stage` model for the int to string mapping.

## Modify Stage

```json--payload
Payload:

{
    "stage_name": "Phone Screen Round 1",
    "stage_type": 1
}
```

```json--response
Response:

{
    "stage_id": 1
}
```

This endpoints modifies stage name and stage type.

### HTTP Request

`PUT http://localhost:8000/api/companies/<company_id>/stages/<stage_id>`

### Parameters

Parameter  | Type   | Description
---------- | ------ | -------------------------------------------------------------------------------------------
stage_name | string | The name of the recruiting stage.
stage_type | int    | The type of the recruiting stage. Please check `stage` model for the int to string mapping.

## Delete Stage

```json--payload
Payload:
```

```json--response
Response:
```

This endpoints deletes the stage under the company.

### HTTP Request

`DELETE http://localhost:8000/api/companies/<company_id>/stages/<stage_id>`
