FROM fundocker/edxapp:hawthorn.1-2.6.0

ARG USER_ID=1000
ARG GROUP_ID=1000

# Switch back to a priviledged user to perform base installation
USER root:root

# Install dockerize to wait for mysql before running the container command
# (and prevent connection issues)
ENV DOCKERIZE_VERSION v0.6.1
RUN python -c "import requests;open('dockerize-linux-amd64.tar.gz', 'wb').write(requests.get('https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz', allow_redirects=True).content)" && \
    tar -C /usr/local/bin -xzvf dockerize-linux-amd64.tar.gz && \
    rm dockerize-linux-amd64.tar.gz

# Add the non-privileged user that will run the application
RUN groupadd -f --gid ${GROUP_ID} edx && \
    useradd --uid ${USER_ID} --gid ${GROUP_ID} --home /edx edx

# Allow the edx user to create files in /edx/var (required to perform database
# migrations)
RUN mkdir /edx/var && \
    chown edx:edx /edx/var

# FIXME: as mentionned in fun-platform and edx-platform bug tracker, this
# webpack-stats.json is required both in production and development in a static
# directory 😢
#
# Also, the /edx/var tree should be writable by the running user to perform
# collectstatic and migrations.
RUN mkdir -p /edx/app/edxapp/staticfiles/studio && \
    chown -R edx:edx /edx/var && \
    cp /edx/app/edxapp/edx-platform/common/static/webpack-stats.json /edx/app/edxapp/staticfiles/ && \
    cp /edx/app/edxapp/edx-platform/common/static/studio/webpack-stats.json /edx/app/edxapp/staticfiles/studio/

# Copy the app to the working directory
COPY --chown=edx:edx . /edx/app/fonzie/

# Install development dependencies and perform a base installation of the app
RUN cd /edx/app/fonzie/ && \
    pip install --no-cache-dir -r requirements-dev.txt

# Switch to an un-privileged user matching the host user to prevent permission
# issues with volumes (host folders)
USER ${USER_ID}:${GROUP_ID}
