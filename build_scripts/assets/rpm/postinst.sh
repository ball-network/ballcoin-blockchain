#!/usr/bin/env bash
# Post install script for the UI .rpm to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/ball/resources/app.asar.unpacked/daemon/ballcoin /usr/bin/ballcoin || true
