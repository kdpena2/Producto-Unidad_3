# Producto-Unidad_3

****PUERTOS GPIO Y POO EN LA RESOLUCIÓN DE PROBLEMAS****
<p>REQUERIMIENTOS. • Se debe implementar los 2 enunciados empleando Python y simulado en una Raspberry Pi. • No se debe ingresar datos por consola. • El programa debe presentar en pantalla información relacionada a lo que se está realizando. • Se debe emplear conceptos de POO. • Cada enunciado se implementará en una clase con sus funciones. • Se debe emplear un programa de selección (clase) que permita seleccionar la ejecución de los programas. • El programa principal es crear objetos de cada clase y llamar a las funciones que correspondan para que opera la lógica de negocio del problema. </p>


****PROBLEMA:****
 <p>¿Cuál es la  configuración de la tarjeta de desarrollo Raspberry Pi , usando Poo para el desarrollo de problemas de lógica digital ? </p>
****OBJETIVO GENERAL:****
 <p>Investigar los usos ,estructuras y parámetros de configuración de la tarjeta de desarrollo Raspberry Pi usando el paradigma de Programación Orientada a Objetos, a través de  la abstracción  y análisis de información,para su desarrollo y aplicación en la resolución de los problemas planteados. </p>
****OBJETIVOS ESPECÍFICOS:****
<p><li> Identificar documentos recientes que tengan información acerca de la tarjeta de desarrollo Raspberry Pi, para de esta manera generar un concepto básico del objeto a investigar y las distintas aplicaciones en las que se encuentran.</li></p>
<p><li>Comprender los usos y funcionalidades de la tarjeta enfocándonos en el paradigma Poo.</li></p>
<p><li>Desarrollar los problemas planteados donde se evidencie el  funcionamiento de la tarjeta.</li></p>

****ESTADO DEL ARTE****
***Sistema de riego por goteo inteligente con frambuesa pi y arduino***
<p>Nikhil Agrawal y Smita Singhal</p>
<p>Siemens, Noida</p>

<p>En este estudio se propuso como objetivo principal  desarrollar  para un sistema de automatización del hogar mismo que utiliza dispositivos rentables y energéticamente eficientes, incluyendo  raspberry pi, microcontroladores arduino y otros . El uso de estos componentes  en conjunto garantiza  una implementación del sistema robusta, escalable y rentable . Los comandos necesarios para la configuración de Raspberry pi se realizaron utilizando el lenguaje de programación Python.Los microcontroladores Arduino son usados para recibir los comandos de encendido / apagado del raspberry pi mediante el protocolo zigbee. La topología en estrella zigbee sirve como columna vertebral para la comunicación entre raspberry pi y los dispositivos finales. En este caso Raspberry pi actuará  como un coordinador central mientras  los dispositivos finales actúan como varios enrutadores. Es así que basándose en el sistema de hogar inteligente se propone un sistema de riego por goteo económico y energéticamente eficiente. El diseño puede ser empleado  en grandes campos agrícolas, así como en pequeños jardines, simplemente enviando un correo electrónico al sistema para regar las plantas. Este sistema funciona de la siguiente manera, el uso de sensores de ultrasonido y válvulas solenoides genera un sistema de riego por goteo inteligente.Pi envía y recibe comandos desde y hacia el microcontroladores arduino que utilizan los módulos zigbee.La programación se realiza tanto para pi como para arduino usa python y bibliotecas y funciones centrales de arduino respectivamente para comunicación adecuada a través de zigbee, usando este sistema, las válvulas solenoides y la placa de relés se pueden controlar de forma remota que abre las oportunidades para controlar el agua flujo así como el flujo eléctrico.
Este inteligente sistema de riego por goteo demuestra ser útil sistema ya que automatiza y regula el riego sin cualquier intervención manual. Envío de correos electrónicos al sistema se puede automatizar, pero el envío manual de los correos electrónicos control sobre el sistema con respecto a si ejecutar o no el sistema dependiendo de las condiciones climáticas. </p>

