import React  from 'react';
import { Link,useNavigate } from 'react-router-dom';
import axios from 'axios';

const Login = () => {

  const navigate = useNavigate();
  function handleSubmit(){

    let user = {
      "username" : document.getElementById("username").value,
      "password" : document.getElementById("password").value
    }
    console.log(user)
    axios.post(`api/users/login`,user)
    .then(res => {
      if(res.data.err)
      {
        alert(res.data.err);
      }
      else
      {
        console.log(res);
        localStorage.setItem('token',res.data.token);
        localStorage.setItem('user',res.data.user);
        navigate('/');
        window.location.reload();
      }
    })
    return;
  }
  return (
  <div>
      <section className="vh-100">
    <div className="container-fluid h-custom">
      <div className="row d-flex justify-content-center align-items-center h-100">
        <div className="col-md-9 col-lg-6 col-xl-5">
          <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp" className="img-fluid" alt="person" />
        </div>

        <div className="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
        <p className="text-center h1 fw-bold mb-5 mx-1 mx-md-4 mt-4">Log In</p>

          <form name="regForm">
       
            
            <div className="form-outline mb-4">
              <input type="text" id="username" name="username" className="form-control form-control-lg"
                placeholder="Enter a valid username" />
              <label className="form-label" >Username</label>
            </div>
  
         
            <div className="form-outline mb-3">
              <input type="password" id="password" name="password" className="form-control form-control-lg"
                placeholder="Enter password" />
              <label className="form-label" >Password</label>
            </div>
  
            <div className="d-flex justify-content-between align-items-center"></div>
             
  
            <div className="text-center text-lg-start mt-4 pt-2">
              <button type="button" className="btn btn-primary btn-lg" onClick={handleSubmit}
                style={{paddingLeft:"2.5rem" , paddingRight:"2.5rem"}}>Login</button>


              <p className="small fw-bold mt-2 pt-1 mb-0">Don't have an account? <Link to="/register"
                  className="link-danger">Register</Link></p>
            </div>
  
          </form>
        </div>
      </div>
    </div>
    
  </section>

  </div>
  )
};
export default Login;