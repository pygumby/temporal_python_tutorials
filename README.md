# temporal_python_tutorials
Me following along various Temporal tutorials in Python

1. Build a Temporal Application from scratch in Python
    - [Source code](hello_temporal)
    - [Tutorial](https://learn.temporal.io/getting_started/python/hello_world_in_python/)
    - Instructions:
        ```
        $ Install dependencies
        $ cd hello_temporal
        $ pip install -r requirements.txt

        # Start Temporal server and worker
        $ temporal server start-dev
        $ python run_worker.py

        # Run tests
        $ pytest

        # Run workflow
        $ python run_workflow.py
        ```
2. Build a trip booking application in Python
    - [Source code](trip_booking)
    - [Tutorial](https://learn.temporal.io/tutorials/python/trip-booking-app/)
    - Instructions:
        ```
        # Install dependencies
        $ cd trip_booking
        $ pip install -r requirements.txt

        # Start Temporal server and worker
        $ temporal server start-dev
        $ python run_worker.py

        # Start Flask app
        $ python starter.py

        # Call REST API
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

3. Build a Background Check application with Temporal and Python
    - [Source code](background_check)
    - [Tutorial](https://learn.temporal.io/tutorials/python/background-check/)
    - Instructions:
        ```
        # Prerequisites
        $ cd background_check
        $ pip install -r requirements.txt

        # Start Temporal server and worker
        $ temporal server start-dev --db-filename temporal.db
        $ temporal operator namespace create background_check_namespace
        $ python -m worker.main

        # Run tests
        $ pytest

        # Run workflow
        $ temporal workflow start \
            --workflow-id background_check_workflow \  # Manually set Workflow ID
            --task-queue background_check_task_queue \
            --type BackgroundCheck \
            --input '"555-55-5555"' \
            --namespace background_check_namespace

        # List workflow executions
        $ temporal workflow list \
            --namespace background_check_namespace

        # Save workflow execution data to file
        $ temporal workflow show \
            --workflow-id background_check_workflow \
            --namespace background_check_namespace \
            --output json > tests/background_check_workflow_history.json
        ```
