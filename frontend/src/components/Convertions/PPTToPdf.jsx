import Convert from '../Convert'

function PPTToPdf() {
  return Convert("toPdf/pptToPdf", "application/vnd.ms-powerpoint,.pptx");
}

export default PPTToPdf