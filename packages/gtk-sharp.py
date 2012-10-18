class GtkSharpPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'gtk-sharp', '2-12-branch')
		self.commit = 'b078aacaf263af84605812d778b62afbdf3e1b59'
		self.source_dir_name = 'mono-gtk-sharp-%s' % self.commit[:7]
		self.configure = './bootstrap-2.12 --prefix="%{prefix}"'
		self.sources = [
			'http://github.com/mono/gtk-sharp/tarball/%{commit}'
		]
		if Package.profile.name == 'darwin':
			self.sources.extend ([
                # workaround against faulty gtk_reparent_* stuff
				# which is broken on gtk-quartz
				# see https://github.com/Dynalon/bockbuild/issues/1
				'https://github.com/Dynalon/gtk-sharp/commit/9b18ce8226312dcc0f03926f0c7e95f77136e218.diff'

			])

	def prep (self):
		Package.prep (self)
		for p in range (1, len (self.sources)):
			self.sh ('patch -p1 < "%{sources[' + str (p) + ']}"')

GtkSharpPackage ()
