import dns.resolver

domain = "example.com"
answers = dns.resolver.resolve(domain, 'NS')

for server in answers:
    print(f"Name Server: {server.target}")
