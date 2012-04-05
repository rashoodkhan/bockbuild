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

		self.sources.extend ([
			# 1
			# Bug 321419 - Allow environment var substitution in Pango config
			# https://bugzilla.gnome.org/show_bug.cgi?id=321419
			'http://bugzilla-attachments.gnome.org/attachment.cgi?id=96023',
			
		])

	def prep (self):
		GnomePackage.prep (self)
		self.sh ('patch -p0 < "%{sources[1]}"')

PangoPackage ()
