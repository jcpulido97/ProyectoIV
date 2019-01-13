# Vagrant Azure
Primero debemos de descargar el plugin y un archivo de configuración para Azure

```bash
$ vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
$ vagrant plugin install vagrant-azure
```

Para crear la instancia, conectarme a ella por SSH, aprovisionarla y demás he usado el siguiente *Vagrantfile*:

```ruby
# Referencia: - https://github.com/Azure/vagrant-azure/
# Dependencia del plugin para vagrant para saber comunicarse con azure 
require 'vagrant-azure'

# Configuracion de maquina
Vagrant.configure('2') do |config|
  # Maquina base de la que partimos, preparada para azure
  config.vm.box = 'azure-dummy'

  # Usuario a usar en la conexion ssh
  config.ssh.username = 'vagrant'
  # Directorio donde se encuentra la clave privada a usar en la conexion ssh
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  # Hacemos override de la variable de conexion a la db si existe en el host (cuando conectemos por ssh)
  if defined?(ENV['DATABASE_URL'])
	config.ssh.forward_env = ['DATABASE_URL']  
  end
  # Evitar que Vagrant actualice nuestra maquina para hacerlo nosotros manualmente
  config.vm.box_check_update = false
	
  # Configuracion de la maquina en Azure, azure como variable de configuracion
  config.vm.provider 'azure' do |azure|
    # Informacion obligatoria para poder conectar con Azure.
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
		
    # Nombre de la maquina
    azure.vm_name     = 'vmmanagement'
    # Maquina de tipo Serie B con recursos suficientes: 1vCPU 1GB RAM
    azure.vm_size     = 'Standard_B1s'
    # Imagen SO Ubuntu server 16.04	alojada en los servicios de Azure
    azure.vm_image_urn = 'canonical:ubuntuserver:16.04-LTS:latest'
    # Localizada en Europa del Oeste (Comentado porque Azure free-tier solo deja crearlas en EEUU)
    # azure.location = 'West Europe'
	
    # Puertos que se exponen; el 80
    azure.tcp_endpoints = '80'
  end

  # Configurar ansible para poder hacer provision desde el mismo vagrant
  config.vm.provision "ansible" do |ansible|
	# Path de nuestro archivo con las instrucciones a seguir para provisionar nuestra maquina
    ansible.playbook = "provision/playbook.yml"
  end
end
```

Debemos de tener configuradas las variables de entorno con nuestros datos de Azure, que nos enseñan a obtener [aquí](https://github.com/Azure/vagrant-azure/)
```bash
$ vagrant up --provider=azure
```

![Vagrant up](https://github.com/jcpulido97/ProyectoIV/blob/master/doc/img/up.PNG?raw=true)

Con el siguiente comando podremos hacer ssh directamente con nuestra Máquina Virtual

```bash
$ vagrant ssh
```

![Vagrant ssh](https://github.com/jcpulido97/ProyectoIV/blob/master/doc/img/ssh.png?raw=true)

Ya tendríamos nuestra máquina encendida con ssh configurado.

Ahora tocaría realizar el provisionamiento de dependencias que podemos ver cómo se hace en este [enlace](https://github.com/jcpulido97/ProyectoIV/tree/master/doc/Ansible.md)