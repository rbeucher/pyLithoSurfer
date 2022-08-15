# PyLithoSurfer: A Simple Python interface to the LithoSurfer API

Romain Beucher (2019-2022)

## Installation

```
pip install PyLithoSurfer
```

## Configuration

The Lithodat API `username` and `password` must be defined as environment variables:

On Linux this can be define in a shell:

```
LITHODAT_TEST_USERNAME="username"
LITHODAT_TEST_PASSWORD="password"
export LITHODAT_TEST_USERNAME
export LITHODAT_TEST_PASSWORD

```

The same applies for the `PRODUCTION` and `DEV` instances.
