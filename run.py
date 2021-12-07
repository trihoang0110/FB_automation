from Automate.automate_liking import Facebook
import Automate.constant as const

with Facebook() as fb:
    fb.access_site()
    fb.login(email=const.num, password=const.password)
#   fb.choose_page()
