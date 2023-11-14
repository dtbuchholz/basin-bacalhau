# Start with Golang 1.21 base image for Basin installation
FROM golang:1.21 as go-builder
RUN go install github.com/tablelandnetwork/basin-cli/cmd/basin@latest

# Use python runtime as the parent image; copy over Basin binary
FROM python:3.8
COPY --from=go-builder /go/bin/basin /usr/local/bin/basin
WORKDIR /app
ADD main.py .
ADD job.py .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
