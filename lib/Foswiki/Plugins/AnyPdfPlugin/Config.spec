#---+ Extensions
#---++ AnyPdfPlugin

# **PATH**
# Location of the Pdf-Creator executable.
$Foswiki::cfg{Plugins}{AnyPdfPlugin}{pdfcmd} = '/usr/bin/phantomjs';

# **STRING**
# Parameters passed to the Pdf-Creator before the file name.
$Foswiki::cfg{Plugins}{AnyPdfPlugin}{pdfparams} = '/usr/share/phantomjs/examples/rasterize.js';

# **STRING**
# Parameters passed to the Pdf-Creator after the file name.
$Foswiki::cfg{Plugins}{AnyPdfPlugin}{pdfformat} = 'A4';

# **BOOLEAN**
# Enable debugging (debug messages will be written to working/logs/debug.log)
$Foswiki::cfg{Plugins}{AnyPdfPlugin}{Debug} = 0;


1;
