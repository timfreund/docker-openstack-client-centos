#!/usr/bin/env bash

latest_release=`find . -name Dockerfile | sort | tail -1 | sed -e 's|./||' -e 's|/.*||'`

for df in `find . -name Dockerfile`;
do
    release=`echo ${df} | sed -e 's|./||' -e 's|/.*||'`
    tag="timfreund/openstack-client-centos:${release}"

    echo docker build -t ${tag} ${release}
    docker build -t ${tag} ${release}
    docker push ${tag}

    if [ ${release} == ${latest_release} ]
    then
        echo docker tag ${tag} timfreund/openstack-client-centos:latest
        docker tag ${tag} timfreund/openstack-client-centos:latest
        docker push timfreund/openstack-client-centos:latest
    fi
done;
