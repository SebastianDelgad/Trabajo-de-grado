import React, { Fragment } from "react";
import logo_imagen from "../Assets/Images/logo-univalle.png";

export const NavbarLogin = () => {
  return (
    <Fragment>
      <div className="container mt-2 bg-light">
        <img
          className="img-responsive"
          src={logo_imagen}
          alt="logoLogin"
        />
      </div>
    </Fragment>
  );
};
