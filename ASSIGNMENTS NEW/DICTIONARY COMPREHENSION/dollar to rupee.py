"""1.DICTIONARY COMPREHENSION----"""
def doller_to_rupee():
    price={"laptop":10,"mobile":5,"watch":3,"keyboard":1}
    covert_to_rupee=81.38
    n_price={i:j*covert_to_rupee for (i,j) in price.items()}
    return n_price
rc=doller_to_rupee()
print(rc)