
#This file is used to extract features of the given url

import re
from urllib.parse import urlparse



def fd_length(url):
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0


def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits


def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters


def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')


# Use of IP or not in domain
def having_ip_address(url):
    match = re.search(
        
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)'
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        
        return -1
    else:
        
        return 1



def hostname_length(url):
    return len(urlparse(url).netloc)

def url_length(url):
    return len(urlparse(url).path)



def get_counts(url):

    count_features = []

    i = url.count('-')
    count_features.append(i)

    i = url.count('@')
    count_features.append(i)

    i = url.count('?')
    count_features.append(i)

    i = url.count('%')
    count_features.append(i)

    i = url.count('.')
    count_features.append(i)

    i = url.count('=')
    count_features.append(i)

    i = url.count('http')
    count_features.append(i)

    i = url.count('https')
    count_features.append(i)

    i = url.count('www')
    count_features.append(i)

    return count_features
#new code
def extract_features(url):
    # Extract features
    features = []
    features.append(fd_length(url))  # Feature: fd_length
    features.append(digit_count(url))  # Feature: digit_count
    features.append(letter_count(url))  # Feature: letter_count
    features.append(no_of_dir(url))  # Feature: no_of_dir
    features.append(having_ip_address(url))  # Feature: having_ip_address
    features.append(hostname_length(url))  # Feature: hostname_length
    features.append(url_length(url))  # Feature: url_length
    features.extend(get_counts(url))  # Feature: get_counts

    return features

