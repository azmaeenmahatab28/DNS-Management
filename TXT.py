import dns.resolver

domain = "example.com"
answers = dns.resolver.resolve(domain, 'TXT')

for txt_record in answers:
    print(f"TXT Record: {txt_record}")
