import pytest

from temporalio.testing import ActivityEnvironment
from activities.ssn_trace_activity import ssn_trace_activity


@pytest.mark.asyncio
async def test_execute_activity() -> str:
    activity_environment = ActivityEnvironment()
    expected_output = "pass"
    assert expected_output == await activity_environment.run(
        ssn_trace_activity, "555-55-5555"
    )
