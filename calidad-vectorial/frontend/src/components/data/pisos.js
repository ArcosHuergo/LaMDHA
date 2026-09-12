import primerPiso from "../../assets/img/floors/primerPiso.png";
import entrepisoPrimerPiso from "../../assets/img/floors/entrepisoPrimerPiso.png";
import entrepisoSegundoPiso from "../../assets/img/floors/entrepisoSegundoPiso.png";

import { zonasEP1, zonasP1 } from "./zonas";

export const pisos = {
    // S: { width: 2200, height: 1400, image: "plantaBaja", zonas: zonasPB },
    // PB: { width: 2200, height: 1400, image: "plantaBaja", zonas: zonasPB },
    P1: { width: 2500, height: 1220, image: primerPiso, zonas: zonasP1 },
    EP1: { width: 2500, height: 610, image: entrepisoSegundoPiso, zonas: zonasEP1 },
    // EP2: { width: 2200, height: 1400, image: "plantaBaja", zonas: zonasPB },
    // P2: { width: 2200, height: 1400, image: "plantaBaja", zonas: zonasPB },
    // P3: { width: 2200, height: 1400, image: "plantaBaja", zonas: zonasPB },
    // EP3: { width: 2200, height: 1400, image: "plantaBaja", zonas: zonasPB },
}