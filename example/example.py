import reader.reader as rf
from utils.config import Config
import boto3
all_formats = ['image/jpeg', 'video/mp4', 'image/gif', 'image/webp', 'application/pdf', 'application/x-executable', 'application/x-msdownload', 'application/wasm', 'image/png', 'application/zip', 'application/font-sfnt', 'audio/x-wav', 'application/x-shockwave-flash', 'image/bmp', 'application/font-woff', 'image/x-icon', 'image/tiff']

config = Config()
s3 = boto3.resource(
    service_name='s3',
    region_name=config.region_name,
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key
)

# Add the format to be uploaded
s3_format_filter = ['image/jpeg', 'image/gif', 'image/webp', 'image/png', 'image/bmp', 'image/x-icon', 'image/tiff']

# your s3 bucket  goes here
s3_bucket = "hollow-bucket"

dir_location = "<provide your dir location here>"
obj = rf.BaseFileUploader(dir_location, s3, s3_bucket, s3_format_filter)
obj.readAll()

