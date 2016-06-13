FROM centos:7
MAINTAINER "Tim Freund" <tim@freunds.net>

RUN yum install -y https://repos.fedorapeople.org/repos/openstack//openstack-mitaka//rdo-release-mitaka-3.noarch.rpm; \
    yum update -y; \
    yum install -y `yum search openstack | grep client | sed -e 's/:.*//' -e 's/ *//' ` python-oslo-log python-oslo-log-doc

CMD ["echo", "try this: docker run -it openstack-client-centos:mitaka /bin/bash"]
