# JupyterHub with DockerSpawner

This repository contains a Docker Compose setup to deploy JupyterHub with DockerSpawner, including support for GPU usage and idle culling.

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/realdalekempire/JupyterHub
   cd jupyterhub-dockerspawner
   ```

2. Build the JupyterHub image:
   ```
   docker-compose build
   ```

3. Start the JupyterHub service:
   ```
   docker-compose up -d
   ```

4. Access JupyterHub at `http://localhost:8000`.

## Configuration

The following environment variables can be set to customize the deployment:

- `SPAWNER_IMAGE`: The Jupyter Notebook image to spawn for users (default: `jupyter/datascience-notebook`).
- `SPAWNER_NETWORK`: The Docker network to be used by spawned containers (default: `jupyterhub-network`).
- `SPAWNER_DEFAULT_URL`: The default URL for the spawned notebook server (default: `/lab`).
- `TIMEOUT`: The idle timeout in seconds (default: `120`).
- `CULL-EVERY`: The interval in seconds for culling idle servers (default: `600`).
- `SHARED_FOLDER`: The path to a folder on the host to be shared among all users (default: `/home/sysadmin/Shared`).

These environment variables can be set in the `docker-compose.yml` file or passed through the command line when starting the services, e.g.,

```
SPAWNER_IMAGE=my-notebook-image
```

## Components

- `docker-compose.yml`: Docker Compose configuration file, defining JupyterHub service, volumes, and networks.
- `Dockerfile`: Dockerfile to build the custom JupyterHub image, including DockerSpawner and jupyterhub-idle-culler.
- `jupyterhub_config.py`: JupyterHub configuration file, setting up DockerSpawner, shared folder, and idle culling.

## Network

The Docker network `jupyterhub-network` is created automatically by Docker Compose. All spawned containers will be connected to this network, allowing communication between JupyterHub and the spawned containers.

## Troubleshooting

If you encounter any issues or need to update the configuration, follow these steps:

1. Stop the JupyterHub service:
   ```
   docker-compose down
   ```

2. Make the necessary modifications to the configuration files or environment variables.

3. Rebuild the JupyterHub image if necessary:
   ```
   docker-compose build
   ```

4. Start the JupyterHub service again:
   ```
   docker-compose up -d
   ```
