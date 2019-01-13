# Ansible para provisionamiento

Usaremos [Ansible](https://www.ansible.com/) que nos permite provisionar nuestras máquinas de forma fácil y bastante sencilla

Primero debemos de crear nuestro archivo hosts en el directorio */etc/ansible/hosts*

```
[staging]
192.168.0.5

[production]
137.116.185.97
```

Debemos poner las IP de las máquina(s)  de los distintos grupos justo debajo del nombre del grupo entre corchetes

En este caso nuestro archivo consta de dos grupos:

- `staging`: que consta de las máquinas donde se hacen las pruebas
- `production`: son las máquinas que estarían dando servicio a nuestros clientes en una situación de las aplicaciones del mundo real

Ahora tocaría crear el archivo que se encarga de descargar las dependencias, etc. Este archivo se llama playbook.yml. **Para ello me he servido de esta [web](https://blog.ssdnodes.com/blog/step-by-step-ansible-guide/)**

```yaml
# Referencia https://blog.ssdnodes.com/blog/step-by-step-ansible-guide/
# Hosts a los que conectarse para realizar el provisionamiento.
- hosts: production

  # Usuario a utilizar en ssh.
  remote_user: vagrant

  # Tareas a realizar.
  tasks:
    # Tendremos que agregar el repositorio de python3 ya que nuestra version de Ubuntu no trae por defecto
    - name: Agregar repo python 3.6
      become: true
      apt_repository: repo=ppa:deadsnakes/ppa state=present

    - name: Update apt
      become: true
      apt:
        upgrade: yes
        update_cache: yes

    - name: Instalar docker
      become: true
      apt: pkg=docker.io state=present

    - name: Cambio permisos docker
      become: true
      file: path=/var/run/docker.sock owner=vagrant group=docker

    - name: Instalar Python 3.6
      become: true
      apt: pkg=python3.6 state=present

    - name: Instalar pip3
      become: true
      apt: pkg=python3-pip state=latest

    - name: Instalar pip
      become: true
      apt: pkg=python-pip state=latest

    - name: Instalar setuptools
      become: true
      pip: name=setuptools state=latest
      
    - name: Instalar docker-py
      become: true
      pip: name=docker-py state=latest

    - name: Ejecutar servicio Docker
      become: true
      service: name=docker state=started
      
    - name: Copio archivo con variable de entorno
      copy: src=./dbpass dest=/home/vagrant owner=vagrant group=vagrant

    # Descargar el contenedor que contiene el proyecto.
    - name: Descargar docker Proyecto
      docker_image: name=kronos483/proyectoiv state=present
```

```bash
# Con este comando podremos provisionar nuestra máquina iniciada con vagrant up
$ ansible-playbook playbook.yml
```

![Ansible](https://github.com/jcpulido97/ProyectoIV/blob/master/doc/img/ansible.PNG?raw=true)

Tambíen podríamos cambiar nuestro vagrantfile para que podamos hacer el provisionamiento con el comando **vagrant provision**:

```ruby
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/playbook.yml"
  end
```

Ya tendríamos nuestra máquina con nuestras dependencias resueltas y preparada para ejecutar nuestro microservicio.

Solo quedaría realizar el despliegue que podemos ver cómo se hace en este [enlace](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/fabric.md)