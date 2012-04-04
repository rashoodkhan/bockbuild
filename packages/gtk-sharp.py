class GtkSharpPackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'gtk-sharp', '2-12-branch')
		self.commit = 'a0d89be14edb8da9e1654c57a490689b19dea4fd'
		self.source_dir_name = 'Dynalon-gtk-sharp-%s' % self.commit[:7]
		self.configure = './bootstrap-2.12 --prefix="%{prefix}"'
		self.sources = [
			'http://github.com/Dynalon/gtk-sharp/tarball/%{commit}'
		]

GtkSharpPackage ()
