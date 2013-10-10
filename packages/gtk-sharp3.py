class GtkSharp3Package (Package):
	def __init__ (self):
		Package.__init__ (self, 'gtk-sharp', '2-12-branch')
		self.commit = '7ce1457c136f13d28adb07fdee7dc06b459bc02c'
		self.source_dir_name = 'mono-gtk-sharp-%s' % self.commit[:7]
		self.configure = './autogen.sh --prefix="%{prefix}"'
		self.sources = [
			'http://github.com/mono/gtk-sharp/tarball/%{commit}'
		]

	def prep (self):
		Package.prep (self)
		return

GtkSharp3Package ()
