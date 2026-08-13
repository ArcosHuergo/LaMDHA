import { Outlet, useLocation, Link } from "react-router-dom";

import "./Layout.css";
import { Header } from "../components/elements/header/Header";

export const Layout = () => {
    return (
        <div className="body-layout">
            <Header />
            <Outlet />
        </div>
    )
}