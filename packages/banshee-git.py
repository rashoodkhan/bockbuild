class BansheePackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'banshee', 'master')

		self.sources = [
			'git://git.gnome.org/banshee'
		]
		self.git_branch = 'master'

		self.configure = [ 'NOCONFIGURE=1 ./autogen.sh && ./profile-configure %{profile.name} --prefix=%{prefix}' ]
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
			'http://bugzilla-attachments.gnome.org/attachment.cgi?id=220140',
		])

	def prep (self):
		Package.prep (self)
		for p in range (1, len (self.sources)):
			self.sh ('patch -p1 < "%{sources[' + str (p) + ']}"')

BansheePackage ()
