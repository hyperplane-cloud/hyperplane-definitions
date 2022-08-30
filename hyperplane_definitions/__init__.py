import os


OUTPUT_FILES_BASE_DIR = "outputs"


def get_job_id():
    job_id = os.environ.get('HYPERPLANE_JOB_ID')

    if not job_id:
        print("Warning: job_id is not set, returning None. If needed you can set it via the HYPERPLANE_JOB_ID environment variable")

    return job_id
