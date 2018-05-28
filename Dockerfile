FROM fundocker/edxapp:ginkgo.1-1.0.3-dev

# Dependencies
ENV DOCKERIZE_VERSION v0.6.0

# Get container user and group ids via build arguments
# Default: 0:0 (root:root)
ARG user=0
ARG group=0

# Add a non-privileged user to run the application if given as a build argument
RUN if [ ${user} -ne 0 -a ${group} -ne 0 ]; then \
        groupadd --gid $group app ; \
        useradd --uid $user --gid $group --home /app app ; \
    fi

# Install dockerize
RUN curl -L \
        --output dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
        https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# Add application sources
ADD . /app/fonzie/

# Install application and project requirements
RUN cd /app/fonzie && \
    pip install --exists-action w -r requirements.txt

# FIXME: pyopenssl seems to be linked with a wrong openssl release leading to
# bad handskake ssl errors. This looks ugly, but forcing pyopenssl
# re-installation solves this issue.
RUN pip install -U pyopenssl

# Run container with the $user:$group user
#
# We recommend to build the container with the following build arguments to map
# container user with the HOST user:
#
# docker build --build-arg user=$(id -u) --build-arg group=$(id -g)
USER $user:$group
