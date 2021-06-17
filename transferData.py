import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Ay6l3k14-8Pz4x7BQpfAwXFeWHndnZuzGv3EhFStr06w_DoZpPUI1v5dLQy7RRBNwItkpTk9hzpd9hL_TNVOpczcOEhVV7mbuRYBf1b68CtPmIi3gf9r_GvlEg5djfeETCSHgEx3'
    transferData = TransferData(access_token)

    file_from = 'C:/Users/Sandeep/Desktop/whitehatjr/class101/text.txt'
    file_to = '/uploadfiledhruv/text.txt'  
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()