<p>Fecha de la conferencia: 15-16 de mayo de 2015</p>
<p>Fecha de adición a IEEE Xplore : 06 de julio de 2015</p>

<p>Este estudio en relación al nuestro contiene aspectos similares como el empleo de un Raspberry pi para controlar un sistema de riego en el que mediante programación en Python se han establecido diversas condiciones para que funcione bajo ciertas circunstancias, sin embargo, a diferencia del nuestro en este se ha empleado otros dispositivos como Arduino que le ayudan a Raspberry a captar los datos del exterior para procesarlos y enviar una respuesta de activado-apagado para el rociador de agua.</p>

***Sistema de gestión de incendios inteligente basado en Raspberry pi que emplea un rociador de agua automático basado en sensores***
<p>Noorinder, Jaspreet Singh  y Ekambir Sidhu</p>
<p>Departamento de Ingeniería Electrónica y Comunicaciones, Universidad de Punjabi, Patiala, India</p>

<p>En este estudio se propone la creación de un sistema de incendios inteligente basado en Raspberry, dicha gestión inteligente de incendios requiere de  sistemas de vigilancia para detectar y controlar el fuego y a los agentes que lo provocan automáticamente. Es por ello que para cubrir este requisito  se ha usado una Raspberry pi. Este diseño  incluye detectores de llamas junto con sensores de temperatura que reducen la tasa de detección de incendios falsos. Además, se notifica al usuario enviando por correo electrónico el video del área afectada por el incendio y brinda actualizaciones de la temperatura ambiente.Para su ejecución se ha empleado un sensor de fugas de gas para detectar varios tipos de gases como etano, metano, GLP, etc. Se han empleado rociadores de agua que se activarán en la detección de incendio por los sensores de incendio, es decir, que si la temperatura se eleva por encima del umbral establecido, el sistema propuesto también enviará el correo al cuerpo de bomberos junto con el video y notificará al usuario para que informe al cuerpo de bomberos manualmente. Este sistema propuesto se puede instalar en una sala de un área máxima de 126 pies × 21 pies empleando un módulo Raspberry pi.El sistema implica una válvula para controlar la apertura de una tubería que se ha instalado en cada sección. Esta válvula solenoide se activa solo cuando los sensores de llama IR detectan la llama.Cuando se detecta la llama, los sensores de llama IR envían lógica señal de salida alta al controlador. El controlador compara el valor de temperatura medido por el sensor de temperatura con el establecer el valor de umbral. Si el valor de la temperatura supera la temperatura de 303F (30 grados Celsius), el Raspberry pi realiza las operaciones de control de incendios que implican apagar el fuego con los rociadores de agua.</p>

<p>Fecha de la conferencia: 16-18 de marzo de 2017</p>
<p>Fecha de adición a IEEE Xplore : 26 de octubre de 2017</p>

<p>Esta investigación en comparación con la nuestra presenta diversas similitudes ya que permite detectar una señal de humo o de otros gases, misma que es obtenida desde un sensor de llama IR  y enviada a la Raspberry pi para que mediante las condiciones establecidas compare si la señal recibida sobrepasa los niveles del umbral establecido,en cambio a diferencia de nuestro trabajo este sistema integra Iot lo que permite enviar al usuario una notificación de la temperatura a su email e inclusive una fotografía de la zona afectada.</p>

****MARCO TEÓRICO****

***Pines GPIO (General Purpose Input Output):***
<p>General Purpose Input Output (GPIO) se trata de un sistema de entrada y salida de propósito general, este consta de una serie de pines o conexiones que se pueden usar como entradas o salidas. Estos pines son digitales, lo que significa que sólo pueden tener dos estados. Tienen una dirección para recibir o enviar corriente (entrada, salida respectivamente) y todo esto es controlable por lenguajes de programación como Python, JavaScript, node-RED, entre otros. Los pines trabajan con una tensión de 3,3 V y un consumo máximo de corriente de 16 mA. </p>

