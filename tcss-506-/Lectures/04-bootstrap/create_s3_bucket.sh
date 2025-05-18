#!/bin/bash

# Stop script execution on any error
set -e
# Echo commands as they are executed
set -x

# Script to create an AWS S3 bucket
# Usage: ./create_s3_bucket.sh <bucket-name> [region]
# 
# This script creates an S3 bucket with the specified name in the given region.
# By default, S3 buckets are created with private access (only accessible by the bucket owner).
# Additional commands would be needed to modify permissions after creation.

# Check if at least the bucket name is provided
if [ $# -lt 1 ]; then
    echo "Usage: $0 <bucket-name> [region]"
    echo "If region is not specified, us-east-1 will be used as default."
    exit 1
fi

BUCKET_NAME=$1
REGION=${2:-"us-east-1"}  # Use provided region or default to us-east-1

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "Error: AWS CLI is not installed. Please install it first."
    exit 1
fi

# Check if AWS credentials are configured
# This verifies that your AWS account has the necessary IAM permissions to create S3 buckets
if ! aws sts get-caller-identity &> /dev/null; then
    echo "Error: AWS credentials are not configured. Please run 'aws configure' first."
    exit 1
fi

# Create S3 bucket
echo "Creating S3 bucket: $BUCKET_NAME in region $REGION..."

# NOTE ON PERMISSIONS:
# This command creates a bucket with default permissions:
# - Private access only (not public)
# - Only the bucket owner has full control
# - No bucket policies or ACLs are applied
# - Default encryption is not enabled
#
# To modify permissions after creation, you would need additional commands like:
# - aws s3api put-bucket-policy: to set a bucket policy
# - aws s3api put-public-access-block: to configure public access settings
# - aws s3api put-bucket-acl: to set bucket ACLs
# - aws s3api put-bucket-encryption: to enable encryption

if [ "$REGION" = "us-east-1" ]; then
    # For us-east-1, we don't specify LocationConstraint
    aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION"
else
    # For other regions, we need to specify LocationConstraint
    aws s3api create-bucket --bucket "$BUCKET_NAME" --region "$REGION" --create-bucket-configuration LocationConstraint="$REGION"
fi

# Check if bucket was created successfully
if [ $? -eq 0 ]; then
    echo "S3 bucket '$BUCKET_NAME' created successfully!"
    echo "SECURITY NOTE: The bucket has been created with default private permissions."
    echo "Only your AWS account has access to this bucket."
else
    echo "Failed to create S3 bucket '$BUCKET_NAME'."
    exit 1
fi