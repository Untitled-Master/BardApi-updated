from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID":
    "",
    "__Secure-1PSIDTS":
    "",
    "__Secure-1PSIDCC":
    ""
}
bard = BardCookies(cookie_dict=cookie_dict)
while True:
  Query = input("enter ")
  res = bard.get_answer(Query)['content']
  print(res)
