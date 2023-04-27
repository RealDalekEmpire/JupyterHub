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

## Acknowledgements

This project is built on top of the following open-source projects:

- [JupyterHub](https://github.com/jupyterhub/jupyterhub): A multi-user Hub that spawns, manages, and proxies multiple instances of the single-user Jupyter Notebook server.
- [DockerSpawner](https://github.com/jupyterhub/dockerspawner): A custom Spawner for JupyterHub that spawns user notebook servers in Docker containers.
- [jupyterhub-idle-culler](https://github.com/jupyterhub/jupyterhub-idle-culler): A JupyterHub service to cull idle servers.


## Frequently Asked Questions

**Q: How do I add new users to JupyterHub?**

A: By default, JupyterHub uses a simple PAM-based authentication system that allows any user with an account on the system to log in. To add new users, you need to create a new system user on the host machine. You can do this by running the following command:

```
sudo useradd -m new_username
sudo passwd new_username
```

**Q: How can I enable HTTPS for JupyterHub?**

A: To enable HTTPS, you need to obtain an SSL certificate for your domain and configure JupyterHub to use it. You can follow the official JupyterHub [documentation](https://jupyterhub.readthedocs.io/en/stable/reference/websecurity.html) on setting up SSL encryption.

**Q: Can I use a different authentication system for JupyterHub?**

A: Yes, JupyterHub supports various authentication systems, including OAuth, LDAP, and more. To use a different authentication system, you need to configure the `authenticator_class` in the `jupyterhub_config.py` file and install the required packages. Refer to the JupyterHub [documentation](https://jupyterhub.readthedocs.io/en/stable/reference/authenticators.html) for more information.

**Q: How do I customize the Jupyter Notebook image used by the users?**

A: To customize the Jupyter Notebook image, you can create your own Dockerfile based on one of the [official Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks), install the required packages and extensions, and set the `SPAWNER_IMAGE` environment variable to the name of your custom image.

**Q: How do I update the JupyterHub, DockerSpawner, or jupyterhub-idle-culler versions?**

A: To update the versions of JupyterHub, DockerSpawner, or jupyterhub-idle-culler, modify the `Dockerfile` to use the desired version of the packages, rebuild the JupyterHub image, and restart the service as described in the [Troubleshooting](#troubleshooting) section.

**Q: How do I back up user data?**

A: User data is stored in Docker volumes, which are automatically created by Docker Compose. To back up user data, you can use the `docker cp` command to copy the contents of the volume to a directory on the host machine, or use a third-party tool like [docker-volume-backup](https://github.com/loomchild/docker-volume-backup) to automate the process.