# z

a zathura wrapper script for displaying **markdown** and pdf files

## requirements

* [pandoc](https://pandoc.org/)
* latex or [wkhtmltopdf](https://wkhtmltopdf.org/) for md2pdf conversion
* or if you want to dockerize pandoc, [dalibo/pandocker](https://github.com/dalibo/pandocker/) is amazing but keep in mind that it will be slow and the script will have to be modified to accomodate volumes and output file

## todo

* cache the file and check hashes for file change
