#!/bin/sh
GRANIAN_WORKERS=8 \
GRANIAN_THREADS=8 \
GRANIAN_LOOP=uvloop \
GRANIAN_HTTP=1 \
GRANIAN_INTERFACE=wsgi \
python3.11 granian --opt --respawn-failed-workers src.django_modular.wsgi:application --host 0.0.0.0
