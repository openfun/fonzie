#!/usr/bin/env bash

set -eo pipefail

REPO_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd)"
FONZIE_UNSET_USER=0

# _set_user: set (or unset) default user/group id used to run docker commands
#
# usage: _set_user
#
# You can override default user (and/or group) ID (the current host user/group
# ID), by defining the FONZIE_USER_ID (and/or FONZIE_GROUP_ID) environment
# variable.
#
# To avoid running docker commands with a custom user/group ID, please set the
# $FONZIE_UNSET_USER environment variable to 1.
function _set_user() {

    if [ $FONZIE_UNSET_USER -eq 1 ]; then
        USER_ID=""
        GROUP_ID=""
        return
    fi

    # USER_ID = FONZIE_USER_ID or `id -u` if FONZIE_USER_ID is not set
    USER_ID=${FONZIE_USER_ID:-$(id -u)}
    GROUP_ID=${FONZIE_GROUP_ID:-$(id -g)}
}

# docker_compose: wrap docker-compose command
#
# usage: docker_compose [options] [ARGS...]
#
# options: docker-compose command options
# ARGS   : docker-compose command arguments
function _docker_compose() {
    docker-compose -p fonzie -f "$REPO_DIR/docker-compose.yml" "$@"
}

# _dc_build: wrap docker-compose build command
#
# usage: _dc_build [options] [ARGS...]
#
# options: docker-compose build command options
# ARGS   : docker-compose build command arguments
function _dc_build() {
    _set_user

    user_args="--build-arg user=$USER_ID --build-arg group=$GROUP_ID"
    if [ -z $USER_ID ]; then
        user_args=""
    fi

    _docker_compose build $user_args "$@"
}

# _dc_run: wrap docker-compose run command
#
# usage: _dc_run [options] [ARGS...]
#
# options: docker-compose run command options
# ARGS   : docker-compose run command arguments
function _dc_run() {
    _set_user

    user_args="--user=$USER_ID:$GROUP_ID"
    if [ -z $USER_ID ]; then
        user_args=""
    fi

    _docker_compose run --rm $user_args "$@"
}

# _dc_exec: wrap docker-compose exec command
#
# usage: _dc_exec [options] [ARGS...]
#
# options: docker-compose exec command options
# ARGS   : docker-compose exec command arguments
function _dc_exec() {
    _set_user

    user_args="--user=$USER_ID:$GROUP_ID"
    if [ -z $USER_ID ]; then
        user_args=""
    fi

    _docker_compose exec $user_args "$@"
}
