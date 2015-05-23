# README #

### Summary ###

A ChatScript syntax file to use with Sublime Text 2, should work with ST3 too. It should also work with other IDE that support tmLanguage files. The matching rely on Oniguruma Regex rules. 

I use Monokai as my ST color scheme, but it should look fine with others as well.

Version 0.5
May 2015

### Usage ###
* Put the *Chatscript.tmLanguage* file in your Package/User folder
** Windows: %APPDATA%\Sublime Text 2
** OSX: ~/Library/Application Support/Sublime Text 2
** Linux: ~/.config/sublime-text-2
* Restart Sublime Text 2
* You can now select View/Syntax/Chatscript from the menu!

### Dev ###
* Install the AAAPackageDev in ST3 
* Edit the regex rules in the JSON-tmLanguage file 
* Compile/build the tmLanguage file from the JSON-tmLanguage by doing build (CTRL+B) and choosing "property list"
*Please stay consistent with the color scheme if you contribute 

### Refs ###
* http://docs.sublimetext.info/en/latest/extensibility/syntaxdefs.html#your-first-syntax-definition
* http://manual.macromates.com/en/language_grammars#naming_conventions.html
* http://www.geocities.jp/kosako3/oniguruma/doc/RE.txt
* http://chatscript.sourceforge.net/Documentation/
* http://tmtheme-editor.herokuapp.com/#/theme/Monokai