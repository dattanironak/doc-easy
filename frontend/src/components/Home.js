/** @format */

import React from "react";
import imageHome from "./images/home.jpg";

export default function Home() {
	return (
		<div className="d-flex align-items-center">
			<div className="col-md-6 col-lg-6 col-xl-5 mt-100 d-flex justify-content-center">
				<div >
					<h1>DocEasy</h1>
					<h2>Converting is simple now</h2>
				</div>
			</div>
			<div className="col-md-6 col-lg-6 col-xl-5">
				<img src={imageHome} className="img-fluid" alt="person" />
			</div>
		</div>
	);
}
