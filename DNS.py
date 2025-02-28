import dns.resolver

domain = "example.com"
answers = dns.resolver.resolve(domain, 'A')

for ip in answers:
    print(f"IP Address: {ip}")
