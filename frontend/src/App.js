/** @format */

import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Header from "./components/Header";
import Login from "./components/Login";
import Register from "./components/Register";
import Home from "./components/Home";
import Imgtopdf from "./components/Convertions/ImgToPdf";
import MergePdf from "./components/PDFOperations/MergePdf";
import CompressPdf from "./components/PDFOperations/CompressPdf";
import WordToPdf from "./components/Convertions/WordToPdf";
import PPTToPdf from "./components/Convertions/PPTToPdf";
import ExcelToPdf from "./components/Convertions/ExcelToPdf";
import UnLockpdf from "./components/PDFOperations/UnLockpdf";
import Lockpdf from "./components/PDFOperations/Lockpdf";
import extractTextFromPdf from "./components/PDFOperations/extractTextFromPdf";
import SplitPdf from "./components/PDFOperations/SplitPdf";
function App() {
	return (
		<>
			<BrowserRouter>
				<Header />
				<Routes>
					<Route exact path="" element={<Home />}></Route>
					<Route exact path="/login" element={<Login />}></Route>
					<Route exact path="/wordToPdf" element={<WordToPdf />}></Route>
					<Route exact path="/pptToPdf" element={<PPTToPdf />}></Route>
					<Route exact path="/xlToPdf" element={<ExcelToPdf />}></Route>
					<Route exact path="/register" element={<Register />}></Route>
					<Route exact path="/imgtopdf" element={<Imgtopdf />}></Route>
					<Route exact path="/lockPdf" element={<Lockpdf />}></Route>
					<Route exact path="/unlockPdf" element={<UnLockpdf />}></Route>
					<Route exact path="/mergepdf" element={<MergePdf />}></Route>
					<Route
						exact
						path="/extractPdf"
						element={<extractTextFromPdf />}
					></Route>
					<Route exact path="/splitPdf" element={<SplitPdf />}></Route>
					<Route exact path="/CompressPdf" element={<CompressPdf />}></Route>
				</Routes>
			</BrowserRouter>
		</>
	);
}

export default App;
