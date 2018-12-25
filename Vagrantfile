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

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end # Vagrant.configure
