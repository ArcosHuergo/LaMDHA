import { Outlet } from 'react-router-dom';
import './Layout.css';
import { Header } from '../components/elements/header/Header';
import { PandhaIdle } from '../components/elements/pandha/PandhaIdle';
import Aurora from '../components/elements/aurora/Aurora';

export const Layout = () => {
    return (
        <div className="body-layout">
            <Header />
            <div className='body-layout__content'>
                <Outlet />
            </div>

            <PandhaIdle
                width={200}
                className='body-layout__pandha'
            />

            <div className="body-layout__aurora">
                <Aurora
                    colorStops={['#004AB8', '#4F0084', '#7F0090']}
                    blend={1.0}
                    amplitude={1.0}
                    speed={1}
                    width={'100%'}
                    heigth={'100%'}
                />
            </div>
        </div>
    );
};
