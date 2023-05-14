import test as t
import Coupon as c
def main(brand):
    ethical, boycotts = t.open_first_link(brand)
    if ethical is None:
        ethical = 'None'
    if boycotts is None:
        boycotts = 'None'
    links = c.coupon_website_links(brand)
    fv = open('forC#.txt','w+',encoding='utf-8')
    fv.write(ethical+'\n')
    fv.write(boycotts+'\n')
    for link in links:
        fv.write(link+'\n')
    fv.close()

    return 
main("Adidas")