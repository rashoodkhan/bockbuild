class GStreamerSharpPackage (GitHubTarballPackage):
	def __init__ (self):
		GitHubTarballPackage.__init__ (self, 'mono-soc-2013', 'gstreamer-sharp',
			'0.1', 'a7bcaf1cf08896190495236b8a8d1a8272201a0b',
			configure = './autogen.sh --prefix="%{prefix}"')

GStreamerSharpPackage ()
