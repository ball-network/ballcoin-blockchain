#!/usr/bin/env bash
# Pre remove script for the UI .deb to clean up the symlinks from the installer

set -e

unlink /usr/bin/ball || true
unlink /usr/bin/ballcoin-blockchain || true
