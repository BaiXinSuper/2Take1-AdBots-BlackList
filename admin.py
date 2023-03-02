import requests
__DEBUG = False
if not __DEBUG:
    url = "http://Server Ip:6471"
else:
    url = "http://127.0.0.1:6471"
headers = {'V': "10", 'F': "B", "Ver": "No_offical_Admin_V1",
           "UUID": 'admin'}  # do not change here


def unban(info):
    return requests.post(url+"/admin/black/remove/"+info, headers=headers).text


def ban_uid(uid):
    return requests.post(url+"/admin/UUID/add/"+uid, headers=headers).text


def main():
    c = input("1 解禁/删除广告机 2 封禁UUID 3 退出\n")
    try:
        c = int(c)
    except:
        main()
    if c == 1:
        print(unban(input("IP/UUID/SCID\n")))
    elif c == 2:
        print(ban_uid(input("UUID\n")))
    elif c == 3:
        return 0
    main()


main()
