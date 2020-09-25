""" Modulo para cortar "inteligentemente" PDF's

Este programa trata de buscar las diapositivas de un PDF que 
contengan informacion redundante (que este preparado para te_
ner animaciones durante la presentacion, pero es incomod cuan_
do se necesita estudiarlos).

Usage:
	pypdf.py <file> [-o <o_file>] [--reverse]

Options:
	-h --help     Mostrar esta ayuda.
	-r --reverse  Orden para ciclar el archivo.
"""

import re
import PyPDF4 as pypdf
from docopt import docopt


def extract_text(pageObj):
	""" Funcion para extraer contenido de diapositivas. """
	text = pageObj.extractText()
	return re.sub("[\n\r\s]+", "", text)


def if_match(page, other_page):
	""" Funcion para definir la similaridad entre diapositivas. """
	return page.startswith(other_page)


def match_srch(pdf, reverse=True):
	""" Buscador de similaridades.

	Funcion para verificar la equivalencia entre las
	paginas y el orden para verificar.

	Input:
		reverse := Indica si revisar de adelante a atras
			(False) o de atras a adelante (True)
	Output:
		exlude_pages := lista de paginas que presentan
			similaridad con otras.
	"""
	num_pages = pdf.numPages
	prev_page_text = extract_text(pdf.getPage(0))
	exclude_pages = []

	pages = range(num_pages-1,0,-1) if reverse else range(1,num_pages)

	for num_pg in pages:
		page_text = extract_text(pdf.getPage(num_pg))

		if if_match(page_text, prev_page_text):
			exclude_pages.append(num_pg)
		prev_page_text = page_text

	return exclude_pages


def trim_file(i_name, o_name,/, reverse=True):
	""" Funcion para eliminar paginas repetidas en archivo.
	
	Input:
		i_name := nombre del archivo de entrada.
		o_name := nombre del archivo de salida.
		reverse := direccion en la que se cicla el archivo.
			- False de arriba a abajo
			- True de abajo a arriba [default]
	"""
	# Init files
	inp_f = pypdf.PdfFileReader(i_name, 'rb')
	out_f = pypdf.PdfFileWriter()
	
	# Get exclude pages
	exclude_pages = match_srch(inp_f, reverse=reverse)
	
	# Create new pdf
	for num_pg in range(inp_f.numPages):
		if num_pg not in exclude_pages:
			pg = inp_f.getPage(num_pg)
			out_f.addPage(pg)
	
	# Write the pdf files
	with open(o_name, 'wb') as pdf:
		out_f.write(pdf)



def main(args):
	reverse = not args['--reverse'] # Default it's True
	i_name = args['<file>']
	o_name = args['<o_file>'] if args['-o'] else 'trimed-'+i_name 

	trim_file(i_name, o_name, reverse)

if __name__ == '__main__':
	args = (docopt(__doc__))
	main(args)
