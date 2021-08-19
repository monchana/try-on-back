import ftplib
from django.conf import settings

from os.path import join as pjoin


def send_image_ftp(imgdict_list, shop_url, user, pwd):
    ftp_urls = []
    ftp = ftplib.FTP(shop_url, user, pwd)
    ftp.retrlines('LIST')
    for d in imgdict_list:
        file = open(d['src'], "rb")
        path = pjoin(settings.BASE_FTP_DIR, d['dest'])
        ftp_mkdir(ftp, root="/", dest=path)
        files = ftp.nlst(path[:path.rfind("/")])
        if path not in files:
            ftp.storbinary(f"STOR {path}", file)
        ftp_urls.append(shop_url + path)

    ftp.quit()
    return ftp_urls


def ftp_mkdir(ftp, root="/", dest="/web/temp"):
    result = root
    assure = False
    for d in dest.split("/"):
        result = pjoin(result, d)
        if "." in d:
            break
        elif assure:
            ftp.mkd(result)
            continue
        else:
            try:
                temp = ftp.dir(result)
            except Exception as e:
                error = str(e)
                if "450" in error or "No such" in error:
                    ftp.mkd(result)
                    assure = True
                    continue


def get_user_info():
    return {
        "shop_url": "tjagksro.cafe24.com",
        "user": "tjagksro",
        "pwd": "Fitzme123!@",
    }


def get_ftp_img_url(shop_url, dest_url):
    return shop_url + pjoin(settings.BASE_FTP_DIR, dest_url)
