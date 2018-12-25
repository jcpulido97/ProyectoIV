# Vagrant Azure
Primero debemos de descargar el plugin y un archivo de configuración para Azure

```bash
$ vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
$ vagrant plugin install vagrant-azure
```

Para crear la instancia, conectarme a ella por SSH, aprovisionarla y demás he usado el siguiente *Vagrantfile*:

```ruby
# Require the Azure provider plugin
require 'vagrant-azure'

# Create and configure the Azure VMs
Vagrant.configure('2') do |config|

  # Use dummy Azure box
  config.vm.box = 'azure-dummy'

  # Specify SSH key
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  # Configure the Azure provider
  config.vm.provider 'azure' do |az, override|
    # Pull Azure AD service principal information from environment variables
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
  end # config.vm.provider 'azure'
    
end # Vagrant.configure
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