import json
import logging

import boto3
import cfnresponse


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def delete_repository(repo_name, region):
    logger.info('deleting {}'.format(repo_name))
    client = boto3.client("ecr", region_name=region)

    response = client.delete_repository(repositoryName=repo_name, force=True)
    logger.info('Response {}'.format(response))


def lambda_handler(event, context):
    # make sure we send a failure to CloudFormation if the function is going to timeout
    logger.info('Received event:{}'.format(json.dumps(event)))
    # status = cfnresponse.SUCCESS
    try:
        repository = event['ResourceProperties']['repository']
        aws_region = event['ResourceProperties']['aws_region']
        if event['RequestType'] == 'Delete':
            delete_repository(repository, aws_region)
    except Exception as e:
        logging.error('Exception: %s' % e, exc_info=True)
    #   status = cfnresponse.FAILED
    finally:
        #    cfnresponse.send(event, context, status, {}, None)
        pass