class GioSharpPackage (GitHubTarballPackage):
	def __init__ (self):
		GitHubTarballPackage.__init__ (self, 'mono', 'gio-sharp',
			'0.3', 'a9468300a2b3de749d1e85746ccab65241be28c1',
			configure = './autogen-2.22.sh --prefix="%{prefix}"')

GioSharpPackage ()
