# merger
Takes a CloudGenix yaml config file and a file containing the configuration to be added to the yaml file and inserts it

Sample Usage: mergery.py SAMPLE-SITE.yml config_to_add.txt

Script will then prompt the user for where to insert the config_to_add. It will insert it on the line after this text input.  A useful spot in a CloudGenix yaml config file would be "element_extensions" when adding lengthy extensions for example.

The new output file will be identified.

./merger.py SAMPLE-SITE.yml config_to_add.txt
Enter string to append after (e.g. "element_extensions": element_extensions
Done! New File is:  SAMPLE-SITE_2.yml
