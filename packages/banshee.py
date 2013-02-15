class BansheeBasePackage (Package):
	def __init__ (self, version):
		Package.__init__ (self, 'banshee', version)

		self.sources = [
			'git://git.gnome.org/banshee',
			# workaround against broken gtk_reparent_*  on gtk-quartz
			'https://github.com/Dynalon/banshee-osx/commit/798ba9ad74f91b1bc9e7ad7c36d6044fceb7a1d5.diff',

			# bugfix for corrupted .dmg background
			'http://bugzilla-attachments.gnome.org/attachment.cgi?id=229975',

			# disable gio-* hw, bgo#693903
			'https://bugzilla.gnome.org/attachment.cgi?id=236272',
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
			BansheeBasePackage.__init__ (self, 'banshee-2.6')
			# release build, specify stable git branch
			self.git_branch = 'stable-2.6'

			self.sources.extend([
			])

		else:
			BansheeBasePackage.__init__ (self, 'master')
			# non-release build, use latest git master
			self.git_branch = 'master'

			self.sources.extend([
			])

# you can set force_latest_git_mater to True when you want to build latest
# source from git for testing purposes but use packages from the release list
BansheePackage (force_latest_git_master = True)
