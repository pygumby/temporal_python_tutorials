# temporal_python_tutorials
Me following along various Temporal tutorials in Python

1. Build a Temporal Application from scratch in Python
    - [Source code](hello_temporal)
    - [Tutorial](https://learn.temporal.io/getting_started/python/hello_world_in_python/)
    - Instructions:
        ```
        $ cd hello_temporal
        $ pip install -r requirements.txt

        # Run tests
        $ pytest

        # Run workflow
        $ temporal server start-dev
        $ python run_worker.py
        $ python run_workflow.py
        ```
2. Build a trip booking application in Python
    - [Source code](trip_booking)
    - [Tutorial](https://learn.temporal.io/tutorials/python/trip-booking-app/)
    - Instructions:
        ```
        $ cd trip_booking
        $ pip install -r requirements.txt

        # Run workflow
        $ temporal server start-dev
        $ python run_worker.py
        $ python starter.py
        $ curl -X POST http://localhost:5000/book \  # Succeeding call
            -H "Content-Type: application/json" \
            -d '{
                "name": "John Doe",
                "attempts": 5,
                "car": "valid-car-id",
                "hotel": "valid-hotel-id",
                "flight": "valid-flight-id"
            }'
        $ curl -X POST http://localhost:5000/book \  # Failing call
            -H "Content-Type: application/json" \
            -d '{
                "name": "Jane Smith",
                "attempts": 3,
                "car": "valid-car-id",
                "hotel": "invalid-hotel-id",
                "flight": "valid-flight-id"
            }'
        ```
