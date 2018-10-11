
import requests

def get_auth_url():
    weibo_auth_url="https://api.weibo.com/oauth2/authorize"
    redirect_url="http://123.206.43.75:8080/complete/weibo/"
    auth_url=weibo_auth_url+"?client_id={client_id}&redirect_uri={redirect_uri}".format(client_id=225198667,redirect_uri=redirect_url)
    return auth_url
def get_access_token(code="7d4817e0170ff209bcdfef449f91222c"):

    access_token_url="https://api.weibo.com/oauth2/access_token"
    re_dict=requests.post(access_token_url,data={
        "client_id":"225198667",
        "client_secret":"ec6b2c97c877eb5f64e33ef867436fff",
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":"http://123.206.43.75:8080/complete/weibo/",

    })
    #'{"access_token":"2.00mcD3MG0Z9uOP83482cd54attzckB","remind_in":"157679999","expires_in":157679999,"uid":"5679370176","isRealName":"false"}'
    pass
def get_user_info(access_token="",uid=1):
    user_url="https://api.weibo.com/2/users/show.json?access_token={access_token}&uid={uid}".format(access_token=access_token,uid=uid)
    print(user_url)
if __name__=="__main__":
    get_auth_url()
    # get_access_token(code="7d4817e0170ff209bcdfef449f91222c")
    #
    # get_user_info(access_token="2.00mcD3MG0Z9uOP83482cd54attzckB",uid=5679370176)
