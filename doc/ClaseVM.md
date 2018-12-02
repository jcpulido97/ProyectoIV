## Clase VM

Esta clase se encarga de manejar todo lo que tiene que ver con las Máquinas virtuales, desde su creación y verificación, hasta su serialización en formato JSON. Se encarga de proveer de una interfaz común para acceder a la información y configuración de todas las máquinas virtuales sin importar el Hypervisor/Sistema Operativo usado en los servidores.

##### Atributos miembro:

| Variable                                                    |    Tipo     | Valor por defecto |
| ----------------------------------------------------------- | :---------: | :---------------: |
| nombre                                                      | **String**  |       Vacío       |
| vcpu                                                        |   **int**   |        -1         |
| ram                                                         |   **int**   |         0         |
| uuid                                                        |   **int**   |         0         |
| ip                                                          | **String**  |       Vacío       |
| vmdsk (Path a la iso de la máquina virtual)                 | **String**  |       Vacío       |
| mac_address                                                 | **String**  |       Vacío       |
| alive                                                       | **Boolean** |       False       |
| date_created (Fecha indicada en formato epoch, estilo Unix) |  **float**  |    time.time()    |

Como regla general todos los atributos son accedidos mediante sus respectivos métodos **set** y **get**. Generalmente los métodos set devolverán **True** siempre y cuando el valor haya sido cambiado y **False** en caso contrario.

![UML VM](https://raw.githubusercontent.com/jcpulido97/ProyectoIV/master/doc/VM.png)