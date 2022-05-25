/** @format */

import Convert from "../Convert";

function WordToPdf() {
	return Convert(
		"toPdf/wordToPdf",
		"application/vnd.openxmlformats-officedocument.wordprocessingml.document,.docx,application/msword,.doc",
	);
}

export default WordToPdf;
