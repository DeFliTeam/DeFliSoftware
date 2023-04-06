#
# DeFliSoftware client-side top-level Makefile
#

# The sub-makefiles understand these variables:

# DESTDIR: a prefix put before all destination paths when installing (used for packaging)
# PREFIX: the base directory to install to, defaults to /usr
# TCLLAUNCHER: path to a tcllauncher binary to install, defaults to tcllauncher from $PATH
# TCLSH: path to a tclsh to use to build package indexes, defaults to tclsh/tcl8.5/tcl8.6 from $PATH
#
# (also see scripts/Makefile for systemd/sysvinit install options)

all:
	@echo "'make install' as root to install client package and program"

install:
	$(MAKE) -C package install
	$(MAKE) -C programs/defli install
	$(MAKE) -C programs/defli-config install
	$(MAKE) -C programs/defli-status install
	$(MAKE) -C programs/pirehose install
	$(MAKE) -C doc install
	$(MAKE) -C scripts install
	$(MAKE) -C etc install

clean:
	$(MAKE) -C package clean
