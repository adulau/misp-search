misp-search - search MISP - Malware Information Sharing Platform
----------------------------------------------------------------

misp-search is a simple set of tools to query MISP instances from
the command line.

## Requirements

- Python 2.7
- [PyMISP](https://github.com/MISP/PyMISP)

## Usage

~~~~
usage: misp-search.py [-h] [-a] -u U -k K -c C [-o O] -q Q [-d]

misp-search - search MISP from command line

optional arguments:
  -h, --help  show this help message and exit
  -a          Add an event based on file attributes (default: False)
  -u U        URL of the MISP instance
  -k K        MISP API key
  -c C        MISP SSL certificate file
  -o O        Output format: json (default) or event_id
  -q Q        One or more value(s) to query
  -d          Debug mode
~~~~

## Examples

Searching a list of MD5 from a MISP instance and returning events with matching MD5:

~~~~
cat listofmd5 | parallel --gnu -m 'python ./bin/misp-search.py -u https://misppriv.circl.lu -k <APIKEY> -c misppriv.circl.lu.crt -o event_id -q {1}'
~~~~