***Control de GPIO con Python ***
<p>Para esto, lo primero es importar la librería que trabaja con la raspberry pi, la cual es RPi.GPIO.</p>
Existen dos maneras de identificar la nomenclatura de los pines:
 <p><li>Board: Este es el método más simple, y se refiere a la ubicación física de los pines. Empezando por la parte superior izquierda del GPIO, se encuentra el pin físico 1 que proporciona alimentación 3v3. A la derecha de ese pin se encuentra el 2 que proporciona 5v de potencia. El número de pines seguirá creciendo a medida que se desciende por las columnas. A la izquierda se encontrarán todos los pines con números impares y a la derecha los pares. </li></p>
 <p><li>Broadcom: La numeración de pines de Broadcom (BCM), se refiere a los pines que están conectados directamente al SoC del Raspberry Pi. Se puede decir que sus conexiones son directas al cerebro de la raspberry.</li></p>


***Tipos de pines de la Raspberry***
*****imagen*****

<p><li>Pines de alimentación: Se puede apreciar pines de 5v, 3v3 (limitados a 50 mA) y tierra (GND o Ground), que aportan alimentación a estos voltajes para los circuitos. </li></p>
<p><li>DNC (Do Not Connect): son pines que por el momento no tienen función, pero en futuras implementaciones si son utilizados. Se encuentran en modelos más primitivos de la Raspberry Pi. En las actuales placas han sido marcados como GND.</li></p>
<p><li>GPIO normales: son conexiones configurables que se pueden programar para los distintos proyectos.</li></p>
<p><li>GPIO especiales: dentro de éstos se encuentran algunos pines destinados a una interfaz UART, con conexiones TXD y RXD que sirven para comunicaciones en serie. También podemos ver otros como SDA, SCL, MOSI, MISO, SCLK, CE0, CE1, etc…, entre ellos destacan:</li></p>
PWM con el que se puede regular el ancho del pulso.
SPI es una interfaz de comunicación.
I2C está compuesto por la señal de datos (GPIO2) y el reloj (GPIO3). Además de EEPROM Data (GPIO0) y EEPROM Clock (GPIO1).
Serial, otra comunicación muy práctica con pines TX (GPIO14) y RX (GPIO15) como los que puedes encontrar en la placa Arduino UNO.

***Programación orientada a objetos (POO) en Python***
<p>Se define como un paradigma de la programación, donde se organiza el código en unidades denominadas clases, de las cuales se crean objetos que se relacionan entre sí para conseguir los objetivos de las aplicaciones. 
Es una forma especial de programar, más cercana a cómo expresamos las cosas en la vida real que otros tipos de programación. </p>

***Ventajas POO***
<p><li>Agiliza el desarrollo de software.</li></p>
<p><li>Facilita el mantenimiento del software.</li></p>
<p><li>Permite crear sistemas más complejos. </li></p>   
<p><li>Fomenta la reutilización y extensión del código.</li></p> 
<p><li>Facilita la creación de programas visuales.</li></p>  
<p><li>Relacionar el sistema al mundo real.</li></p>  
<p><li>Construcción de prototipos.</li></p>
 

***Elementos de POO*** 
***Clases***
<p>Las clases son los modelos o representaciones donde posteriormente se van a crear objetos similares, esta es una plantilla que describe los detalles de un objeto individual.
Se compone de tres cosas: un nombre, atributos y operaciones.  
consta de métodos y de datos que resumen las características comunes de dicho conjunto. 
Las clases son similares a los tipos abstractos de datos y equivalen a modelos que describen cómo se construyen ciertos tipos de objetos. Cada vez que se construye un objeto a partir de una clase estamos creando lo que se llama una instancia de esa clase.</p>  
 
