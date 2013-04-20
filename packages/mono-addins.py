Package ('mono-addins', '0.6.2',
	sources = [
		'http://download.mono-project.com/sources/mono-addins/%{name}-%{version}.tar.bz2'
	],
	configure = './configure --enable-gui=no --prefix="%{prefix}"'
)
