class GstreamerPackage (GstreamerXzPackage):
        def __init__ (self):
                GstreamerXzPackage.__init__ (self,
                        project  = 'gstreamer',
                        name = 'gstreamer',
                        version = '1.0.10')

                self.configure = './configure --disable-gtk-doc --prefix="%{prefix}"'

        def prep (self):
                Package.prep (self)

GstreamerPackage ()
