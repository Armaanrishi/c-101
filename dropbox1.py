import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A-Gh3A1_yK3xl4L4f3JIctQkwtYTBo1xXLaewoXAAsHw53gaXM6lxjR-vx3BMPuW3XVe7RwOZ9FoOroi8RL7jaNCSpVpR5kN2aQOmIctklEHfp9JMM-zlJcsx2sRjV2qR8V9X33WqAnw'
    transferData = TransferData(access_token)

    file_from = 'download.png'
    file_to = '/test_dropbox/test.png'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()