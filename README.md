# OpenStack Client on Centos Docker Image

The Cloud team at [NIC](http://egov.com/) ran a training event last
year for new OpenStack users in our organization.  The biggest pain
point for all involved was installing the OpenStack client.  Every
version of every OS had its own quirks.

The new student experience needs to be smooth, and this docker
container lets us provision a customized environment for each student
once they've registered and signed in to our lab management system.

Of course anyone can use these images to run code against any
OpenStack installation.  There are tags for all of the supported
releases.

```
# Pull the latest release
docker pull timfreund/openstack-client-centos

# Pull the latest of a named release
docker pull timfreund/openstack-client-centos:liberty
```
