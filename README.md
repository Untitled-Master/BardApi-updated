# BardApi-updated
# This is an updated version that works
- Go to [Bard](https://bard.google.com/), click `F12` and go to `Application`
- Obtian these elements: `__Secure-1PSID`, `__Secure-1PSIDTS`, `__Secure-1PSIDCC`
- Install the library `bardapi`:
  ```bash
  pip install bardapi
  ```
  if you already have it just upgrade it:
    ```bash
  pip install --upgrade bardapi
  ```
  - Copy this code and fill it:
    ```python
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
    ```
    And voila!
