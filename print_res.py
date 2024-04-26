import qrcode
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#folderid=input('文件夾id:')
folderid='1xsWVZ2MeRxEtcTdqCALNwQfbrhEKWwQf'


while(1):
    try:
        name=input('圖片名稱:')
        back=input('副檔名:')
        file = drive.CreateFile()
        file['parents'] = [{'id':folderid}]
        file.SetContentFile('./converted_img/'+name+'.'+back)
        file.Upload()
        fileid=file.get('id')
        img = qrcode.make('https://drive.google.com/file/d/'+fileid)
        #img.show()
        img.save(name+'.'+back)
    except:
        pass