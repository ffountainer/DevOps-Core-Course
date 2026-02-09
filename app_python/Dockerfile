FROM python:3.13-slim AS builder
WORKDIR /app_python
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY app.py . 

FROM python:3.13-slim
ENV PORT="12345"
EXPOSE 12345
RUN useradd --create-home --shell /bin/bash newuser
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder ./app_python .
USER newuser
CMD ["python", "app.py"]
