import React, { Fragment, useState } from "react";
import logo_imagen from "../Assets/Images/icon-univalle.png";
import { auth } from "../firebase";
import { useHistory } from "react-router-dom";
import { Helmet } from "react-helmet";

export const PagChangePass = () => {
  let history = useHistory();

  function handleClickRegresar() {
    history.push("/login");
  }

  const [email, setEmail] = useState("");
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const forgotPassword = (email) => {
    auth
      .sendPasswordResetEmail(email)
      .then(function () {
        setSuccess(
          "Se ha enviado un email para la recuperación por favor verifica el correo..."
        );
      })
      .catch(function (e) {
        console.log(e);
        if (e.code === "auth/invalid-email") {
          setError("Ingrese un correo válido");
        }
        if (e.code === "auth/missing-email") {
          setError("Ingrese un correo, el campo está vacío!!");
        }
      });
  };

  return (
    <Fragment>
      <Helmet>
          <title>Recuperar contraseña - SISCOD</title>
        </Helmet>
      <div className="container mt-3 bg-light rounded-6">
        <div className="row">
        <div className="mt-3 mb-4 col-8 col-sm-9 col-xs-9 col-md-9 col-lg-9 col-xl-9 col-xxl-9">
          <div className="row">
          <div className="col-3 col-sm-3 col-xs-2 col-md-2 col-lg-2 col-xl-1 col-xxl-1">
            <img src={logo_imagen} alt="logoLogin"/>
            </div>
            <div className="mt-3 col-5">
              <strong className="text-danger ">SISCOD</strong>
              </div>
            </div>
          </div>
          <div className="mt-4 mb-4 col-4 col-sm-3 col-xs-3 col-md-3 col-lg-3 col-xl-3 col-xxl-3 mt-3">
            <div className="btn-toolbar">
              <u className="nav-link" onClick={handleClickRegresar}>
                <div className="row">
                  <div className="col-3 col-sm-3 col-xs-3 col-md-3 col-lg-3 col-xl-3 col-xxl-3">
                    <span className="material-icons md-36">&#xe5c4;</span>
                  </div>
                  <div className="col-9 col-sm-9 col-xs-9 col-md-9 col-lg-9 col-xl-9 col-xxl-9">
                    <span> Regresar </span>
                  </div>
                </div>
              </u>
            </div>
          </div>
        </div>
      </div>
      <div className="container mt-3 bg-light rounded-6">
        <div className="row mt-3 justify-content-center">
          <h4 className="text-responsive mt-3">
            {" "}
            Por favor ingrese el correo para recuperar la contaseña{" "}
          </h4>
        </div>
        <div className="row mt-3 justify-content-center">
          <div className="col-7 col-sm-7 col-xs-7 col-md-7 col-lg-7 col-xl-7 col-xxl-7">
            <input
              type="email"
              className="form-control"
              placeholder="Ingrese el correo"
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
        </div>
        <div className="row mt-2 justify-content-center">
          {error ? (
            <div className="alert alert-danger col-7">{error}</div>
          ) : null}
        </div>
        <div className="row mt-2 justify-content-center">
          {success ? (
            <div className="alert alert-success col-7">{success}</div>
          ) : null}
        </div>
        <div className="row mt-3 justify-content-center">
          <div className="col-4 col-sm-4 col-xs-4 col-md-4 col-lg-4 col-xl-4 col-xxl-4">
            {" "}
          </div>
          <div className="mb-3 col-6 col-sm-6 col-xs-6 col-md-6 col-lg-6 col-xl-6 col-xxl-5">
            <button
              className="btn btn-outline-danger"
              onClick={() => forgotPassword(email)}
            >
              <span> Enviar </span>
            </button>
          </div>
        </div>
      </div>
    </Fragment>
  );
};
