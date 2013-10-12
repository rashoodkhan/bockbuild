class GtkSharp3Package (Package):
	def __init__ (self):
		Package.__init__ (self, 'gtk-sharp', '2-12-branch')
		self.commit = '72b51cc71259571e368115e6dec94a6b3b01eeb0'
		self.source_dir_name = 'mono-gtk-sharp-%s' % self.commit[:7]
		self.configure = './autogen.sh --prefix="%{prefix}"'
		self.sources = [
			'http://github.com/mono/gtk-sharp/tarball/%{commit}'
		]

	def prep (self):
		Package.prep (self)
		return

GtkSharp3Package ()
