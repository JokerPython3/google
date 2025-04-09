
from user_agent import generate_user_agent;import requests,re,os,http.client,random,time
class gmail:
  def __init__(self):
    self.day=str(random.randint(1,28))
    self.monthe=str(random.randint(1,12))
    self.year=str(random.randint(1990,2007))
    self.name="".join(random.choice("qwertyuiopasdfghjklzxcvbnm")for m in range(random.randrange(5,10)))
    self.ua=str(generate_user_agent())
  def generate_tokens(self):
    while True:
      try:

        conn = http.client.HTTPSConnection('accounts.google.com')
        headers = {
            'authority': 'accounts.google.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',

            'referer': 'https://accounts.google.com/',
    
            'user-agent': self.ua,
          
        }
        conn.request(
            'GET',
            '/lifecycle/flows/signup?biz=false&continue=https%3A%2F%2Fwww.google.com%2F&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar',
            headers=headers
        )
        response = conn.getresponse().info()
        __Host_GAPS=str(response).split("Set-Cookie: __Host-GAPS=")[1].split(";")[0]
        TL=str(response).split("TL=")[1].split("\n")[0]
        #print(__Host_GAPS)
        #print(TL)
        break
      except:""
    time.sleep(0.55)
    while True:
      try:
       

        cookies = {
   
            '__Host-GAPS': __Host_GAPS,
        }

        headers = {
            'authority': 'accounts.google.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',

            'referer': 'https://accounts.google.com/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
      
            'user-agent': self.ua,
        }

        response = requests.get(
            'https://accounts.google.com/lifecycle/steps/signup/name?continue=https://www.google.com/&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar&TL='+TL,
            cookies=cookies,
            headers=headers,
        )
        tok=re.findall(r'"(.*?)"',str(response.text).split("<!doctype html>")[1].split("/lifecycle/_/AccountLifecyclePlatformSignupUi/")[0])
        hl=tok[0]
        #print(hl)
        
        s1=tok[31]
        at=tok[38]
        #print(s1)
        #print(at)
        break
      except:""
    time.sleep(0.66)
    while True:
      try:
        
 

        cookies = {

            '__Host-GAPS': __Host_GAPS,
        }

        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',

            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
  
            'user-agent':self.ua,
          
            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'E815hb',
            'source-path': '/lifecycle/steps/signup/name',
        
            'hl': hl,
            'TL': TL,
         
        }

        data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.name,at)

        response = requests.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        #print(response.text)
        break
      except:""
    time.sleep(0.77)
    while True:
      try:
    

        cookies = {
 
            '__Host-GAPS': __Host_GAPS,
        }

        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
  
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',
    
            'user-agent': self.ua,

            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
            'x-same-domain': '1',
        }

        params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',
    
            'hl': hl,
            'TL': TL,
    
        }

        data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3CwQ1qDVUCAAbT44Wh8-ONpCKnITjBv4_0ADQBEArZ1OHFo2LLCEdNUcXy72zJAiI9Al8MfF1V7_QxWgZ0_EdCBKDQj7dGTKSxVn_kmHgszQAAAvSdAAAAJ6cBB7EATWHmVLRNR36wpcNfKHXYV6prWjtVVJh9KPUJWrRIJ8fWcUYaCapIRx91xmmquWW1zXfeXYaE9Wl0dFKBqu9MS_y_iUD2H2W7hit7JibrVgdejIiG8HK0q3vp5353qe4C-ifZFtn4Hi4O6YoI4AIPV98eXca7JRRXMddSp0YdG6qVCyGfc8c1X5Fow_aFywwafr5GjIKQ3t3MVYEIVxYnoa5MmFZzlgaIkGf1ZS7RUQPxZAVe5hMh6TJAt9fQcRx7I8WjvCFWsZcpSXV9fBE8cvHUlmVfp7gQLYgbcpBeFVQIems_cGZm5Qguw_tnox_-bucNJRQhQAPSyJo5GX_yk9ONoNamoyMZa41dj6fPH8yXkh9InuE-H35ycldTbZsKykXmwf88u2Bj6Owlhj0aiHEOz5bpX1WvaNmttElrcM8dJWM917ZQXzBUIpp2oiLSW2XrKwcYSn__T-0ocrQt20GF3-auOiuUR-trm3IowBO_OSj-StpFEUuqJ4Wxy6AAbTHS-EFx5kAHyMcjDyM1OexkfonfQoHeQcnk65EiYSJd1nuvtcLjwnD4ICbGvCwFxmIyJWgGJEPyXU1JqOZ3QLnrsfjQAeYtYCJRESDpT69AFHzGnNss7JznzvybzdDD0jY1vCWwPv-XnrhM8BvpvxpScbzFP-0yX__SUmguXbPe1IsLc5vDW7_abJO_sg19CQtRs0Oiq07f5CQ20t7bNuzSCUcbYNwSoJ6JFvgzVCa-plDho77asQmmED-eIUHurSttId3yKq3TMk972jlfFcypJIbgMKYWZg9Lch-UTI1u-tGzgKfxXN4PTzWhsnkgcA_9wQNj__8sGEvDuGJvM1sIteHcrmYIQjdWhiPoXds9X1PYdnXq_zruWo0QD_aEpo-7tSsXrs07MB0mvfN8zqRKm4ImLg8vhWMtR6A8idNTCrmQkeoKZb1ftuNJKHPTMkYbBCkp9QsTq81An5R981Al7X-1IqDa5s4BSBZJHL0T2QotGIevZb297OTNoYKCcS5OkSHFDdtOk_yClTUHhL0nHGoZVQGfl-jprT8QeICA-4jjkmBL2IEv3XplwpNoFPjfxopSQ8I-_msDoy2T5cTubEiLjJiwIkQ4LPVWnX1xOYxfVK89U47GMypN0cekAto42Fxw_HqYcson7wOoXGNceD7FXwp2TdNALrKrXT7WAfUJc4n3frt1NLNyjmfNg-uoryBskAa2lHKjOD1rCvnZ6TyxpT5uVoYVCJc1ae_kEFHxCWjY-DlL_c3nrW7sA3Qp0lhLlY_rEmLtuNAR6OMT1khNn-pAXH965oOSFLTfPhA2El3LBHe9WGwDGr5CG33LK_xiSogL9MMscgd_fCC_PA83aA_-Mb26w29q7ju4p39JwIhcOb1gKDnMWpSre6xjdvEIF84hH_vkDDLKqIQgE2sfZD5a4zCWickV908V_fXo1FXMpQWcs1zTHLhVOa2hrd_IgoW3f_ZVLaLPLbKIwTrNhl6hN2MvUMo_cNnsF_KPqIdnVsLdG2LQne_SzTrgnzAyPiNFRxCvcTvYtXOZmkKOM0onaMMWNYygg9yi2V9jXGGALCovTCVl2kvxawGDDZq0YU0zffuj_BC8vqD552Y-49hqLAXV_6sO_cHbySrzIvNYRlI2rn6DghsIVsqcDAJbDnwR7Kb_9o980BRjkG7f8YYErsEDIf2T7HR8sMoBuZjjxmRXIhLsE6fUJN-7J7lPwDuyDOD-7wtIiw4F_Puf5k1lv7qSOr00pIVcKDVLsFH0nmi3oIxLsOYYLHvPl2l5letXZQ-x1g8KfM48kT1thcq8lAzJ9sO4xxpK_xQCxiyHpZQcHF3s4lJLiKW55LgMYe9lmG8vJBRyWjGx6UadXgcLV6_oANwpR_GsAG-CBtjhi0HtOyNeCTQyAJOif2MuRghU5_xWaKy7nVVJc79BmTNkWYp5l0ViizabYPbFQz9F5n3VBtdcfjeTFut9WPumq0lQyTEfg-q3u-zydYAa_A1RPG4S7bvNbYGI4DLH1E5YxVeMxn64Y2bxxNolSj1An4KBIXATiwgoaBvGKQ-rFivg_FyQAxLlktykcQC3VzPxoQd0RF1VtEXJA4A9k4Lj_6cEpPYOexDc4k-WWEVEBZJfUoH7_E4DgC_U4VuAFCUD2ncin-F7wA0nHigNejoGzuWrHdzg2A_ZUgaWKeK6eOP9QqikpPtX85ZEBtWg_pD570gd7FwmFdvBIDuR-6HmKIbdzapxOCzZonadFXjlCAiHpPtYFrZcFBWcid_fy4vcy5CtXVjJQSqXCq-p2XXTqB3oMs2N5tPOMqIT8x2CEF5RApnxyutv2cP2nrF-uR9kAE8Alv-BrBJ1p0-V48jW0BffSwyY3O6AFAWmkarAVnmJA6zxxbFx7ifNIcIsvdQkZH9IFTnc0Ku1IfiQ0WyS7oxBWI2zd1quKDxs_7xm69lXJIqMUgtp0MJgcMC50Jvcm_JRIopTBkE-xbr5ZvydAQzaipwORkun8B8EvJUEpy38svuZNiZ-Dlfi1mZVXFHoMk-ERhcOpbhLgm3V_raS55CXJcgzJtk0n6VgcJhomowwxtX4Jr1hWdtMGTDGRkcVqed8_r7d2rE%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fwww.google.com%2F%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(self.year,self.monthe,self.day,at)

        response = requests.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        ).text
        #print(response)
        break
      except:""
    try:
        return{
           "tokens":{
               "TL":TL,
               "hl":hl,
               "at":at,
               "s1":s1,
               "__Host-GAPS":__Host_GAPS,
           },
       "info":{
           "Year":self.year,
           "monthe":self.monthe,
           "day":self.day,
           "Birthday":self.year+":"+self.monthe+":"+self.day,
           "Name":self.name,
       }
        }
    except:
        return{
            "tokens":{
                   "TL":"",
                   "hl":"",
                   "at":"",
                   "s1":"",
                   "__Host-GAPS":"",
            },
            "info":{
                   "Year":self.year,
                   "monthe":self.monthe,
                   "day":self.day,
                   "Birthday":self.year+":"+self.monthe+":"+self.day,
                   "Name":self.name,
            }
        }
  def get_tokens(self):
      while True:
          try:
              m=self.generate_tokens()["tokens"]
              TL=m["TL"]
              hl=m["hl"]
              at=m["at"]
              s1=m["s1"]
              __Host_GAPS=m["__Host-GAPS"]
              try:
                  os.remove("tokens.txt")
              except:""
              with open("tokens.txt","a") as f:
                  f.write(f"{TL}///{at}///{s1}///{hl}///{__Host_GAPS}")
              return
          except:""
  def check_tokens(self):
      while True:
          try:
              try:
                  m=open("tokens.txt","r").read().splitlines()[0].split("///")
                  TL=m[0]
                  at=m[1]
                  s1=[2]
                  hl=m[3]
                  __Host_GAPS=m[4]
                  
              except:
                  self.get_tokens()
                  return
              email="".join(random.choice("qwertyuiopasdgfhjklzxcbvnm1234567890")for kse in range(random.randrange(9,15)))
  

              cookies = {

                  '__Host-GAPS': __Host_GAPS,
              }

              headers = {
                  'authority': 'accounts.google.com',
                  'accept': '*/*',
                  'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                  'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',

                  'origin': 'https://accounts.google.com',
                  'referer': 'https://accounts.google.com/',

                  'user-agent': self.ua,
      
                  'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                  'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
                  'x-same-domain': '1',
              }

              params = {
                  'rpcids': 'NHJMOd',
                  'source-path': '/lifecycle/steps/signup/username',
                  'hl': hl,
                  'TL': TL,
     
              }

              data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C1%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C32994%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

              response = requests.post(
                  'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                  params=params,
                  cookies=cookies,
                  headers=headers,
                  data=data,
              )
              #print(response.text)
              if "password" in response.text:
                  return
              else:
                  self.get_tokens()
                  return


              
                
          except:""
  def check_gmail(self,email):
      while True:
          try:
              if "@" in email:email=email.split("@")[0]
              self.check_tokens()
              m=open("tokens.txt","r").read().splitlines()[0].split("///")
              
              TL=m[0]
              at=m[1]
              s1=[2]
              hl=m[3]
              __Host_GAPS=m[4]
         

              cookies = {

                  '__Host-GAPS': __Host_GAPS,
              }

              headers = {
                  'authority': 'accounts.google.com',
                  'accept': '*/*',
                  'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                  'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
  
                  'origin': 'https://accounts.google.com',
                  'referer': 'https://accounts.google.com/',

                  'user-agent': self.ua,
        
                  'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
                  'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
                  'x-same-domain': '1',
              }

              params = {
                  'rpcids': 'NHJMOd',
                  'source-path': '/lifecycle/steps/signup/username',

                  'hl': hl,
                  'TL': TL,

              }

              data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C1%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C32994%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

              response = requests.post(
                  'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
                  params=params,
                  cookies=cookies,
                  headers=headers,
                  data=data,
              )
              #print(response.text)
              if "password" in response.text:
                  return True
              else:
                  return False
          except:""
email=input("Enter Email: ")
print(gmail().check_gmail(email))
