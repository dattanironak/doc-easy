/** @format */

import React, { useRef, useState, useEffect } from "react";
import axios from "axios";
import Input from "./input";
import "./CSS/main.css";

const Convert = (path, fileType) => {
	const fileUpload = useRef(null);
	const [file, setFile] = useState([]);
	const [state, SetState] = useState("upload");
	const [convertedFile, SetConvertedFile] = useState();

	useEffect(() => {
		console.log(fileType);
	});

	async function readUrl(input) {
		document.getElementById("images-previews").innerHTML = "";

		for (var i = 0; i < input.target.files.length; i++) {
			if (
				input.target.files[i] &&
				(fileType === "application/pdf" || fileType === "image/*")
			) {
				let reader = new FileReader();
				reader.onload = (e) => {
					let imgData = e.target.result;

					document.getElementById(
						"images-previews",
					).innerHTML += `<embed id="file-preview"  class="mx-3 my-2" src='${imgData}'  />`;
				};

				reader.readAsDataURL(input.target.files[i]);
			} else if (input.target.files[i]) {
				document.getElementById(
					"images-previews",
				).innerHTML += `<div id="file-preview class="mx-3 my-2">${i} ${input.target.files[i].name}</div>`;
			}
		}

		setFile([...input.target.files]);
		console.log(file);
	}

	function handleSubmit() {
		console.log(file);
		let formData = new FormData();
		SetState("processing");

		for (var i = 0; i < file.length; i++) {
			console.log(file[i].name);
			formData.append(file[i].name, file[i]);
		}

		if (document.getElementById("pass")) {
			var pass = document.getElementById("pass").value;
			formData.append("password", pass);
		}
		console.log(localStorage.getItem("token"));
		const config = {
			headers: {
				"content-type": "multipart/form-data",
				Authorization: `Token ${localStorage.getItem("token")}`,
			},
		};
	//	console.log(formData.getAll("password"));
		axios
			.post(path, formData, config)
			.then((res) => {
				console.log(res);
				if (res.data.err) {
					alert(res.data.err);
					SetState("upload");
				} else {
					var link = axios.defaults.baseURL + res.data.filePath;
					SetConvertedFile(link);
					SetState("finished");
				}
			})
			.catch((err) => {
				alert(err.message);
				SetState("upload");
			});
		return;
	}

	return (
		<div className="mt-2">
			<div className="container p-y-1">
				<div className="row m-b-1">
					<div className="col-sm-6 offset-sm-3">
						{state === "upload" && (
							<form className="form">
								<div className="form-group inputDnD">
									<label className="sr-only">File Upload</label>
									<div className="file-drop-area">
										{" "}
										<span className="choose-file-button   font-weight-bold">
											Choose files
										</span>{" "}
										<span className="file-message  font-weight-bold">
											or drag and drop files here
										</span>
										<Input
											Ref={fileUpload}
											onChange={readUrl}
											FileType={fileType}
										/>
									</div>
									{(window.location.pathname === "/unlockPdf" ||
										window.location.pathname === "/lockPdf") && (
										<input id="pass" type="text" name="password" />
									)}
								</div>

								<div id="images-previews"></div>

								<button
									type="button"
									className="btn btn-primary btn-block"
									onClick={handleSubmit}
									style={{ paddingLeft: "2.5rem", paddingRight: "2.5rem" }}
								>
									Convert
								</button>
							</form>
						)}
						{state === "processing" && (
							<div className="spinner-border text-primary" role="status">
								<span className="visually-hidden">Loading...</span>
							</div>
						)}
						{state === "finished" && (
							<>
								<a
									className="btn btn-primary m-3"
									rel="noopener"
									target="_blank"
									href={convertedFile}
									// onClick={SetState("upload")}
								>
									Download
								</a>
								<button
									className="btn btn-primary m-3"
									onClick={()=>SetState("upload")}
								>
									Back
								</button>
							</>
						)}
					</div>
				</div>
			</div>
		</div>
	);
};

export default Convert;
