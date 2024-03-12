#!/usr/bin/env bash
# Post install script for the UI .deb to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/ball/resources/app.asar.unpacked/daemon/ball /usr/bin/ball || true
ln -s /opt/ball-network/ballcoin-blockchain /usr/bin/ballcoin-blockchain || true
