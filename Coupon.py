from googlesearch import search

def coupon_website_links(brand):
    """
    return array with 3 Links:
    [0] Coupon site
    [1] Comapny site
    [2] Company enviroment impact site
    """

    links = ["","",""]

    search = brand

    if " " in search:
        "".join(search.split(" "))

    CouponSite = "https://www.joinhoney.com/search?q={}".format(search)
    links[0] = CouponSite

    CompanySite = next(iter(search(brand, num_results=1)))
    links[1] = CompanySite

    ImpactSite = next(iter(search("{} positive environment impact".format(brand))))
    links[2] = ImpactSite

    return links


