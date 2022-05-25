

import {
	faEnvelope,
} from "@fortawesome/fontawesome-free-solid";
import Input from "components/Input/Input";
import Button from "components/Button/Button";
import { authenticationService } from "services";
import { Form, Formik, ErrorMessage } from "formik";
import * as Yup from "yup";

function Register(props) {
	function handleRegister(
		{ username, password, confPass, email },
		{ setStatus, setSubmitting },
	) {
		if (password === confPass) {
			authenticationService
				.register({ username, email, password })
				.then((e) => {
					props.changeVal();
				})
				.catch((error) => {
					setSubmitting(false);
					setStatus(error.message);
				});
		}
	}
	return (
		<div className="container">
			<div className="row">
				<div className="col-sm-9 col-md-7 col-lg-5 mx-auto">
					<div className="card border-0 shadow rounded-3 my-5">
						<div className="card-body p-4 p-sm-5">
							<h2 className="card-title text-center mb-5">Sign Up</h2>
							<div>
								<Formik
									initialValues={{
										username: "",
										password: "",
										email: "",
										confPass: "",
									}}
									validationSchema={Yup.object().shape({
										username: Yup.string().required("Username is required"),
										password: Yup.string().required("Password is required"),
										email: Yup.string()
											.required("Email is required")
											.email("Email is Not valid"),
										confPass: Yup.string()
											.oneOf(
												[Yup.ref("password"), null],
												"Confirm Password is not same as above",
											)
											.required("Confirm password is required"),
									})}
									onSubmit={handleRegister}
								>
									{({
										setFieldValue,
										values,
										errors,
										status,
										touched,
										isSubmitting,
									}) => (
										<Form>
											<ErrorMessage
												name="username"
												component="div"
												className="invalid-feedback form-floating mb-3 d-flex justify-content-center"
											/>
											<div className="mb-3 d-flex form-floating justify-content-center">
												<label htmlFor="username" id="lblUser">
													Username
												</label>
												<Input
													name="username"
													type="username"
													label="lblUser"
													
													className={
														"form-control" +
														(errors.username && touched.username ? " is-invalid" : "")
													}
													value={values["username"]}
													setFieldValue={setFieldValue}
												/>
											</div>
											<ErrorMessage
												name="email"
												component="div"
												className="invalid-feedback form-floating mb-3 d-flex justify-content-center"
											/>
											<div className="form-floating mb-3 d-flex justify-content-center">
												<label htmlFor="email" id="lblEmail">
													Email
												</label>
												<Input
													name="email"
													type="email"
													label="lblEmail"
													icon={faEnvelope}
													className={
														"form-control" +
														(errors.email && touched.email ? " is-invalid" : "")
													}
													value={values["email"]}
													setFieldValue={setFieldValue}
												/>
											</div>
											<ErrorMessage
												name="password"
												component="div"
												className="invalid-feedback form-floating mb-3 d-flex justify-content-center"
											/>
											<div className="form-floating mb-3 d-flex justify-content-center">
												<label htmlFor="password" id="lblPass">
													Password
												</label>
												<Input
													name="password"
													type="password"
													label="lblPass"
													className={
														"form-control" +
														(errors.password && touched.password
															? " is-invalid"
															: "")
													}
													value={values["password"]}
													setFieldValue={setFieldValue}
												/>
											</div>
											<ErrorMessage
												name="confPass"
												component="div"
												className="invalid-feedback form-floating mb-3 d-flex justify-content-center"
											/>
											<div className="form-floating mb-3 d-flex justify-content-center">
												<label htmlFor="confPass" id="confPass">
													Confirm Password
												</label>
												<Input
													name="confPass"
													type="password"
													label="confPass"
													className={
														"form-control" +
														(errors.confPass && touched.confPass
															? " is-invalid"
															: "")
													}
													value={values["confPass"]}
													setFieldValue={setFieldValue}
												/>
											</div>

											{status && (
												<div className={"alert alert-danger"}>
													{status.toString()}
												</div>
											)}

											<div className="d-grid justify-content-center">
												<Button
													type="submit"
													value="Sign up"
													onClick={() => {}}
												></Button>
												{isSubmitting && (
													<img alt='load' src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
												)}
											</div>
											<hr class="my-4" />
											<div className="content">
												<h3>One of us ?</h3>
												<p>Great! Just Login Again</p>
												<Button
													value="Sign In"
													type="button"
													onClick={() => {
														props.changeVal();
													}}
												></Button>
											</div>
										</Form>
									)}
								</Formik>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
}

export default Register;





/** @format */

import { BehaviorSubject } from "rxjs";

import { handleResponse } from "helpers";
import axios from "axios";

const currentUserSubject = new BehaviorSubject(
	JSON.parse(localStorage.getItem("currentUser")),
);

const authenticationService = {
	login,
	logout,
	register,
	currentUser: currentUserSubject.asObservable(),
	get currentUserValue() {
		return currentUserSubject.value;
	},
};

async function login(username, password) {
	return axios
		.post(
			"users/authenticate",
			{ username, password },
			{
				headers: {
					"Content-Type": "application/json",
				},
			},
		)
		.catch(handleResponse)
		.then((response) => {
			console.log("here");
			localStorage.setItem("currentUser", JSON.stringify(response.data));
			currentUserSubject.next(response.data);
			return response.data;
		})
		.catch((error) => {
			return Promise.reject(error);
		});
}
async function register(user) {
	return axios
		.post("users/register", user, {
			headers: {
				"Content-Type": "application/json",
			},
		})
		.catch(handleResponse);
}

function logout() {
	// remove user from local storage to log user out
	localStorage.removeItem("currentUser");
	currentUserSubject.next(null);
}

export default authenticationService;