from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    RemovalPolicy,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins

)
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        s3_bucket = s3.Bucket(self, "Bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            versioned=True,
            removal_policy=RemovalPolicy.RETAIN
        )

        cloudfront.Distribution(self, "distro",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(s3_bucket),
            )
        )
