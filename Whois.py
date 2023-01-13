import datetime
import whois

Domeny = ('directit.pl','wp.pl','pn-it.pl','nowaczyk.pl')


for domain in Domeny:

    x = whois.whois(domain)
    expiration_date = x.expiration_date
    domain_name = x.domain
    current_date = datetime.datetime.now()

    try:
        days_left = (expiration_date - current_date).days

        if days_left <= 0:
            print(f"{domain_name} domena wygasła.")
        elif days_left <= 30:
            print(f"{domain_name} domena wygaśnie za {days_left} days.")
        else:
            print(f"{domain_name} domena wygaśnie za {days_left} days.")
    except:
        print("Wygasły tokeny xD")
        break
