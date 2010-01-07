from profile import Profile

class UnixProfile (Profile):
	def __init__ (self):
		Profile.__init__ (self)
		self.name = 'unix'

		self.gcc_arch_flags = [ '-m32', '-arch i386' ]
		self.gcc_flags = [ '-I%{prefix}/include' ]

		self.env.set ('PATH', ':',
			'%{prefix}/bin',
			'/usr/bin',
			'/bin')
		
		self.env.set ('CFLAGS', ' ',
			'%{gcc_flags}', 
			'%{gcc_arch_flags}')
		self.env.set ('CXXFLAGS',        '%{env.CFLAGS}')
		self.env.set ('CPPFLAGS',        '%{env.CFLAGS}')
		self.env.set ('C_INCLUDE_PATH',  '%{prefix}/include')

		self.env.set ('LD_LIBRARY_PATH', '%{prefix}/lib')
		self.env.set ('LDFLAGS', ' ',
			'-L%{prefix}/lib', 
			'%{gcc_arch_flags}')

		self.env.set ('ACLOCAL_FLAGS',   '-I%{prefix}/share/aclocal')
		self.env.set ('PKG_CONFIG_PATH', ':',
			'%{prefix}/lib/pkgconfig',
			'%{prefix}/share/pkgconfig')