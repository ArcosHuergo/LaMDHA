import plantaBaja from "../../assets/img/floors/plantaBaja.png";
import primerPiso from "../../assets/img/floors/primerPiso.png";
import entrepisoPlantaBaja from "../../assets/img/floors/entrepisoPlantaBaja.png";
import entrepisoSegundoPiso from "../../assets/img/floors/entrepisoSegundoPiso.png";
import segundoPiso from "../../assets/img/floors/segundoPiso.png";
import tercerPiso from "../../assets/img/floors/tercerPiso.png";

import { zonasPB, zonasEPB, zonasP1, zonasEP1, zonasP2, zonasP3 } from "./zonas";

export const pisos = {
    PB: { width: 2500, height: 1220, image: plantaBaja, zonas: zonasPB },
    EPB: { width: 2500, height: 1220, image: entrepisoPlantaBaja, zonas: zonasEPB },
    P1: { width: 2500, height: 1220, image: primerPiso, zonas: zonasP1 },
    EP1: { width: 2500, height: 610, image: entrepisoSegundoPiso, zonas: zonasEP1 },
    P2: { width: 2500, height: 610, image: segundoPiso, zonas: zonasP2 },
    P3: { width: 2500, height: 610, image: tercerPiso, zonas: zonasP3 },
}