import json

import pytest
from temporalio.client import WorkflowHistory
from temporalio.worker import Replayer

from workflows.background_check_workflow import BackgroundCheck


@pytest.mark.asyncio
async def test_replay_workflow_history_from_file():
    with open("tests/background_check_workflow_history.json", "r") as f:
        history_json = json.load(f)
        await Replayer(workflows=[BackgroundCheck]).replay_workflow(
            WorkflowHistory.from_json("background_check_workflow", history_json)
        )
