#!/usr/bin/env python3

import argparse
import csv

import boto3
from botocore.exceptions import ClientError


# Define add_tags() function that will add the tags to the given S3 bucket
def add_tags(s3_client, bucket_name, tag_set):

  try:
    s3_client.put_bucket_tagging(Bucket=bucket_name, Tagging=tag_set)
    print('Tags added to the %s S3 bucket successfully' % bucket_name)
  except ClientError as e:
    print(e.response['Error']['Code'])
    print('Error! Tags were not added to the %s S3 bucket successfully'
          % bucket_name)


# Define create_s3_session() function which will create a AWS S3 session
# for the given named AWS account
def create_s3_session(account):

  session = boto3.session.Session(profile_name=account)
  return session.client(service_name='s3')


# The main function will parse the user arguments given via the user
# console and call the function to create
if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Check all S3 buckets in the \
    given AWS account and display buckets without any tags')
  parser.add_argument('aws_account_name', type=str, help='Named AWS user \
    account')
  parser.add_argument('tag_list_file', type=str, help='Bucket names and \
    related tags as a csv file')

  args = parser.parse_args()
  s3_client = create_s3_session(args.aws_account_name)

  with open(args.tag_list_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    count = len(header)

    for row in csv_reader:
      tag_set = []
      for x in range(1, count):
        tag_set.append({'Key': str(header[x]), 'Value': str(row[x])})
      tag_set = {'TagSet': tag_set}

      add_tags(s3_client, row[0], tag_set)
