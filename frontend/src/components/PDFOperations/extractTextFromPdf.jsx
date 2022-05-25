import Convert from '../Convert'

function extractTextFromPdf() {
  return Convert("pdfop/extract", "application/pdf");
}

export default extractTextFromPdf