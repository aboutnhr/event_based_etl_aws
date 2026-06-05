import boto3

glue = boto3.client("glue")

def lambda_handler(event, context):

    response = glue.start_job_run(
        JobName="ETL Job",
        Arguments={
            "--input_observed":
                "s3://hanumanth-bigdata-practice-bucket/sample_files/plants_observed_temp.csv",

            "--input_required":
                "s3://hanumanth-bigdata-practice-bucket/sample_files/plants_required_temp.csv",

            "--output_path":
                "s3://hanumanth-bigdata-practice-bucket/output/"
        }
    )
    return {
        "statusCode": 200,
        "jobRunId": response["JobRunId"]
    }
