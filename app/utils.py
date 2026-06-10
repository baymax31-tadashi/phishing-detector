import re
from urllib.parse import urlparse


FEATURE_NAMES = [
    "url_length",
    "num_dots",
    "num_hyphens",
    "num_at",
    "num_double_slash",
    "num_subdomains",
    "has_https",
    "has_ip_in_domain",
    "domain_length",
    "num_query_params",
    "has_suspicious_keywords",
    "num_digits_in_url",
    "has_port",
    "path_length",
    "num_special_chars",
]

def extract_features_from_url(url):
    try:
        parsed = urlparse(url)
        domain = parsed.netloc
        path = parsed.path

        suspicious_keywords = [
            "login", "verify", "secure", "account", "update",
            "banking", "confirm", "signin", "password", "ebayisapi"
        ]

        features = [
            len(url),                                                             # url_length
            url.count('.'),                                                       # num_dots
            url.count('-'),                                                       # num_hyphens
            url.count('@'),                                                       # num_at
            url.count('//') - 1,                                                 # num_double_slash
            len(domain.split('.')) - 2 if domain.count('.') > 1 else 0,         # num_subdomains
            int(parsed.scheme == 'https'),                                        # has_https
            int(bool(re.match(r'\d+\.\d+\.\d+\.\d+', domain))),                 # has_ip_in_domain
            len(domain),                                                          # domain_length
            len(parsed.query.split('&')) if parsed.query else 0,                 # num_query_params
            int(any(kw in url.lower() for kw in suspicious_keywords)),           # has_suspicious_keywords
            sum(c.isdigit() for c in url),                                       # num_digits_in_url
            int(':' in domain and not domain.endswith(':80')
                and not domain.endswith(':443')),                                 # has_port
            len(path),                                                            # path_length
            sum(url.count(c) for c in ['%', '=', '?', '&', '#']),               # num_special_chars
        ]
        return features

    except Exception:
        return [0] * len(FEATURE_NAMES)
