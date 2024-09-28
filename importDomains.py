import whois
import models

with open('cloudflare-radar_top-1000-domains_20240916-20240923.csv', 'r') as file:
    for line in file:
        print(line)
        w = whois.whois(line.rstrip())
        if 'registrar' in w:
            print(w['registrar'])
            if w['registrar']:
                id = models.insert_service(w['registrar'], "example")
                models.insert_url(line.rstrip(), id)
