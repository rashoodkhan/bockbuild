class BansheeBasePackage (Package):
	def __init__ (self, version):
		Package.__init__ (self, 'banshee', version)

		self.sources = [
			'git://git.gnome.org/banshee'
		]

		self.configure = [ 'NOCONFIGURE=1 ./autogen.sh && ./profile-configure %{profile.name} --prefix=%{prefix}' ]

	def prep (self):
		Package.prep (self)
		for p in range (1, len (self.sources)):
			self.sh ('patch -p1 < "%{sources[' + str (p) + ']}"')

class BansheePackage (BansheeBasePackage):
	def __init__ (self, force_latest_git_master = False):
		global BansheeBasePackage;

		if (Package.profile.cmd_options.release_build and not force_latest_git_master):
			BansheeBasePackage.__init__ (self, 'banshee-2.4')
			# release build, specify stable git branch
			self.git_branch = 'stable-2.4'

			self.sources.extend([
				# switch over from ige_* to gtk_* binding
				'http://git.gnome.org/browse/banshee/patch/?id=d71b1031124424fcfa226536c57a4575a635ad7c'
			])

		else:
			BansheeBasePackage.__init__ (self, 'master')
			# non-release build, use latest git master
			self.git_branch = '2.5.0'

			self.sources.extend([
			])

# you can set force_latest_git_mater to True when you want to build latest
# source from git for testing purposes but use packages from the release list
BansheePackage (force_latest_git_master = False)
