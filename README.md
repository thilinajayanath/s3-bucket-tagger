# s3-bucket-tagger
Simple script written in Python 3 that will add tags to the given buckets in an AWS account.

## Prerequisites

Following Python 3 libraries are required.
```
boto3
botocore
```

AWS named profile and credentials should be configured - [Read more](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

## Installation

* Clone the git repository
```
git clone git@github.com:thilinajayanath/s3-bucket-tagger.git
```

It is recommended to use a Python 3 virtual environment to install the above libraries [Read more](https://docs.python.org/3/library/venv.html)  
Required libraries can be installed with the requirements.txt file to the virtual environment [Read more](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

```
python3 -m venv /path/to/new/virtual/environment
/path/to/new/virtual/environment/bin/pip install -r requirements.txt
```

## Format of the csv file with tags
Please refer the example.csv file.  

The csv file containing the tags should be in the following format.  

Header of the csv file
```
bucket_name,key1,key2,etc..
```

Values
```
<bucket-name>,tag1,tag2
```

## Run the application

```
cd s3-bucket-tagger
chmod u+x s3-bucket-tagger.py
/path/to/new/virtual/environment/bin/python s3-bucket-tagger.py <AWS-PROFILE-NAME> <TAG-LIST-AS-CSV>
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
