
Step 1: Install AWS CLI

Windows: Download, install & verify:

aws --version

Linux:

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version

macOS:

brew install awscli
aws --version

Step 2: Configure AWS CLI

aws configure

Example inputs:

AWS Access Key ID: AKIA...
AWS Secret Access Key: wJalr...
Default region name: eu-north-1
Default output format: json

Verify:

aws configure get region

Step 3: Create S3 Bucket & Folder
aws s3 mb s3://my-cli-bucket
aws s3 cp myfile.txt s3://my-cli-bucket/xyz/
aws s3 cp myarchive.zip s3://my-cli-bucket/xyz/

aws s3 ls s3://manishcli/xyz/
