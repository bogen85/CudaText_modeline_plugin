Plugin for CudaText.
Handles modeline processing, specific to CudaText.
Similar to VIM modelines https://howtoforge.com/tutorial/vim-modeline-settings but using a different syntax.
# CudaText: lexer_file=None; tab_size=2; tab_spaces=Yes;

Checks for modeline (typically in a comment) in the first 5 lines of the text file.

Modeline is read from the the remainder of the first line containing " CudaText: " (no quotes).

Modeline uses the HTML Cookie list format.
See https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie#syntax

Values with spaces in them, like some lexer names have, need to have double quotes around the value.

Property names are the same as the property names in the  in the CudaText API without the leading PROP_ prefix
https://wiki.lazarus.freepascal.org/CudaText_API#Properties

Property names are treated with case-insensitivity.

Currently only 4 properties are accepted.

Name        Value type                          Description
----        ----------                          -----------
lexer_file  string                              lexer name
tab_size    integer                             tab width in spaces
tab_spaces  boolean (or fuzzy equivalent)       true for soft tabs (spaces), false for hard tabs.
newline     string (one of "cr", "lf", "crlf")  line endings

Boolean and newline values are treated with case-insensitivity.
Lexer name is case-sensitive.

boolean matches are:

True:  "on", "yes", "1", "true", "enable", "enabled"
False: "off", "no", "0", "false", "disable", "disabled"

Examples:

# python file with a tab width of 4 using soft tabs and CRLF line endings
# CudaText: lexer_file=Python; tab_size=4; tab_spaces=Yes; newline=CRLF;

# Makefile with a tab width of 8 using hard tabs
# CudaText: lexer_file=Makefile; tab_size=8; tab_spaces=No;

# bash script with a tab width of 2 using soft tabs
# CudaText: lexer_file="Bash script"; tab_size=2; tab_spaces=Yes;

// Rust source file with a tab width of 2 using soft tabs and LF line endings
// CudaText: lexer_file=Rust; tab_size=2; tab_spaces=Yes; newline=LF;
