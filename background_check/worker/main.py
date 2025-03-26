import asyncio

from temporalio.client import Client
from temporalio.worker import Worker

from activities.ssn_trace_activity import ssn_trace_activity
from workflows.background_check_workflow import BackgroundCheck


async def main():
    client = await Client.connect(
        "localhost:7233", namespace="background_check_namespace"
    )

    worker = Worker(
        client,
        task_queue="background_check_task_queue",
        workflows=[BackgroundCheck],
        activities=[ssn_trace_activity],
    )

    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
