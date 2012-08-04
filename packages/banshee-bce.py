class BansheeBcePackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'banshee-community-extensions', 'master')

		self.sources = [
			'git@gitorious.org:~dynalon/banshee-community-extensions/banshee-community-extensions-macosx.git',
		]
		self.git_branch = 'master'

		self.configure = [ 'NOCONFIGURE=1 ./autogen.sh && ./profile-configure %{profile.name} --prefix=%{prefix}' ]

	def prep (self):
		Package.prep (self)
		for p in range (1, len (self.sources)):
			self.sh ('patch -p1 < "%{sources[' + str (p) + ']}"')

BansheeBcePackage ()
