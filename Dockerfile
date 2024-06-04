FROM python:3.11.9-bullseye AS base
RUN pip install pdm

# builder js
FROM oven/bun:1 as style_builder
WORKDIR /app
COPY . .
RUN bun install
RUN bun run build

# builder static
FROM base AS builder
WORKDIR /app
COPY . .
COPY --from=style_builder /app/src/app_landing/static/app_landing/tailwind.css /app/src/app_landing/static/app_landing/tailwind.css
RUN pdm install
RUN pdm run src/manage.py collectstatic --noinput
RUN pdm build

# build deps only
FROM python:3.11.9-bullseye AS build_python
WORKDIR /app
COPY --from=builder /app/dist/*.whl .
RUN pip install *.whl --no-cache-dir --prefer-binary

# Deployment
FROM gcr.io/distroless/python3-debian12:latest AS runner
WORKDIR /usr/local/lib/python3.11/site-packages
USER nonroot
COPY --from=builder /app/src/static /app/src/static
COPY --from=build_python /usr/local/bin/granian /usr/local/bin/granian
COPY --from=build_python /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
COPY src/manage.py .
EXPOSE 8000
COPY run.sh .
ENV GRANIAN_WORKERS=8
ENV GRANIAN_THREADS=8
ENV GRANIAN_LOOP=uvloop
ENV GRANIAN_HTTP=1
ENV GRANIAN_INTERFACE=wsgi
# CMD ["./run.sh"]
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]
CMD ["/usr/local/bin/granian", "--opt", "--respawn-failed-workers", "django_modular.wsgi:application", "--host", "0.0.0.0"]
