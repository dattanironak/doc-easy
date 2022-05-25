import Convert from '../Convert'

function ExcelToPdf() {
  return Convert("toPdf/excelToPdf", "application/vnd.ms-excel,.xlsx");
}

export default ExcelToPdf