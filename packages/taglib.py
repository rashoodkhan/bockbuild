Package ('taglib', '1.7', 
	sources = [
		'http://developer.kde.org/~wheeler/files/src/%{name}-%{version}.tar.gz'
	],
	override_properties = {
		'configure': './autogen.sh ; cmake '
			'[-DCMAKE_INSTALL_PREFIX=%{prefix}] '
			'[-Dlibdir=%{prefix}/lib] '
			'[-Ddatadir=%{prefix}/share] '
			'.'
	}
)
