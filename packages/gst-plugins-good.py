class GstPluginsGoodPackage (GstreamerXzPackage):
	def __init__ (self):
		GstreamerXzPackage.__init__ (self, 'gstreamer', 'gst-plugins-good',
			'1.0.10', configure_flags = [
				'--disable-gtk-doc',
				'--disable-gdk_pixbuf',
				'--disable-cairo',
				'--disable-jpeg',
				'--disable-libpng',
				'--disable-deinterlace',
				'--disable-taglib',
				'--disable-annodex'
			]
		)

		# FIXME: these should be passed on the Linux profile
		# when we do away with xvideo/xoverlay and replace
		# with Clutter and Cairo
		if Package.profile.name == 'darwin':
			self.configure_flags.extend ([
				'--disable-x',
				'--disable-gtk-doc',
				'--disable-cairo',
				'--disable-cairo_gobject',
				'--disable-xvideo',
				'--disable-deinterlace',
				'--disable-xshm'
			])

GstPluginsGoodPackage ()
