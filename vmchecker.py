import urllib2, urllib, re, cookielib
import android

droid = android.Android()


def login(u,p):
    url= "https://www1.virginmobileusa.com/login/login.do"
    data_t= [
        ("loginRoutingInfo", "https://www1.virginmobileusa.com:443/myaccount/home.do")
        , ("min", u)
        , ("vkey", p)
        , ("submit", "submit")
        ]
    data= urllib.urlencode(data_t)
    cj= cookielib.CookieJar()

    opener= urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    opener.addheaders = [('Referer', 'https://www1.virginmobileusa.com/login/login.do'),
                   ('Content-Type', 'application/x-www-form-urlencoded'),
                   ('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')]


    usock= opener.open(url, data)
    s= usock.read()

#    print(usock.geturl())
#    print(usock.info())
#    print(s)
    return s



def get_min(s):
    matches= re.search(r"remaining_minutes\"><strong>(\d+)<\/strong>\D*(\d+)<", s)
#    import pdb; pdb.set_trace()
    return matches.group(1,2)
    




def alert_mins((u,v)):
    s= "minutes used: %s/%s" % (u,v)
#    print s

    droid.makeToast(s)
    



def get_user_info():
    phone= droid.getLine1Number().result
#    print phone
    if phone == None:
        phone= droid.dialogGetInput('Phone Number').result
    pin= droid.dialogGetPassword('Pin').result
    return (phone, pin)


if __name__ == "__main__":
    u,p= get_user_info()
#    print u,p
    s= login(u,p)
    data= get_min(s)
    alert_mins(data)
