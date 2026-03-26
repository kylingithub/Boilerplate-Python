# ── Build Stage ──────────────────────────────────────────────────────────────
FROM python:3.13-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ── Runtime Stage ─────────────────────────────────────────────────────────────
FROM python:3.13-slim

WORKDIR /app

# 從 builder 複製已安裝的套件
COPY --from=builder /install /usr/local

# 只複製程式碼，不含測試、設定範本等
COPY src/ ./src/

# 設定 PYTHONPATH 讓 game_metric package 可被找到
ENV PYTHONPATH=/app/src

# Prometheus metrics 預設 port
EXPOSE 8800

# 非 root 使用者執行，降低安全風險
RUN useradd --no-create-home --shell /bin/false appuser
USER appuser

CMD ["python", "-m", "proj.main"]
