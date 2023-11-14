# Tableland Basin + WeatherXM + Bacalhau Demo

[![License: MIT AND Apache-2.0](https://img.shields.io/badge/License-MIT%20AND%20Apache--2.0-blue.svg)](./LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg)](https://github.com/RichardLitt/standard-readme)

> Compute over data with Bacalhau from data pushed to Tableland Basin

## Table of Contents

- [Background](#background)
- [Install](#install)
  - [Docker](#docker)
- [Usage](#usage)
  - [Docker](#docker-1)
  - [On your Machine](#on-your-machine)
  - [Building the Image](#building-the-image)
  - [Makefile Reference](#makefile-reference)
- [Contributing](#contributing)
- [License](#license)

## Background

This project contains a simple setup wherein data pushed to Tableland Basin (replicated to Filecoin) is fetched and computed over with the [Bacalhau](https://www.bacalhau.org/) network.

## Install

To set things up on your machine, you'll need to do the following:

1. Run: `python -m venv env`.
2. Source: `source env/bin/activate`

Then, you can use the `Makefile` command to install dependencies: `make install`.

### Docker

By default, the `main.py` script points to a custom [`dtbuchholz/basin`](https://hub.docker.com/repository/docker/dtbuchholz/basin/tags?page=1&ordering=last_updated) image within the Bacalhau job configuration. You can also run `docker compose` if desired, which is provided in the Makefile commands noted below.

## Usage

### Docker

Use `docker compose` to run it on Docker:

```sh
make up
```

This will set up the Bacalhau job, pointing to the `dtbuchholz/basin` image, and run the job defined at `job.py`. The job will fetch data from Tableland Basin, compute over it, and return computation results. It'll log something like the following:

```
Submitted job: 26a5f55f-dabd-490b-ba4b-59f14f746702
Waiting for job to finish...
Job finished; results at CID: QmdKf9z6URSRwSLUrehSKXAQCU1rwBqbKvpSfPpxzQ3QFq
// ...
```

To stop the job, run:

```sh
make down
```

### On your Machine

Or, to run the job directly on your machine, simply run the `main.py` program:

```sh
make local
```

This assumes that any changes in your project/image have been published to the Docker Hub, so make sure you run `make publish` in order to see those changes. If you're simply trying to see how the job _should_ run from a pure data analysis perspective, you can try running the job directly on your machine, without Bacalhau involved:

```sh
make job-local
```

### Building the Image

The image is built using `docker buildx` for cross-platform targeting; the Bacalhau network requires an `amd64` target architecture. If you haven't already, you'll need to create a builder instance via the following, and thereafter, you can inspect it to ensure that the builder is properly set up:

```sh
make buildx-create
make buildx-inspect
```

Then, you can build the image with:

```sh
make build
```

If you want to build the image using `docker compose` (with forced "no cache"), you can run:

```sh
make up-build
```

### Makefile Reference

The following defines all commands available in the `Makefile`:

- `make install`: install dependencies.
- `make buildx-create`: create a builder instance.
- `make buildx-inspect`: inspect the builder instance.
- `make build`: build the image with `buildx`.
- `make up-build`: build the image using `docker compose` with `--no-cache`.
- `make publish`: publish the image to Docker Hub (note: the username is `dtbuchholz`, so replace with your own here as well as in the `build` step).
- `make up`: run the image using `docker compose`.
- `make down`: stop the image using `docker compose`.
- `make local`: run the `main.py` & `job.py` programs on your machine using Bacalhau.
- `make job-local`: run the `job.py` program on your machine without using Bacalhau.
- `make freeze`: freeze dependencies (only needed if you make changes to the python code deps).

## Contributing

PRs accepted.

Small note: If editing the README, please conform to the standard-readme specification.

## License

MIT AND Apache-2.0, © 2021-2023 Tableland Network Contributors