***Objeto***
<p>Se trata de un ente abstracto usado en programación que permite separar los diferentes componentes de un programa, simplificando su elaboración, depuración y posteriores mejoras. 
Los objetos se integran, a diferencia de los métodos procedurales, tanto los procedimientos como las variables y datos referentes al objeto. 
A los objetos se les otorga ciertas características en la vida real. Los objetos se componen de 3 partes fundamentales: métodos, eventos y atributos. </p>

***Métodos de un objeto*** 

<p>Se trata de funciones, pero en POO se les llama métodos y representan acciones que puede realizar el objeto, a más de los servicios que realizará el objeto dentro del programa.
Cuando el objeto es creado podemos acceder a sus propiedades y métodos de una forma muy simple: nombre de objeto seguido de un punto y el método o propiedad a la que se  quiere acceder.  
Siempre el primer parámetro de todos los métodos que se definen en una clase es self, este hace referencia al objeto o instancia que invoca al método.</p>
<p>El método __init__ es un método especial de una clase en Python. El objetivo fundamental de este método es inicializar los atributos del objeto que creamos.</p>
<p>Otras características del método __init__ son:</p>
Se ejecuta inmediatamente luego de crear un objeto.
No puede retornar datos.
Puede recibir parámetros que se utilizan normalmente para inicializar atributos.
Es un método opcional, de todos modos es muy común declararlo.
<p>sintaxis:</p>
<p>def __init__([parámetros]):
        [algoritmo]</p>
 
 
***Atributos***
<p>Características que aplican al objeto solo en el caso en que el sea visible en pantalla por el usuario; entonces sus atributos son el aspecto que refleja, tanto en color, tamaño, posición, si está o no habilitado. 
- Las variables de instancia también denominados miembros datos, son declaradas en la clase pero sus valores son fijados y cambiados en el objeto. Además de las variables de instancia hay variables de clase, las cuales se aplican a la clase y a todas sus instancias.</p>



***Lógica digital***
<p>La lógica digital es una ciencia de razonamiento aplicada a circuitos eléctricos que realizan decisiones de tipo (SI) y (NO), donde una serie de circunstancias particulares ocurre, una acción resultara y siempre es el mismo para una serie dada de circunstancias.</p>
<p>La posibilidad de predecir el resultado final permite el diseño de sistemas digitales a partir de circuitos básicos llamados compuertas, además de la ayuda de la matemática booleana permite la creación de sistemas electrónicos digitales para casi cualquier evento que necesitemos realizar.</p>

****DIAGRAMAS****

*****imagen*****

****LISTA DE COMPONENTES****
<p>Estos son los recursos que se han utilizado a lo largo del desarrollo del trabajo de investigación.</p>

*****imagen*****

****MAPA DE VARIABLES****
 
****EXPLICACIÓN DE CÓDIGO FUENTE****
 
****DESCRIPCIÓN DE PRERREQUISITOS Y CONFIGURACIÓN****

*****imagen*****
 
****APORTACIONES****




****CONCLUSIONES****




****RECOMENDACIONES****



****CRONOGRAMA****



*****imagen*****



****BIBLIOGRAFÍA:****

<p>[1]N. Agrawal and S. Singhal, "Smart drip irrigation system using raspberry pi and arduino," International Conference on Computing, Communication & Automation, Noida, 2015, pp. 928-932, doi: 10.1109/CCAA.2015.7148526.</p>
 
<p>[2]Noorinder, J. Singh and E. Sidhu, "Raspberry pi based smart fire management system employing sensor based automatic water sprinkler," 2017 International Conference on Power and Embedded Drive Control (ICPEDC), Chennai, 2017, pp. 102-106, doi: 10.1109/ICPEDC.2017.8081068.</p>
 
<p>[3]Challenger-Pérez, I., Díaz-Ricardo, Y., & Becerra-García, R. A. (2014). El lenguaje de programación Python. Ciencias Holguín, 20(2), 1-13.
[4]Raihan, M. K. J., Rahaman, M. S., Sarkar, M. K., & Mahfuz, S. (2013). Raspberry Pi image processing based economical automated toll system. Global Journal of Research In Engineering.</p>


