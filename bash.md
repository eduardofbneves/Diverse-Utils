# Bash

## Shotcuts
<kbd>Alt</kbd>
_Win - abre atividades
_Alt+F2 - comando de 1 linha
_Alt+Esc - trocar janelas na mesma workspace
_Win+PageUP/Down - trocar entre workspaces
_Shift+Win+PageUp/Down - mover janela para outra workspace
_Win+A - lista de aplicações
_Shift+Win+-> - mover janela para outro monitor
_Win+V - notificações
_Win+D - desktop

CHECK SPECS
$ lspci
$ inxi -G [graphics]

## DIRETORIAS E PERMISSÕES
_remover dir
	$ rm -r dir

_system control status
systemctl status

_verificar utilizador
$ whoami

_mover todos os ficheiros de uma dir
	$ mv  -v ~/Downloads/* ~/Videos/

_pesquisar ficheiros começados por
$ apt-cache pkgnames <prefixo>

_ouvir em portas
$ netstat

_localizar ficheiro específico
$ locate <ficheiro>

_dar permissões a um utilizador para editar diretoria
$ sudo chown -R {user}:{user} public
INSTALAR

_.run - ficheiros executáveis
	$ chmod +x app.run
	$ ./app.run (sudo se não der)

_.exe - ficheiros Win
	$ chmod +x app.exe
	Instalar com Wine

_.deb - ficheiros deb
	$ sudo dpkg -i package_file.deb.


APPS
~/.local/share/applications
/usr/share/applications

_repositories
$ add-apt-repository
$ wget

_uninstall
$ *command* remove app --purge (remove pacotes ligados)

REMOVE
_remove a PPA
 - Software and Updates app
 - Other Software

_remove repository update
 - $ sudo nano /etc/apt/sources.list
 - delete de lines that are not needed

_remove repository
 $ sudo add-apt-repository remove


THEMES
gnome-tweaks
 
XINPUT
	$ xinput list
	$ xinput list-props [id]
 	$ xinput set-prop [id] [prop] [value]

xinput set-prop 11 287 1

PYTHON
_setup.py
	$ python3 setup.py build
	$ python3 setup.py install

SCREENSHOT
_snip screeshot: Shift + Prt Scrn

PERMISSIONS
sudo chmod eduardo:eduardo *pasta*