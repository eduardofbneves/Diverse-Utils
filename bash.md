# Bash

## Shotcuts
<kbd>Alt</kbd>

<kbd>Win</kbd> - opens activities

<kbd>Alt</kbd> + <kbd>F2</kbd> - one line command

<kbd>Win</kbd> + <kbd>PgUp</kbd>/<kbd>PgDw</kbd> - switch to upper/lower workspace

<kbd>Shift</kbd> + <kbd>Win</kbd> + <kbd>PgUp</kbd>/<kbd>PgDw</kbd> - send window to upper/lower workspace

<kbd>Win</kbd> + <kbd>A</kbd> - applications

<kbd>Win</kbd> + <kbd>V</kbd> - notifications

<kbd>Win</kbd> + <kbd>D</kbd> - desktop


## Machine info and check

Displays information about all Peripheral Component Interconnect (PCI) **buses and devices connected to the system**:
```bash
$ lspci
```

**System control status**:
```bash
$ systemctl status
```


## Directories

**Remove** non-empty directory (recursively):
```bash
$ rm -r <dir>
```

## Permissions

Check **user**:
```bash
$ whoami
```

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