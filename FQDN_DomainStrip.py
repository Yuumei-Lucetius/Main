# Takes a CSV list of FQDNs and strips the domains, outputting solely the hostnames to a new CSV
hostnames = []
with open('D://Test/hostnames.csv') as f:
    hosts = f.read().splitlines()
for h in hosts:
    h = h.split(".", 1)[0]
    hostnames.append(h)
with open('D://Test/new_hostnames.csv', 'w') as f:
    for h in hostnames:
        f.write("%s\n" % h)
