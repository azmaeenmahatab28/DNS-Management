import dns.resolver

domain = "example.com"
answers = dns.resolver.resolve(domain, 'MX')

for record in answers:
    print(f"Mail Server: {record.exchange}, Priority: {record.preference}")
