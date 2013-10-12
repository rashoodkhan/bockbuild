GstreamerXzPackage ('gstreamer', 'gst-plugins-bad', '1.0.10', configure_flags = [
	' --disable-gtk-doc',
	' --with-plugins=quicktime',
	' --disable-apexsink',
	' --disable-bz2',
	' --disable-metadata',
	' --disable-oss4',
	' --disable-theoradec'
])
