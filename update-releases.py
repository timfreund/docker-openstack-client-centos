#!/usr/bin/env python3

import bs4
import os
from jinja2 import Template
from urllib.request import urlopen

base_url = 'http://newton.vpn.freunds.net:8000/repos/openstack/'

def get_releases(base_url = base_url):
    releases = []
    response = urlopen(base_url)
    body = response.read().decode('utf-8')
    soup = bs4.BeautifulSoup(body, "html.parser")
    for a in soup.findAll('a'):
        if a.attrs['href'].count('openstack-') == 1:
            release_name = a.attrs['href'].split('-')[-1][0:-1]
            release_url = "/".join((base_url, a.attrs['href']))
            releases.append((release_name, release_url))
    return releases
            
def get_release_rpm_url(release_url):
    response = urlopen(release_url)
    body = response.read().decode('utf-8')
    soup = bs4.BeautifulSoup(body, "html.parser")

    rpm_url = None
    max_index = 0
    for a in soup.findAll('a'):
        if a.attrs['href'].count('.rpm') == 1:
            file_name = a.attrs['href'].replace('.noarch.rpm', '')
            index = int(file_name[file_name.rindex('-')+1:])
            if index > max_index:
                max_index = index
                rpm_url = "/".join((release_url, a.attrs['href']))
    return rpm_url

def write_release_directory(release_name, rpm_url):
    if not os.path.exists(release_name):
        os.mkdir(release_name)
    with open('Dockerfile.template', 'r') as template_file:
        template = Template(template_file.read())
        rendered = template.render(rpm_url=rpm_url)
        
        with open("%s/Dockerfile" % release_name, 'w') as docker_file:
            docker_file.write(rendered)
        
            
if __name__ == '__main__':
    releases = get_releases()
    for release_name, release_url in releases:
        rpm_url = get_release_rpm_url(release_url)
        if rpm_url:
            write_release_directory(release_name, rpm_url)

