/** @format */

import React from "react";
import { Link } from "react-router-dom";
import "./CSS/Header.css";

const Header = () => {
	function logOut() {
		localStorage.removeItem("user");
		localStorage.removeItem("token");
		window.location.reload();
	}

	return (
		<div className="Header">
			<nav className="navbar navbar-expand-lg navbar-light bg-light">
				<Link className="navbar-brand" to="#">
					DocumentEasy
				</Link>
				<button
					className="navbar-toggler"
					type="button"
					data-toggle="collapse"
					data-target="#navbarNav"
					aria-controls="navbarNav"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span className="navbar-toggler-icon"></span>
				</button>
				<div
					className="collapse navbar-collapse d-flex justify-content-between"
					id="navbarNav"
				>
					<ul className="navbar-nav">
						<li className="nav-item active">
							<Link className="nav-link" to="/">
								Home<span className="sr-only">(current)</span>
							</Link>
						</li>
						{/* <li className="nav-item">
          <Link className="btn nav-link" to="#">Merge PDF</Link>
        </li> */}
						<li className="dropdown">
							<button className="btn dropdown-toggle">PDF operations</button>
							<div className="dropdown-content">
								<Link to="/mergepdf">Merge PDF</Link>
								<Link to="/CompressPdf">Compress PDF</Link>
							</div>
						</li>
						<li>
							<div className="dropdown">
								<button className="btn dropdown-toggle">Secure PDF</button>
								<div className="dropdown-content">
									<Link to="/lockPdf">Lock PDF</Link>
									<Link to="/unlockPdf">Unlock PDF</Link>
								</div>
							</div>
						</li>
						<li>
							<div className="dropdown">
								<button className="btn dropdown-toggle">to PDF</button>
								<div className="dropdown-content">
									<Link to="/wordToPdf">Word to PDF</Link>
									<Link to="/pptToPdf">PPT to PDF</Link>
									<Link to="/xlToPdf">Excel to PDF</Link>
									<Link to="/imgtopdf">Image to PDF</Link>
								</div>
							</div>
						</li>

						{/*
        <li className="nav-item">
          <p>Hello,</p>
        </li>
         
         <li className="nav-item">
            <a className="nav-link" href="/login/logout">Log out</a>
          </li> */}
					</ul>
					<ul className="navbar-nav">
						{localStorage.getItem("user") == null && (
							<li className="nav-item">
								<Link className="nav-link" to="/register">
									Register
								</Link>
							</li>
						)}
						{localStorage.getItem("user") == null && (
							<li className="nav-item">
								<Link className="nav-link" to="/login">
									Login
								</Link>
							</li>
						)}
						{localStorage.getItem("user") !== null && (
							<li className="nav-item">
								<Link to="#" className="nav-link" onClick={logOut}>
									Logout
								</Link>
							</li>
						)}
					</ul>
				</div>
			</nav>
		</div>
	);
};

export default Header;
