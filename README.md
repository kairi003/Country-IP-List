# Country IP List

It shows the IP address range of each country obtained and formatted from five RIPs: ARIN, RIPE NCC, APNIC, LACNIC, and AfriNIC.

See [dst/](dst/) for the formatted data.

Last Updated: 2026-02-14T02:25:32+00:00


# Usage
For example, download `ipv4-cidr.txt` and decompress.

```sh
# download txt data
$ wget https://raw.githubusercontent.com/kairi003/Country-IP-List/main/dst/ipv4-cidr.txt
$ curl https://raw.githubusercontent.com/kairi003/Country-IP-List/main/dst/ipv4-cidr.txt > ipv4-cidr.txt

# download txt data with auto compression
$ wget --compression=gzip https://raw.githubusercontent.com/kairi003/Country-IP-List/main/dst/ipv4-cidr.txt
$ curl --compressed https://raw.githubusercontent.com/kairi003/Country-IP-List/main/dst/ipv4-cidr.txt > ipv4-cidr.txt

# download gzip data and decompress
$ wget -O - https://raw.githubusercontent.com/kairi003/Country-IP-List/main/dst/ipv4-cidr.txt.gz | gunzip > ipv4-cidr.txt
$ curl https://raw.githubusercontent.com/kairi003/Country-IP-List/main/dst/ipv4-cidr.txt.gz | gunzip > ipv4-cidr.txt
```
