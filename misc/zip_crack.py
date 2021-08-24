import zipfile
import easygui  as gui
from threading import Thread

def crackPassword(zFile,password):
    try:
        zFile.extractall(pwd=password.encode("utf-8"))
        print("[+]crack password "+password)
        return
    except (RuntimeError,zipfile.BadZipFile):
        print("密码："+password+" error! test next one...")
        pass


def main():
    filepath=gui.fileopenbox("请选择要破解的zip文件！")
    zFile=zipfile.ZipFile(filepath)

    pass_file=gui.fileopenbox("请选择密码文件！")
    with open(pass_file,'r') as fp:
        for passwd in fp.readlines():
            passwd=passwd.strip('\n')
            t=Thread(target=crackPassword,args=(zFile,passwd))
            t.start()


if __name__=='__main__':
    main()