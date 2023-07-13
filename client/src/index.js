import React, { StrictMode } from "react";
import ReactDOM from "react-dom";
import App from "./App";
import "semantic-ui-css/semantic.min.css";
import axios from "axios";

axios.defaults.baseURL = process.env.REACT_APP_APP_URL;
// const backend_url = process.env.REACT_APP_APP_URL

ReactDOM.render(
  <StrictMode>
    <App />
  </StrictMode>,
  document.getElementById("root")
);
