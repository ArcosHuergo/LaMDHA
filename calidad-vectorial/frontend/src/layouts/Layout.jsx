import { Outlet, useLocation, Link } from 'react-router-dom';

import './Layout.css';
import { Header } from '../components/elements/header/Header';
import Aurora from '../components/elements/aurora/Aurora';

export const Layout = () => {
    return (
        <div className="body-layout">
            <Header />
            <div className='body-layout__content'>
                <Outlet />
            </div>

            <div className="body-layout__aurora">
                <Aurora
                    colorStops={['#7F0090', '#004AB8', '#4F0084']}
                    blend={1.0}
                    amplitude={1.0}
                    speed={1}
                />
            </div>
        </div>
    );
};
