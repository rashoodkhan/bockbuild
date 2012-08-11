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
			self.git_branch = 'master'

			self.sources.extend([
				'https://github.com/Dynalon/banshee-osx/pull/1.diff',

				# https://bugzilla.gnome.org/show_bug.cgi?id=677866
				'http://bugzilla-attachments.gnome.org/attachment.cgi?id=217548',

				# watch out: this patch might not make it into master
				# see the bgo report at
				# https://bugzilla.gnome.org/show_bug.cgi?id=679252
				'http://bugzilla-attachments.gnome.org/attachment.cgi?id=217821',

				# code cleanup, remove VolumeButton and use gtk
				# https://bugzilla.gnome.org/show_bug.cgi?id=681062
				# 'http://bugzilla-attachments.gnome.org/attachment.cgi?id=220140',

				# fix volume reset between changing tracks
				# https://bugzilla.gnome.org/show_bug.cgi?id=681639
				'https://bugzilla.gnome.org/attachment.cgi?id=220919'
			])

# you can set force_latest_git_mater to True when you want to build latest
# source from git for testing purposes but use packages from the release list
BansheePackage (force_latest_git_master = False)
