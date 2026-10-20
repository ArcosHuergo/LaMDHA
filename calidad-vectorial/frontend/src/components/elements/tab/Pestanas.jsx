import './Pestanas.css';

export const Pestanas = ({ items, activa, onChange, className }) => (
    <nav className={`${className} pestanas`} role="tablist">
        {items.map(({ id, nombre }) => (
            <button
                key={id}
                role="tab"
                aria-selected={id === activa}
                className={`pestanas__tab ${id === activa ? 'pestanas__tab--activa' : ''}`}
                onClick={() => onChange(id)}
            >
                {id}
            </button>
        ))}
    </nav>
);