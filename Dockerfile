FROM python:3.9

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir \
    annotated-types==0.6.0 \
    anyio==4.3.0 \
    certifi==2024.2.2 \
    click==8.1.7 \
    colorama==0.4.6 \
    dnspython==2.6.1 \
    email_validator==2.1.1 \
    fastapi==0.111.0 \
    fastapi-cli==0.0.2 \
    greenlet==3.0.3 \
    h11==0.14.0 \
    httpcore==1.0.5 \
    httptools==0.6.1 \
    httpx==0.27.0 \
    idna==3.7 \
    Jinja2==3.1.3 \
    markdown-it-py==3.0.0 \
    MarkupSafe==2.1.5 \
    mdurl==0.1.2 \
    orjson==3.10.3 \
    pip==23.3.1 \
    pydantic==2.7.1 \
    pydantic_core==2.18.2 \
    Pygments==2.18.0 \
    PyMySQL==1.1.0 \
    python-dotenv==1.0.1 \
    python-multipart==0.0.9 \
    PyYAML==6.0.1 \
    rich==13.7.1 \
    setuptools==69.0.2 \
    shellingham==1.5.4 \
    sniffio==1.3.1 \
    SQLAlchemy==2.0.29 \
    starlette==0.37.2 \
    typer==0.12.3 \
    typing_extensions==4.11.0 \
    ujson==5.9.0 \
    uvicorn==0.29.0 \
    watchfiles==0.21.0 \
    websockets==12.0 \
    wheel==0.42.0

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]