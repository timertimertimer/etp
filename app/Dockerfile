FROM ghcr.io/astral-sh/uv:python3.13-bookworm

ARG UID=1000

WORKDIR /var/www/app

ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

RUN echo "deb http://deb.debian.org/debian/ bookworm main contrib non-free" > /etc/apt/sources.list.d/debian.list \
    && apt-get update && apt-get install -y \
        curl \
        cron \
        sudo \
        default-mysql-client \
        supervisor \
        git \
        zip \
        p7zip-full \
        unrar \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./

RUN uv pip install -e . --system
RUN playwright install && playwright install-deps

RUN touch /var/log/etp_parsing_output.log && chmod 777 /var/log/etp_parsing_output.log

COPY ./cron /etc/cron.d/mycron
RUN chmod 0644 /etc/cron.d/mycron

COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
