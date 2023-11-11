# Tableland Basin + WeatherXM + Bacalhau Demo

[![License: MIT AND Apache-2.0](https://img.shields.io/badge/License-MIT%20AND%20Apache--2.0-blue.svg)](./LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg)](https://github.com/RichardLitt/standard-readme)

> Compute over data from data pushed to Tableland Basin with Bacalhau

## Table of Contents

- [Background](#background)
- [Install](#install)
  - [Docker](#docker)
- [Usage](#usage)
  - [Docker Compose](#docker-compose)
- [Contributing](#contributing)
- [License](#license)

## Background

This project contains a simple setup wherein data pushed to Tableland Basin (replicated to Filecoin) is fetched and computed over with the [Bacalhau](https://www.bacalhau.org/) network.

> Note: this is a demo project, and is not intended for production use. It is a WIP and does not contain the full suite of features noted above and simply runs a `"hello world"` job.

## Install

To set things up on your machine, you'll need to do the following:

1. Run: `python -m venv env`.
2. Source: `source env/bin/activate`
3. Install: `pip install -r requirements.txt`

### Docker

By default, the `main.py` script points to a custom [`dtbuchholz/wxm`](https://hub.docker.com/repository/docker/dtbuchholz/wxm/tags?page=1&ordering=last_updated) image within the Bacalhau job configuration. You can also run `docker compose` if desired.

## Usage

To run the job, simply run `main.py`:

```sh
python main.py
```

This will set up the Bacalhau job, pointing to the `dtbuchholz/wxm` image, and run the job defined at `job.py`. The job will fetch data from Tableland Basin, compute over it, and return computation results. It'll log something like the following:

```
Submitted job: 26a5f55f-dabd-490b-ba4b-59f14f746702
Waiting for job to finish...
Job finished; results at CID: QmdKf9z6URSRwSLUrehSKXAQCU1rwBqbKvpSfPpxzQ3QFq
// ...
```

### Docker Compose

You can run the job with `docker compose` as well:

```sh
docker compose up
```

## Contributing

PRs accepted.

Small note: If editing the README, please conform to the standard-readme specification.

## License

MIT AND Apache-2.0, © 2021-2023 Tableland Network Contributors
