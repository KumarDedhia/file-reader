import unittest
import boto3

class BaseFileUploader(unittest.TestCase):
    def setUp(self):
        s3 = boto3.resource(
            service_name='s3',
            region_name='ap-south-1',
            aws_access_key_id='<aws_access_key_id>', # test credentials
            aws_secret_access_key='<aws_secret_access_key>' # test credentials
        )

    def test_getFileType(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
