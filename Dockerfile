FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive DISPLAY=:1 WIDTH=1024 HEIGHT=768

RUN apt-get update && apt-get install -y --no-install-recommends \
    xvfb xdotool scrot x11-utils python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --break-system-packages fastapi uvicorn google-generativeai playwright pydantic

RUN playwright install --with-deps chromium

WORKDIR /app
COPY agent.py server.py .

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
