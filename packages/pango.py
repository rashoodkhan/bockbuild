class PangoPackage (GnomeXzPackage):
	def __init__ (self):
		GnomePackage.__init__ (self,
			'pango',
			version_major = '1.32',
			version_minor = '4',
			configure_flags = [
				'--without-x'
			]
		)

		self.sources.extend ([
		])

	def prep (self):
		GnomePackage.prep (self)
		return
		self.sh ('patch -p0 < "%{sources[1]}"')
		if Package.profile.name == 'darwin':
			for p in range (2, len (self.sources)):
				self.sh ('patch -p1 < "%{sources[' + str (p) + ']}"')

PangoPackage ()
