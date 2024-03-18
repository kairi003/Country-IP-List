#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipaddress
import requests
from pathlib import Path
from itertools import repeat

RIR_URLS = {
    'arin': 'https://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest',
    'ripencc': 'https://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest',
    'apnic': 'https://ftp.apnic.net/stats/apnic/delegated-apnic-latest',
    'lacnic': 'https://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-latest',
    'afrinic': 'https://ftp.afrinic.net/pub/stats/afrinic/delegated-afrinic-latest',
}


def main():
    dst_dir = Path('dst')
    dst_dir.mkdir(exist_ok=True)
    mask4 = dst_dir / 'ipv4-mask.txt'
    mask6 = dst_dir / 'ipv6-mask.txt'
    cidr4 = dst_dir / 'ipv4-cidr.txt'
    cidr6 = dst_dir / 'ipv6-cidr.txt'
    with mask4.open('w') as m4, mask6.open('w') as m6, cidr4.open('w') as c4, cidr6.open('w') as c6:
        for resitry, url in RIR_URLS.items():
            print(f'Fetching {resitry} data...')
            for cc, network in iter_networks(resitry, url):
                if network.version == 4:
                    m4.write(f'{cc}\t{network.with_netmask}\n')
                    c4.write(f'{cc}\t{network.with_prefixlen}\n')
                elif network.version == 6:
                    m6.write(f'{cc}\t{network.with_netmask}\n')
                    c6.write(f'{cc}\t{network.with_prefixlen}\n')
    print('Done.')


def iter_networks(resitry_name, url):
    res = requests.get(url, stream=True)
    for line in res.iter_lines(1024):
        if isinstance(line, bytes):
            line = line.decode('utf-8')
        elif not isinstance(line, str):
            continue
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        try:
            resitry, cc, type_, start, value, *_ = line.split('|')
        except ValueError:
            continue
        if resitry != resitry_name:
            continue
        if cc == '' or cc == '*' or start == '*':
            continue
        if type_ == 'ipv4':
            start_address = ipaddress.IPv4Address(start)
            end_address = start_address + (int(value) - 1)
            yield from zip(repeat(cc), ipaddress.summarize_address_range(start_address, end_address))
        if type_ == 'ipv6':
            yield cc, ipaddress.IPv6Network(f'{start}/{value}')


if __name__ == '__main__':
    main()
