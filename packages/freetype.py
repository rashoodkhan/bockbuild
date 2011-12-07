SourceForgePackage ('%{name}', 'freetype', '2.4.8', override_properties = {
	'configure': './configure --prefix "%{prefix}"'
})
