class PangoPackage (GnomeXzPackage):
	def __init__ (self):
		GnomePackage.__init__ (self,
			'pango',
			version_major = '1.30',
			version_minor = '0',
			configure_flags = [
				'--without-x'
			]
		)

	def prep (self):
		GnomePackage.prep (self)

PangoPackage ()
