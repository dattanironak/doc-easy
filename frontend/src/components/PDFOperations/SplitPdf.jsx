
import Convert from '../Convert'

function SplitPdf() {
  return Convert("pdfop/splitpdf", "application/pdf");
}

export default SplitPdf