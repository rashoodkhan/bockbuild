class GlibPackage (GnomeXzPackage):
	def __init__ (self):
		GnomePackage.__init__ (self,
			'glib',
			version_major = '2.35',
			version_minor = '3')

		self.darwin = Package.profile.name == 'darwin'

		if Package.profile.name == 'darwin':
			#link to specific revisions for glib 2.30.x
			self.sources.extend ([
			])

	def prep (self):
		Package.prep (self)
		if self.darwin:
			for p in range (2, len (self.sources)):
				self.sh ('patch -p0 < %{sources[' + str (p) + ']}')
	
	def build (self):
		Package.build (self)

	def install (self):
		Package.install (self)
		if self.darwin:
			# FIXME: necessary?
			return
			self.sh ('rm %{prefix}/lib/charset.alias')

GlibPackage ()
