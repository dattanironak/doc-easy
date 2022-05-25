/** @format */

import React from "react";

function Input(props) {
	var operation = window.location.pathname;
    console.log(operation)
	if (operation === "/mergepdf") {
		return (
			<input
				className="file-input "
				type="file"
				ref={props.Ref}
				id="inputFile"
				accept=".pdf"
				onChange={props.onChange}
				multiple
			/>
		);
	}
	if (operation === "/imgtopdf")
		return (
			<input
				className="file-input "
				type="file"
				ref={props.ref}
				id="inputFile"
				accept={props.FileType}
				onChange={props.onChange}
			/>
		);


    return (
			<input
				className="file-input "
				type="file"
				ref={props.Ref}
				id="inputFile"
				accept={props.FileType}
				onChange={props.onChange}
			/>
		);
}

export default Input;
