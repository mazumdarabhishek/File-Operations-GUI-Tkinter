from PyPDF2 import PdfFileMerger, PdfFileReader
class pdf_op:

    def get_pdfs(self,list=[]):
        paths = []
        for f in list:
            if f.endswith('.pdf'):
                paths.append(f)
        return paths

    def merge_pdf(self,list=[],output_file=''):
        merger = PdfFileMerger()
        for unit in list:
            merger.append(PdfFileReader(unit),'rb')
        merger.write(output_file)


