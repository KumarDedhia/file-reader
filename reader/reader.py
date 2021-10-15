import os
import filetype
class BaseFileUploader():
    def __init__(self, dir, s3_connector, s3_bucket_name, s3_format_filter=[]):
        self.dir = dir
        self.s3 = s3_connector
        self.s3_format_filter = s3_format_filter
        self.s3_bucket = s3_bucket_name
        self.checkS3BucketConnection()

    def checkS3BucketConnection(self):
        return self.s3.Bucket(self.s3_bucket).creation_date != None

    def readAll(self):
        for root, directories, files in os.walk(self.dir, topdown=False):
            for name in files:
                try:
                    file_type = self.getFileType(os.path.join(root, name))
                    if file_type in self.s3_format_filter:
                        self.upload_s3(os.path.join(root, name), name)
                except Exception as e:
                    print("Failed to upload %s with the below error."%(os.path.join(root, name)))
                    print(e)

    def getFileType(self, path):
        # print(path)
        kind = filetype.guess(path)
        return kind.mime

    def upload_s3(self, path, filename):
        print("Uploading : %s"%(filename))
        self.s3.Bucket(self.s3_bucket).upload_file(Filename=path, Key=filename)
        print("Uploaded : %s"%(filename))
