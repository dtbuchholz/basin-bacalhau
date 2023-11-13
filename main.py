"""Run a job on the Bacalhau network."""

import time
import pprint

from bacalhau_apiclient.models.deal import Deal
from bacalhau_apiclient.models.job_spec_docker import JobSpecDocker
from bacalhau_apiclient.models.job_spec_language import JobSpecLanguage
from bacalhau_apiclient.models.publisher_spec import PublisherSpec
from bacalhau_apiclient.models.spec import Spec
from bacalhau_apiclient.models.storage_spec import StorageSpec

from bacalhau_sdk.config import get_client_id
from bacalhau_sdk.api import submit, states

# Set up the job submission
job_submission = dict(
    APIVersion="V1beta1",
    ClientID=get_client_id(),
    Spec=Spec(
        engine="Docker",
        publisher_spec=PublisherSpec(type="ipfs"),
        docker=JobSpecDocker(
            image="dtbuchholz/wxm",
            entrypoint=["python", "job.py"],
        ),
        language=JobSpecLanguage(job_context=None),
        wasm=None,
        resources=None,
        timeout=1800,
        outputs=[
            StorageSpec(
                storage_source="IPFS",
                name="outputs",
                path="/outputs",
            )
        ],
        deal=Deal(concurrency=1),
        do_not_track=False,
    ),
)

# Check the state of a submitted job
def check_job_state(job_id, attempts=30, delay=1):
    for _ in range(attempts):
        job_states = states(job_id).to_dict()
        state_meta = job_states['state']
        executions = state_meta['executions']

        # If the job is completed, return the results, including the CID
        if executions[0]['state'] == "Completed":
            return executions[0]['published_results']
        
        # Wait before trying again
        time.sleep(delay)
        
    return None

# Submit the job
job_req = submit(job_submission).to_dict()
pprint.pprint(job_req)
job_id = job_req['job']['metadata']['id']
print("Submitted job:", job_id)

# Check for the job in the list with retries
print("Waiting for job to finish...")
matching_executions = check_job_state(job_id)
if matching_executions:
   print("Job finished; results at CID:", matching_executions['cid'])
else:
    print("No matching job found.")