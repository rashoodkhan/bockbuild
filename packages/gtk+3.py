class Gtk3Package (GnomeXzPackage):
	def __init__ (self):
		GnomeXzPackage.__init__ (self, 'gtk+',
			version_major = '3.8',
			version_minor = '1',
			configure_flags = [
				'--disable-x11-backend',
				'--enable-quartz-backend',
#				'--enable-introspection',
				'--disable-colord',
				'--without-atk-bridge',
				'--prefix="%{prefix}"'
			]
		)
		self.configure = './configure'

		if Package.profile.name == 'darwin':
			self.sources.extend ([
			])

	def prep (self):
		Package.prep (self)
		if Package.profile.name == 'darwin':
			for p in range (2, len (self.sources)):
				self.sh ('patch -p1 < "%{sources[' + str (p) + ']}"')

	def install(self):
		Package.install(self)
		return
		self.install_gtkrc ()

	def install_gtkrc(self):
		return
		origin = os.path.join (self.package_dest_dir (), os.path.basename (self.sources[1]))
		destdir = os.path.join (self.prefix, "etc", "gtk-2.0")
		if not os.path.exists (destdir):
			os.makedirs(destdir)
		self.sh('cp %s %s' % (origin, destdir))

Gtk3Package ()
