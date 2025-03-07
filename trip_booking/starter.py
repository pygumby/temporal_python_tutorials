import asyncio
import uuid

from flask import Flask, jsonify, request
from temporalio.client import Client

from shared import TASK_QUEUE_NAME, BookVacationInput
from workflows import BookingWorkflow


def create_app(temporal_client: Client):
    app = Flask(__name__)

    def generate_unique_username(name):
        return f"{name.replace(' ', '-').lower()}-{str(uuid.uuid4().int)[:6]}"

    @app.route("/book", methods=["POST"])
    async def book_vacation():
        """
        Endpoint to book a vacation. This function expects to receive a POST request
        with the following JSON body:

        {
            "name": "User Name",
            "attempts": 5,
            "car": "valid-car-id",
            "hotel": "valid-hotel-id",
            "flight": "valid-flight-id",
        }

        Returns:
            Response: JSON response with booking details or error message.
        """
        user_id = generate_unique_username(request.json.get("name"))
        attempts = request.json.get("attempts")
        car = request.json.get("car")
        hotel = request.json.get("hotel")
        flight = request.json.get("flight")

        input_data = BookVacationInput(
            attempts=int(attempts),
            book_user_id=user_id,
            book_car_id=car,
            book_hotel_id=hotel,
            book_flight_id=flight,
        )

        result = await temporal_client.execute_workflow(
            BookingWorkflow.run,
            input_data,
            id=user_id,
            task_queue=TASK_QUEUE_NAME,
        )

        response = {"user_id": user_id, "result": result}
        return jsonify(response)

    return app


async def main():
    temporal_client = await Client.connect("localhost:7233")
    app = create_app(temporal_client)
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    asyncio.run(main())
