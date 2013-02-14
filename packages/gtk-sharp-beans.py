class GtkSharpBeansPackage (GitHubTarballPackage):
	def __init__ (self):
		GitHubTarballPackage.__init__ (self, 'mono', 'gtk-sharp-beans',
			'2.14.0', 'a2ff3c5dcf1e34141d0666e1d5268c4ba4f421bd',
			configure = './autogen.sh --prefix="%{prefix}"')

GtkSharpBeansPackage ()
