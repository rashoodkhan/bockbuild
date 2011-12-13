Package ('libgcrypt', '1.5.0', sources = [
	'ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2'
],
	configure_flags = [ '--disable-asm' ]
)
