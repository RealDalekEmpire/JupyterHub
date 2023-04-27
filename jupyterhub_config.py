import os
# Configuration file for jupyterhub.

c = get_config()  #noqa
c.JupyterHub.hub_connect_ip = 'jupyterhub'
c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.network_name = os.environ.get('SPAWNER_NETWORK', 'jupyterhub-network')
c.DockerSpawner.volumes = {
       'jupyterhub-user-{username}': '/home/jovyan',
       os.environ.get('SHARED_FOLDER', '/home/sysadmin/Shared'): '/home/jovyan/Shared'  # Add the shared mapping
   }

c.JupyterHub.services = [
       {
           'name': 'cull-idle',
           'admin': True,
           'command': [
               'python',
               '-m',
               'jupyterhub_idle_culler',
               f"--timeout={os.environ.get('TIMEOUT', '3600')}",  # Set the idle timeout (in seconds)
               f"--cull-every={os.environ.get('CULL-EVERY', '600')}",  # Set the culling interval (in seconds)
               '--concurrency=10',  # Set the number of concurrent requests when culling (optional)
           ],
       }
   ]
c.DockerSpawner.image = os.environ.get('SPAWNER_IMAGE', 'jupyter/datascience-notebook') 